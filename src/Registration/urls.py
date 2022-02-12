from django.urls import path

from Registration.views import formA_view, membership_view

urlpatterns = [
    path('formA/', formA_view, name='formA'),
    path('memberships/', membership_view, name='membership')
]

