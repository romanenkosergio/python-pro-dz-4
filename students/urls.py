from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('generate-student', views.generate_student, name='generate_student'),
    path('generate-students', views.generate_students, name='generate_students'),
    path('all-students', views.get_all_students, name='get_all_students'),
]
