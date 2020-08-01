from django.db import models
from django.contrib.auth.models import User
# Create your models here.
''' 
    username
    password 
    first_name
    last_name
    email  
     '''

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15,null=True , blank=True)
    addres = models.CharField(max_length=50 , blank=True, null=True)
    # image
    # age
    # Job

    def __str__(self):
        return str(self.user)
