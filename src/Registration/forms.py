from django import forms
from .models import Student, Membership

class FormA(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['branch', 'sem', 'cont']

class Membership_form(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ['m_type']