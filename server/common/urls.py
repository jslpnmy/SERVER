from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('users/<int:pk>/', views.EachUser.as_view(), name='each_user'),
    path('signup/', views.signup, name='signup'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
