#Users views#

#Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from users.forms import ProfileForm, SignupForm
from django.views.generic import TemplateView

#Utilities
from django.utils.decorators import method_decorator

from users.models import Profile


@method_decorator(login_required, name='dispatch')
class UpdateProfile(TemplateView):
    def post(self, request):
        profile = request.user.profile
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()
        return redirect('users:login')
    def get(self, request):
        profile = request.user.profile
        form = ProfileForm()
        return render(
            request=request,
            template_name='users/update_profile.html',
            context={
                'profile': profile,
                'user': request.user,
                'form': form
            }
        )


class LoginView(TemplateView):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('posts:feed')
        else:
            return redirect(request, 'users/login.html', {'error':'Invalid username and password'})
    def get(self, request):
        if not request.user.is_anonymous:
            return redirect('posts:feed')
        return render(request, 'users/login.html')


@method_decorator(login_required, name='dispatch')
class LogoutView(TemplateView):
        def get(self, request):
            logout(request)
            return redirect('users:login')


class SignupView(TemplateView):
    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create(
                username=form.cleaned_data.get('username'),
                first_name=form.cleaned_data.get('first_name'),
                last_name=form.cleaned_data.get('last_name'),
                email=form.cleaned_data.get('email'),
                password=form.cleaned_data.get('password')
            )
            user.save()
            profile = Profile.objects.create(
                user=user
            )
            login(request, user)
            return redirect('posts:feed')
        else:
            form = SignupForm()
            return render(
                request=request,
                template_name='users/signup.html',
                context={'form':form}
            )

    def get(self,request):
        form = SignupForm()
        if not request.user.is_anonymous:
            return redirect('posts:feed')
        return render(
            request=request,
            template_name='users/signup.html',
            context={'form':form}
        )


@method_decorator(login_required, name='dispatch')
class AccountView(TemplateView):
    def get(self,request):
        if not request.user.is_anonymous:
            return render(
                request=request,
                template_name='users/detail.html'
            )
