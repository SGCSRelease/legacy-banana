from django.urls.base import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def blog_home(request, username):
    user = User.objects.get(username=request.user)

    return render(request, 'blog/home.html', {'user':user})

def login_check(request):
    if request.user.is_authenticated():
        username = str(request.user)
        return redirect('./blog_home', username=username)
    return redirect('../accounts/login/')

