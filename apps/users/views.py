from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError
from .forms import RegisterForm, LoginForm, UserProfileForm
from .models import UserProfile


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'auth/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                UserProfile.objects.create(user=user)
                messages.success(request, 'Account created successfully! Please login.')
                return redirect('users:login')
            except IntegrityError:
                messages.error(request, 'An error occurred during registration. Please try again.')
                form = RegisterForm()
                return render(request, 'auth/register.html', {'form': form})
        return render(request, 'auth/register.html', {'form': form})


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'auth/login.html', {'form': form})

    def post(self, request):
        try:
            form = LoginForm(request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                messages.success(request, f'Welcome back, {user.username}!')
                return redirect('dashboard:dashboard')
            return render(request, 'auth/login.html', {'form': form})
        except Exception as e:
            messages.error(request, 'An error occurred during login. Please try again.')
            form = LoginForm()
            return render(request, 'auth/login.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'You have been logged out.')
        return redirect('users:login')


class ProfileView(LoginRequiredMixin, View):
    login_url = 'users:login'

    def get(self, request):
        profile, _ = UserProfile.objects.get_or_create(user=request.user)
        form = UserProfileForm(instance=profile)
        return render(request, 'auth/profile.html', {'form': form, 'profile': profile})

    def post(self, request):
        profile, _ = UserProfile.objects.get_or_create(user=request.user)
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('users:profile')
        return render(request, 'auth/profile.html', {'form': form, 'profile': profile})
