from django.http import HttpResponse
from django.shortcuts import render

from .models import Student
from .services import generate_student_service


def home(request):
    """Home page."""
    return render(request, 'home.html', {'title': 'Home'})


def generate_student(request):
    """Generate a student."""
    students = generate_student_service()
    return render(request, 'generate_student.html', {'students': students, 'title': 'Generate Student'})


def generate_students(request):
    """Generate students based on the count parameter."""
    count = request.GET.get('count')
    if not count:
        return HttpResponse('Please provide a count parameter')
    students = generate_student_service(count)
    if isinstance(students, ValueError):
        return HttpResponse(students)
    return render(request, 'generate_student.html', {'students': students, 'title': 'Generate Students'})


def get_all_students(request):
    """Get all students."""
    students = Student.objects.all().values()
    return render(request, 'generate_student.html', {'students': students, 'title': 'All Students'})
