from django.urls import path
from . import views

urlpatterns=[
    path('',views.index, name='template-index'),
    path('relative/',views.relative, name='template-relative'),
    path('other/',views.other, name='template-other'),
]
