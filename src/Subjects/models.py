from django.db import models
from django.urls import reverse

# Create your models here.

class Subject(models.Model):
    s_name = models.CharField(max_length=100, blank=True, null=True)
    s_code = models.CharField(max_length=10, blank=True, null=True)
    dept = models.CharField(max_length=100, blank=True, null=True)
    descp = models.TextField(blank=True, null=True)
    prof = models.TextField(blank=True, null=True)
    elec = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('Subjects:detail-view', kwargs={'sub_id':self.id})