from datetime import date, datetime
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django import forms


# Create your models here.


class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE ,null=True)
    bio = models.TextField(max_length=500, blank=True , null=True )
    phone_number = models.CharField(max_length=12, blank=True , null=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_image=models.ImageField (default="Group-user.jpg" , null=True , blank=True)
    

class Expense(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)
    amount = models.FloatField(null=True , max_length=42)
    category = models.CharField(null=True , max_length=255 )
    description =models.TextField(null=True ,max_length=255)
    date= models.DateField(null=True , blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    
    class Meta:
      db_table = "Expense"
      ordering : ("-date")
    def __str__(self):
        return self.category

class Income(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)
    income = models.IntegerField(null=True )
    source = models.CharField(null=True , max_length=255 )
    date= models.DateField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    
    class Meta:
      db_table = "Income"

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name


# Create your forms here.


class NewUserForm(UserCreationForm):
  email = forms.EmailField(required=True)

  class Meta:
    model = User
    fields = ("username", "email", "password1", "password2" )


class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = '__all__'
		exclude = ['user']


