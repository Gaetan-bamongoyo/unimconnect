from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.db.models import Count

# Create your views here.

def loginPage(request):
    return render(request, 'login.html')

def createUser(request):
    if request.method == 'POST':
        username = request.POST.get('matricule')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if CustomerUser.objects.filter(username = username).exists():
            return render(request, 'message.html')
        else:
            form = CustomerUser(
                username = username,
                email = email,
                password = password,
                acces = 1,
                is_superuser = 0
            )
            form.set_password(password)
            form.save()
            return render(request, 'login.html')

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('matricule')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user is not None:
            auth_login(request, user)
            return redirect('postapp:homepage')
        else:
            return redirect('postapp:login')

@login_required
def dashboardPage(request):
    post = Post.objects.annotate(nb_commentaire=Count('user_id')).prefetch_related('user_id')
    return render(request, 'dashboard.html', {'posts':post})

@login_required
def createPost(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        if request.method == 'POST':
            description = request.POST.get('description')
            image = request.FILES.get('image')
            lieu = request.POST.get('lieu')
            user_id_id = CustomerUser.objects.get(id=user_id)
            user_id_id.id
            form = Post(
                description = description,
                image = image,
                lieu = lieu,
                user_id = user_id_id
            )
            form.save()
            return redirect('postapp:homepage')
    else:
        return redirect('postapp:login')

