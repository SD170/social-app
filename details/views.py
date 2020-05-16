from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .models import *
from .forms import UserForm

# Create your views here.
@login_required(login_url='/login/')
def home(request):

    user = request.user

    context = {
        'user' : user,
    }

    return render(request, 'details/home_page.html', context)

def register_page(request):
    user_form = UserForm()
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.refresh_from_db() 

            user.profile.full_name = user_form.cleaned_data.get('full_name')
            user.profile.birth_date = user_form.cleaned_data.get('birth_date')
            user.profile.email = user_form.cleaned_data.get('email')
            user.profile.gender = user_form.cleaned_data.get('gender')
            user.save()

            raw_password = user_form.cleaned_data.get('password1')
            username = user.username
            
            checked_user = authenticate(username=username, password=raw_password)
            login(request,checked_user)

            return redirect('home')

    context = {
        'user_form' : user_form,
    }

    return render(request, 'details/register_page.html', context)

def login_page(request):

    username = request.POST.get('username')
    password = request.POST.get('password')

    checked_user = authenticate(request, username=username, password = password)

    if request.user.is_authenticated:
        user=request.user
        return HttpResponse("Your'e alrady logged in")


    if checked_user is not None:
        login(request,checked_user)
        return redirect('home')
    else:
        messages.info(request,'Username or Password not correct')

    context={}
    return render(request, 'details/login_page.html', context)

@login_required(login_url='/login/')
def logout_page(request):
	logout(request)
	return redirect('login')

@login_required(login_url='/login/')
def friend_list(request):

    user = request.user
    friends_list = user.friendlist_set.all() | user.profile2.all()
    no_of_friends = user.friendlist_set.all().count() + user.profile2.all().count()
    context={
        'user':user,
        'friends':friends_list,
        'no_of_friends':no_of_friends
    }

    return render(request, 'details/friend_list.html', context)

@login_required(login_url='/login/')
def profile_page(request,pk):
    current_user = request.user
    view_user = User.objects.get(id=pk)
    is_sent = False
    is_received = False
    is_friends = False
    
    
    if(FriendList.objects.filter(profile1=current_user,profile2=view_user, is_friends = True).exists() | FriendList.objects.filter(profile1=view_user,profile2=current_user, is_friends = True).exists()):
        is_friends=True

    elif(FriendRequest.objects.filter(sender=current_user,reciever=view_user, is_sent=True).exists()):
        is_sent=True
    elif(FriendRequest.objects.filter(sender=view_user,reciever=current_user, is_sent=True).exists()):
        is_received = True
            

    print('view_user' , view_user,
        'current_user' , current_user,
        'is_sent' , is_sent,
        'is_friends' , is_friends)
 
    context={
        'view_user' : view_user,
        'current_user' : current_user,
        'is_sent' : is_sent,
        'is_friends' : is_friends,
        'is_received' : is_received,
    }

    return render(request, 'details/profile_page.html', context)

@login_required(login_url='/login/')
def send_request(request,pk):
    sender = request.user
    reciever = User.objects.get(id=pk)
    FriendRequest.objects.create(sender=sender,reciever=reciever, is_sent=True)
    return redirect('profilepage',pk=pk)

@login_required(login_url='/login/')
def potential_friends(request):
    current_user = request.user
    all_user = User.objects.filter().exclude(username=current_user)
    all_friends = current_user.friendlist_set.all() | current_user.profile2.all()
    new_friends = all_user
    for i in all_friends:
        new_friends = new_friends.exclude(pk=i.profile1.pk)
        new_friends = new_friends.exclude(pk=i.profile2.pk)
    no_of_friends = new_friends.count()

    context={
        'current_user' : current_user,
        'new_friends' : new_friends,
        'no_of_friends' : no_of_friends
    }
    return render(request, 'details/potential_friends.html',context)

@login_required(login_url='/login/')
def friend_request(request):
    current_user = request.user
    friend_request_recieved = FriendRequest.objects.filter(reciever=current_user,is_sent=True)

    if request.method == 'POST' and 'accept' in request.POST:
        
        sender=User.objects.get(id=int(request.POST.get('sender')))
        reciever=User.objects.get(id=int(request.POST.get('reciever')))
        FriendList.objects.create(profile1=sender, profile2=reciever, is_friends = True)
        FriendRequest.objects.get(sender=sender, reciever=reciever).delete()

    if request.method == 'POST' and 'reject' in request.POST:
        FriendRequest.objects.get(sender=sender, reciever=reciever).delete()

    context={
        'current_user' : current_user,
        'friend_request_recieved' : friend_request_recieved,
    }
    return render(request, 'details/friend_request.html',context)

