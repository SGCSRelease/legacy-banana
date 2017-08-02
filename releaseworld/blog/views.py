from django.shortcuts import render, redirect
from django.contrib.auth.views import login


def BlogHome(request, username):
    user = request.user

    return render('home.html', { 'user':user })

def LoginCheck(request):
    if request.user.is_authenticated():
        return redirect('BlogHome', username=request.user.username)
    return redirect('../accounts/login/')
