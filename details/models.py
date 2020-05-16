from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):

    Gender = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    birth_date = models.DateTimeField(null=True, blank=True, auto_now=True)
    gender = models.CharField(max_length=20, choices=Gender, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    def __str__(self):
        if self.full_name == None:
            return "Full Name is NULL"
        return self.full_name

# class Friend(models.Model):
#     profile = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)


class FriendList(models.Model):
    profile1 = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    profile2 = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='profile2')
    is_friends = models.BooleanField(default=False)

    def __str__(self):
        return str('%s <-> %s' % (self.profile1.username, self.profile2.username))


class FriendRequest(models.Model):
    sender = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='sender')
    reciever = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='reciever')
    is_sent = models.BooleanField(default=False)

    def __str__(self):
        return str('%s -> %s' % (self.sender.username, self.reciever.username))