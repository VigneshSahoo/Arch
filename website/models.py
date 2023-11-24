from django.db import models
from django.forms import ModelForm
from django.contrib import admin
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TotalUsers(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password2', 'password1', 'first_name', 'last_name']


class Services(models.Model):
    s_name = models.CharField(max_length=100)
    s_description = models.CharField(max_length=250, blank=True, null=True)
    s_price = models.IntegerField()
    objects = models.Manager()

    class Meta:
        db_table = 'services_offered'


class ServicesForm(ModelForm):

    class Meta:
        model = Services
        fields = ['s_name', 's_description', 's_price']


class Room(models.Model):
    a1 = models.CharField(max_length=100)
    a2 = models.IntegerField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class User(models.Model):
    # null is for DB & blank is for HTML
    u_id = models.CharField(max_length=20, blank=False, null=False)
    u_name = models.CharField(max_length=100, blank=False, null=False)
    u_email = models.EmailField(blank=False, null=False)
    u_contact = models.CharField(max_length=15, null=False)
    objects = models.Manager()

    class Meta:
        db_table = "user"


class Subscription(models.Model):
    sub_name = models.CharField(max_length=100)
    sub_email = models.EmailField(max_length=100)
    objects = models.Manager()

    class Meta:
        db_table = 'subscribers'


class SubscriptionForm(ModelForm):
    class Meta:
        model = Subscription
        fields = [
            'sub_name',
            'sub_email',
        ]


class RegisteredUsers(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    objects = models.Manager()


class RegisteredUsersAdmin(admin.ModelAdmin):
    list_display = ['username', 'password']


admin.site.register(RegisteredUsers, RegisteredUsersAdmin)
