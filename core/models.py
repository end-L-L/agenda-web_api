from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import AbstractUser, User
from django.conf import settings
from django.core.validators import MinValueValidator

class BearerTokenAuthentication(TokenAuthentication):
    keyword = u"Bearer"

class Profiles(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, default=None)
    identifier = models.CharField(max_length=255,null=True, blank=True)
    start_date = models.CharField(max_length=255,null=True, blank=True)
    end_date = models.CharField(max_length=255,null=True, blank=True)
    job = models.CharField(max_length=255,null=True, blank=True)
    update = models.DateTimeField(null=True, blank=True)
    creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return "Perfil de Usuario: "+ "Nombre: " +self.user.first_name+" Job: "+self.job