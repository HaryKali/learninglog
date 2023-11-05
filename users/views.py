from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    """注册新用户"""
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
    if form.is_valid():
        new_user = form.save()
        authenticated_user = authenticate(username=new_user.username,
                                         password=request.POST['password1'])
        print("here")
        login(request, authenticated_user)
        return HttpResponseRedirect(reverse('index'))

    context = {'form': form}
    return render(request, '../templates/users/register.html', context)