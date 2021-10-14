from .models import Profile, Posting
from .serializers import ProfileSerializer, PostSerializer
from rest_framework import generics, status
from rest_framework.decorators import api_view
from .ai import sentiment_predict
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.models import User
from .pagination import LargeResultsSetPagination


class UserList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class EachUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class MainScreen(generics.ListAPIView):
    queryset = Posting.objects.all() #모든 게시물 정보 보내기 nickname, token, content, (image)
    serializer_class = PostSerializer
    pagination_class = LargeResultsSetPagination


@api_view(['POST'])
def signup(request): #회원가입, request = {nickname, email, password}
    if request.method == 'POST':
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():

            if Profile.objects.filter(nickname=serializer.data['nickname']).exists():
                return Response({'message':"name already exists"}, safe=False) #같은 이름이 이미 존재할 때
            elif Profile.objects.filter(nickname=serializer.data['email']).exists():
                return Response({'message':"email was already used"}) #이미 사용된 이메일일 때
            else:
                # 테이블 생성
                user = User.objects.create_user(username=request.data['nickname'], password=request.data['password'])

                token = Token.objects.create(user=user)
                Profile.objects.create(
                    user = user,
                    nickname = serializer.data['nickname'],
                    email = serializer.data['email'],
                    password = serializer.data['password'],
                    token = token.key,
                )
                return Response({'message':'success', 'token':token.key}) #회원가입 성공
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST) #request가 옳지 않을 때


@api_view(['GET'])
def LogIn(request): #request = {email, password}
    if Profile.objects.filter(email=request.data['email'],
                              password=request.data['password']).exists(): #해당 정보의 user가 존재하는지 확인
        return Response({'success':'true', 'token':Profile.objects.filter(email=request.data['email'], password=request.data['password']).values('token')}) #존재할 때
    else:
        return Response({'success':'false', 'token':'null'}) #존재하지 않을 때


@api_view(['POST', 'GET'])
def posting(request): #request = {nickname, token, content, (image)}
    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            if Profile.objects.filter(nickname=serializer.data['nickname']).exists():
                sentiment = sentiment_predict(serializer.data['content']) #해당 글의 해악성 판독

                if sentiment >= 65: #해악성이 65%가 넘으면
                    return Response({'message': "too high sentiment"})
                else:
                    if 'image' in request.FILES: #이미지가 있을 때
                        Posting.objects.create(
                            nickname=serializer.data['nickname'],
                            token= serializer.data['token'],
                            content=serializer.data['content'],
                            image=serializer.FILES['image'],
                        )
                    else: #이미지가 없을 때
                        Posting.objects.create(
                            nickname=serializer.data['nickname'],
                            token=serializer.data['token'],
                            content=serializer.data['content'],
                        )
                    return Response({'success':'true', 'sentiment' : sentiment})
            else:
                return Response({'success':'false', 'message':"nickname does not exist"})
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        try:
            snippet = Posting.objects.get()
        except Posting.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)

        serializer = PostSerializer(snippet)
        return Response(serializer.data)


#token으로 user 찾기
@api_view(['GET'])
def trace_user(request): #request={token}
    if Profile.objects.filter(token=request.data['token']).exists():
        return Response({'success':'true', 'nickname':Profile.objects.filter(token=request.data['token']).values('nickname'), 'token':request.data['token']})
    else:
        return Response({'success':'false', 'nickname':'null', 'token':request.data['token']})


@api_view(['GET'])
def trace_content(request): #request={token}
    if Posting.objects.filter(token=request.data['token']).exists():
        return Response({'success':'true', 'content':Posting.objects.filter(token=request.data['token']).values('nickname', 'content', 'image'), 'token':request.data['token']})
    else:
        return Response({'success':'false', 'content':'null', 'token':request.data['token']})


@api_view(['PUT'])
def delete_content(request): #request={content, token}
    if Posting.objects.filter(token=request.data['token']).exists():
        if Posting.objects.filter(content=request.data['content']).exists():
            snippet = Posting.objects.filter(token=request.data['token'], content=request.data['content'])
            snippet.delete()

            return Response({'success':'true'})
        else:
            return Response({'success':'false', 'message': 'content does not exist'})
    else:
        return Response({'success':'false', 'message': 'token does not exist'})
