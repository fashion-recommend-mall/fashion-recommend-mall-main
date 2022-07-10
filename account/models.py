from django.db import models
from django.contrib.auth.models import User as U

# Create your models here.


class UserDetail(models.Model):
    '''
    Title : UserDetail
    This is User table extends admin user in django
    Attributes:
        user (Djang admin User) : This is One To One Filed to connect user in django
    '''
    user = models.OneToOneField(U, on_delete=models.CASCADE)
    traditional = models.IntegerField(default=0)
    manish = models.IntegerField(default=0)
    feminine = models.IntegerField(default=0)
    ethnic = models.IntegerField(default=0)
    contemporary = models.IntegerField(default=0)
    natural = models.IntegerField(default=0)
    genderless = models.IntegerField(default=0)
    sporty = models.IntegerField(default=0)
    subculture = models.IntegerField(default=0)
    casual = models.IntegerField(default=0)