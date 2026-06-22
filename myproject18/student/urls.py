from . import views
from django.urls import path

urlpatterns = [
    path('add/',views.student_create,name='student_create'),
    path('',views.student_list,name='student_list'),
    path('detail/<int:id>/',views.student_detail,name='student_detail'),
]
