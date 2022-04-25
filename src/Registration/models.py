from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    branch = models.CharField(max_length=100, null=True)
    sem = models.IntegerField(null=True)
    cont = models.IntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.student)

class Membership(models.Model):
    TYPES = (('Gym', 'Gym'),
            ('Swimming', 'Swimming'),
            ('Both', 'Both'))
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    m_type = models.CharField(max_length=100, choices=TYPES)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.student)