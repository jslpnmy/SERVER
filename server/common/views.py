from .models import Profile, Posting
from .serializers import ProfileSerializer, PostSerializer
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .ai import sentiment_predict
from rest_framework.authtoken.models import Token


class EachUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


@api_view(['GET'])
def mainscreen():
    return Posting.objects.all() #모든 게시물 정보 보내기 nickname, token, content, (image)


@api_view(['POST'])
def signup(request): #회원가입
    if request.method == 'POST':
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            if Profile.objects.filter(nickname=request.data['nickname']).exist():
                return Response(serializer.data, status={'message':"name already exists"}) #같은 이름이 이미 존재할 때
            elif Profile.objects.filter(nickname=request.data['email']).exist():
                return Response(serializer.data, status={'message':"email was already used"}) #이미 사용된 이메일일 때
            else:
                token = Token.objects.create(user=request.data['nickname']) #token 생성
                # 테이블 생성
                User.objects.create(
                    nickname = request.data['nickname'],
                    email = request.data['email'],
                    password = request.data['password'],
                    token = token.key,
                )
                return Response(serializer.data, status={'message':'success', 'token':token.key}) #회원가입 성공
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #request가 옳지 않을 때


@api_view(['GET'])
def LogIn(request):
    if Profile.objects.filter(email=request.email, password=request.password).exist(): #해당 정보의 user가 존재하는지 확인
        return Response(status={'success':'true', 'token':Profile.objects.filter(email=request.email, password=request.password).value()['token']}) #존재할 때
    else:
        return Response(status={'success':'false', 'token':'null'}) #존재하지 않을 때


@api_view(['POST', 'GET'])
def posting(request):
    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            sentiment = sentiment_predict(request.data['content']) #해당 글의 해악성 판독

            if sentiment >= 65: #해악성이 65%가 넘으면
                return Response(serializer.data, status="too high sentiment")
            else:
                if 'image' in request.data: #이미지가 있을 때
                    Posting.objects.create(
                        nickname=serializer.data['nickname'],
                        token=serializer.data['token'],
                        content=serializer.data['content'],
                        image=request.data['image'],
                    )
                else: #이미지가 없을 때
                    Posting.objects.create(
                        nickname=serializer.data['nickname'],
                        token=serializer.data['token'],
                        content=serializer.data['content'],
                    )
                return Response(status={'success':'true', 'token':serializer.data['token']})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        try:
            snippet = Posting.objects.get()
        except Posting.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PostSerializer(snippet)
        return Response(serializer.data)


#token으로 user 찾기
@api_view(['GET'])
def trace_user(request):
    if Profile.objects.filter(token=request.data['token']).exist():
        return Response(status={'success':'true', 'nickname':Profile.objects.filter(token=request.data['token']).value()['nickname'], 'token':request.data['token']})
    else:
        return Response(status={'success':'false', 'nickname':'null', 'token':request.data['token']})
