from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, LoginView, LogoutView, UserUpdateView, email_verification, password_recovery

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('verification/', email_verification, name='verification'),
    path('recovery/', password_recovery, name='recovery'),
]
