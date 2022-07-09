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