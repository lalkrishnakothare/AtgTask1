import json

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, get_user_model
from django.utils.safestring import mark_safe
User = get_user_model()

# Create your views here.
@login_required()
def homepage(request):
    return render(request, 'PublicChatRoom/homepage.html')

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            render(request, 'registration/register.html', {'form':form})

    return render(request, 'registration/register.html', {'form':form})

@login_required()
def updateuser(request, user_id):
    user = get_object_or_404(get_user_model(), pk=user_id)
    form = UserChangeForm(request.POST, instance=user)
    if request.method =='POST':
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('/')
    return render(request, 'registration/update.html', {'form':form})

@login_required()
def searchuser(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
        users = User.objects.filter(username__contains=search_text)
        return render(request, 'registration/search.html',{'search_text':search_text, 'users':users})
    else:
        return render(request, 'registration/search.html')

@login_required()
def chatroom(request):
    return render(request, 'PublicChatRoom/chatroom.html', {
        'username': mark_safe(json.dumps(request.user.username)),
    })
