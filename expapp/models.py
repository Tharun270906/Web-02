from django.db import models

# Create your models here.
class Student(models.Model):
    user=models.CharField(max_length=100,primary_key=100)
    password=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.ImageField(upload_to='profile/')
    addres=models.TextField()
