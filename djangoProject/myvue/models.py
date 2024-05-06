from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meda:
        db_table = 'User'
