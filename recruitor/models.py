from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Company(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=12)
    email=models.CharField(max_length=255)
    looking_for=models.CharField(max_length=12,null=True,blank=True)
    company_name = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.user.username
