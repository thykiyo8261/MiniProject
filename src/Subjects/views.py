from django.shortcuts import render, get_object_or_404

from .forms import SubjectForm
from .models import Subject

# Create your views here.

def create_view(request):
    sub = SubjectForm(request.POST or None)
    if sub.is_valid():
        sub.save()
        sub = SubjectForm()
    context = {
        'obj': sub
    }
    return render(request, 'subject_create.html', context)

def detail_view(request, sub_id):
    sub = get_object_or_404(Subject, id=sub_id)
    context = {
        'obj': sub
    }
    return render(request, 'subject_detail.html', context)

def list_view(request):
    sub_list = Subject.objects.all()
    context={
        'obj_list': sub_list
    }
    return render(request, 'subject_list.html', context)

def menu_view(request):
    context = {}
    return render(request, 'subject_menu.html', context)