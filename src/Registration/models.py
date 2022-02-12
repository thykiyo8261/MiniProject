from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200, null=True)
    regno = models.IntegerField(null=True)
    branch = models.CharField(max_length=100, null=True)
    sem = models.IntegerField(null=True)
    cont = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

class Membership(models.Model):
    TYPES = (('Gym', 'Gym'),
            ('Swimming', 'Swimming'),
            ('Both', 'Both'))

    name = models.CharField(max_length=200, null=True)
    regno = models.IntegerField(null=True)
    branch = models.CharField(max_length=100, null=True)
    sem = models.IntegerField(null=True)
    cont = models.IntegerField(null=True)
    m_type = models.CharField(max_length=100, choices=TYPES)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)