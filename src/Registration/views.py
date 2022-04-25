from django.shortcuts import render

from .forms import FormA, Membership_form
from .models import Student

# Create your views here.

def formA_view(request):
    if request.user.is_authenticated:
        form = FormA(request.POST or None)
        if form.is_valid():
            ins = form.save()
            ins.student = request.user
            ins.save()
            form = FormA()
        context = {
            'obj': form
        }
        return render(request, 'formA.html', context)

def membership_view(request):
    if request.user.is_authenticated:
        form = Membership_form(request.POST or None)
        if form.is_valid():
            std = Student.objects.get(student=request.user)
            ins = form.save()
            ins.student = std
            ins.save()
            form = Membership_form()
        context = {
            'obj': form
        }
        return render(request, 'membership.html', context)
