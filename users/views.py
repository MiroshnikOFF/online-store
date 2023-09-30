import random

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from config import settings
from users.forms import UserRegisterForm, UserForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        user = form.save()
        key = ''.join([str(random.randint(0, 9)) for _ in range(12)])
        user.key = key
        send_mail(
            subject='Подтверждение электронной почты',
            message=f'Код для подтверждения: {key}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


class LoginView(BaseLoginView):
    template_name = 'users/login.html'

    def get_success_url(self):
        user = self.request.user
        if user.is_verified:
            return reverse('catalog:home')
        return reverse('users:verification')


class LogoutView(BaseLogoutView):
    pass


class UserUpdateView(UpdateView):
    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserForm

    def get_object(self, queryset=None):
        return self.request.user


def email_verification(request):
    if request.method == 'POST':
        input_key = request.POST.get('key')
        try:
            user = User.objects.get(key=input_key)
            user.is_verified = True
            user.save()
        except User.DoesNotExist:
            return render(request, 'users/unsuccessful_verification.html')
        return render(request, 'users/successful_verification.html')
    return render(request, 'users/verification.html')


def password_recovery(request):
    if request.method == 'POST':
        new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])
        input_email = request.POST.get('email')
        try:
            user = User.objects.get(email=input_email)
            user.set_password(new_password)
            user.save()
            send_mail(
                subject='Восстановление доступа',
                message=f'Ваш новый пароль: {new_password}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],
            )
        except User.DoesNotExist:
            return render(request, 'users/unsuccessful_recovery.html')
        return render(request, 'users/successful_recovery.html')
    return render(request, 'users/password_recovery.html')