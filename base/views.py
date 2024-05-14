from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Universe, Movie, Message, UserProfile
from django.db.models import Q
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(request):
    
    q = request.GET.get('q','') 
    universe = Universe.objects.filter(
        Q(name__icontains=q) |
        Q(genres__name__icontains=q)
    ).distinct()
    context = {'universes':universe}
    return render(request,'base/home.html',context)

def movies(request,pk):
    universe = Universe.objects.get(id=pk)
    movies = Movie.objects.filter(universe = universe)
    context = {'universe':universe,'movies':movies}
    return render(request,'base/movies.html',context)

@login_required(login_url='login')
def chatroom(request,pk):
    universe = Universe.objects.get(id=pk)
    room_messages = universe.message_set.all()
    participants = universe.participants.all()
    if request.method == "POST":
        message = Message.objects.create(
            user = request.user,
            room = universe,
            body = request.POST.get('body')
        )
        universe.participants.add(request.user)
        return redirect('chat-room', pk=universe.id)     
    
    context = {'room_messages':room_messages,'universe':universe, 'participants':participants}
    return render(request,'base/chatroom.html',context)

def logme(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            return HttpResponse('no user found')
        
        user = authenticate(request, username = username, password = password)
        
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('password did not matched')
    return render(request,'base/login.html')



def profile(request, pk):
    user = get_object_or_404(User, id=pk)
    profile = UserProfile.objects.get(user=user)
    return render(request, 'base/profile1.html', {'user': user, 'profile': profile})


def profileEdit(request, pk):
    if request.method == 'POST':
        user = get_object_or_404(User, id=pk)
        profile = UserProfile.objects.get(user=user) 
              
        fullname = request.POST.get('fullname')
        interested_genre = request.POST.get('interested_genre')
        about = request.POST.get('about')
        insta = request.POST.get('insta')
        twitter = request.POST.get('twitter')
        facebook = request.POST.get('facebook')
        linkedin = request.POST.get('linkedin')
        
        profile.interested_genres = interested_genre
        profile.fullname = fullname
        profile.interest_topics = about
        profile.instagram = insta
        profile.twitter = twitter
        profile.facebook = facebook
        profile.linkedin = linkedin
        profile.save()
        return redirect('home')
    return render(request, 'base/profile2.html')

def logmeout(request):
    logout(request)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            return HttpResponse('Passwords do not match')
        if User.objects.filter(username=username).exists():
            return HttpResponse('Username is already taken')
        user = User.objects.create_user(username=username, email=email, password=password1)
        UserProfile.objects.create(user=user,fullname=user)
        user = authenticate(username=username, password=password1)
        login(request, user)
        return redirect('home')

    return render(request, 'base/register.html')