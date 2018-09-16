from django.db import models

# Create your models here.


# 用户表
class Users(models.Model):
    Username = models.CharField(max_length=24, primary_key=True)
    Password = models.CharField(max_length=16)
    Email = models.EmailField(max_length=36)

    def __str__(self):
        return self.Username

