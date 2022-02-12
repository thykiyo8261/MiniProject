from django import forms
from .models import Student, Membership

class FormA(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class Membership_form(forms.ModelForm):
    class Meta:
        model = Membership
        fields = '__all__'