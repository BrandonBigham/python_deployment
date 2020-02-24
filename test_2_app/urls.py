from django.urls import path
from . import views	

urlpatterns = [
    path('', views.index),
    path('users', views.createUser),
    path('login', views.login),
    path('homepage', views.homepage),
    path('logout', views.logout),
    path('createpost', views.createpost),
    path('delete/<int:id>', views.deletepost),
    path('like/<int:id>', views.likepost),
    path('unlike/<int:id>', views.unlikepost),
    path('user/<int:id>', views.userprofile),
    path('edit/<int:id>', views.edituser),
    path('edit/<int:id>/proccess', views.edituserproccess)
]