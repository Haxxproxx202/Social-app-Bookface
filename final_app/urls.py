"""final_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from sns.views import MainView, LoginView, LogoutView, RegisterView, WallView, SettingsView, FriendsView, \
                        add_friend_view, like_view, delete_friend_view, ChangePasswordView, EditProfileView, \
                        ProfileView, CommentView, play_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name="main"),
    path('wall/', WallView.as_view(), name="wall"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/', RegisterView.as_view(), name="register"),
    path('settings/', SettingsView.as_view(), name="settings"),
    path('friends/', FriendsView.as_view(), name="friends"),
    path('add_friend/<int:id_>/', add_friend_view, name="add-friend"),
    path('delete_friend/<int:id_>/', delete_friend_view, name="delete-friend"),
    path('like/<int:pk>', like_view, name='like_post'),
    path('settings/profile/', ProfileView.as_view(), name="profile"),
    path('settings/edit/', EditProfileView.as_view(), name="edit-profile"),
    path('settings/pw/', ChangePasswordView.as_view(), name="change-pw"),
    path('comment/<int:id_>/', CommentView.as_view(), name="comment"),
    path('play/', play_view, name='games'),

]
