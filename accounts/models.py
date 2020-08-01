from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
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


@receiver(post_save , sender=User)
def create_user_profile(sender,instance,created , **kwargs):
    if created:
        Profile.objects.create(
            user = instance
        )
