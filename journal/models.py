from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Thought(models.Model):

    title = models.CharField(max_length=150)
    content = models.CharField(max_length=400)
    date_posted = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, max_length=10, on_delete=models.CASCADE, null=True)



#As soon as we create a new user, we will automatically create a new profile object linked to the user by foreign key
class Profile(models.Model):

    profile_pic = models.ImageField(null=True, blank=True, default='Default.png') #null = True allows null value in database and blank = True allows us to have a null value in form
    
    user = models.ForeignKey(User, max_length=10, on_delete=models.CASCADE, null=True)





















