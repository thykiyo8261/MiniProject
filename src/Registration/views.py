from django.shortcuts import render

from .forms import FormA, Membership_form

# Create your views here.

def formA_view(request):
    form = FormA(request.POST or None)
    if form.is_valid():
        form.save()
        form = FormA()
    context = {
        'obj': form
    }
    return render(request, 'formA.html', context)

def membership_view(request):
    form = Membership_form(request.POST or None)
    if form.is_valid():
        form.save()
        form = Membership_form()
    context = {
        'obj': form
    }
    return render(request, 'membership.html', context)
