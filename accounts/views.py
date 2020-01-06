from django.contrib.auth import get_user_model, authenticate, login
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.base import View
User = get_user_model()


# Create your views here.


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('404_'))
        return render(request, template_name='accounts/register.html')


class LoginView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('404_'))
        return render(request, template_name='accounts/login.html')

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            data = request.POST
            username = data['username']
            password = data['password']
            user_qs = User.objects.filter(username__iexact=username)
            if user_qs.exists(): #and user_qs.active is True:
                user = authenticate(username=username, password=password)
                login(request, user)
                return JsonResponse({'message': 'Logged In Successfully!'}, status= 200)
            return JsonResponse({'message': 'Error With User!'}, status=400)
        return JsonResponse({'message':'Method Not Allowed!'}, status=400)