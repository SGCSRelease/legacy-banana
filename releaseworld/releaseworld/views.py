from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return render(request, 'registration/register.html', {"form":form})

    return render(request, 'registration/register.html', {"form":form})

def register_done(request):
    return render(request, 'registration/register_done.html')
