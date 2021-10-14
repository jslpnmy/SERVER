from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('users/', views.UserList.as_view(), name='users'),
    path('users/<int:pk>/', views.EachUser.as_view(), name='each_user'),
    path('signup/', views.signup, name='signup'),
    path('mainscreen/', views.MainScreen.as_view(), name='mainscreen'),
    path('login/', views.LogIn, name='login'),
    path('posting/', views.posting, name='posting'),
    path('user/', views.trace_user, name='trace_user_by_token'),
    path('own_content/', views.trace_content, name='trace_content_by_token'),
    path('del_content/', views.delete_content, name='delete_content'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
