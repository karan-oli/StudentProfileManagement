<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404,redirect
from .models import Student, Class, StudentSubject

def class_list(request):
    classes = Class.objects.all()
    return render(request, 'studentApp/class_list.html', {'classes': classes})

def student_list(request, class_id):
    students = Student.objects.filter(student_class_id=class_id)
    return render(request, 'studentApp/student_list.html', {'students': students})

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'studentApp/student_detail.html', {'student': student})

def generate_grade_sheet(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student_subjects = StudentSubject.objects.filter(student=student)

    # Calculate GPA
    total_marks = sum(ss.full_marks for ss in student_subjects)
    total_obtained = sum(ss.obtained_marks for ss in student_subjects)
    gpa = (total_obtained / total_marks) * 4.0 if total_marks > 0 else 0

    context = {
        'student': student,
        'student_subjects': student_subjects,
        'gpa': gpa,
    }

    return render(request, 'studentApp/grade_sheet.html', context)
def add_all_subjects_to_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    subjects = Subject.objects.filter(student_class=student.student_class)
    
    # Create StudentSubject entries for each subject
    for subject in subjects:
        StudentSubject.objects.get_or_create(
            student=student,
            subject=subject,
            defaults={'full_marks': 0, 'obtained_marks': 0}  # Default values if needed
        )
    
    return redirect('student_detail', pk=student_id)
=======
from django.shortcuts import render
from .models import Student
# Create your views here.

def student_list(request):
    students = Student.objects.all()
    return render(request, 'studentApp/student_list.html', {'students': students})

def student_detail(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request, 'studentApp/student_detail.html', {'student': student})
>>>>>>> origin/master
