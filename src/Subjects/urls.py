from django.urls import path
from Subjects.views import create_view, list_view, detail_view, menu_view

app_name = 'Subjects'

urlpatterns = [
    path('create/', create_view, name='create-view'),
    path('list/', list_view, name='list-view'),
    path('<int:sub_id>/', detail_view, name='detail-view'),
    path('', menu_view, name='menu-view')
]