from django.shortcuts import render
from .models import Student
# Create your views here.

def student_list(request):
    students = Student.objects.all()
    return render(request, 'studentApp/student_list.html', {'students': students})

def student_detail(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request, 'studentApp/student_detail.html', {'student': student})
