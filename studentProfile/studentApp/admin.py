<<<<<<< HEAD
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import admin
from .models import Student, Class, Subject, StudentSubject
from .forms import ClassSelectionForm

class StudentSubjectInline(admin.TabularInline):
    model = StudentSubject
    extra = 1

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'student_class', 'photo', 'grade_sheet']
    inlines = [StudentSubjectInline]
    # change_list_template = 'admin/student_change_list.html'

    def get_actions(self, request):
        actions = super().get_actions(request)
        if request.user.has_perm('studentApp.can_assign_subjects'):
            actions['assign_subjects_to_students'] = (
                self.assign_subjects_to_students,
                'assign_subjects_to_students',
                'Assign subjects to students'
            )
        return actions

    def assign_subjects_to_students(self, request, queryset):
        if 'apply' in request.POST:
            form = ClassSelectionForm(request.POST)
            if form.is_valid():
                selected_class = form.cleaned_data['selected_class']
                students = queryset
                subjects = Subject.objects.filter(student_class=selected_class)
                for student in students:
                    for subject in subjects:
                        if not StudentSubject.objects.filter(student=student, subject=subject).exists():
                            StudentSubject.objects.create(
                                student=student,
                                subject=subject,
                                full_marks=0,
                                obtained_marks=0
                            )
                self.message_user(request, "Subjects assigned to selected students successfully.")
                return HttpResponseRedirect(reverse('admin:studentApp_student_changelist'))
        else:
            form = ClassSelectionForm()

        context = {
            'form': form,
            'opts': self.model._meta,
            'title': 'Assign Subjects to Students'
        }
        return render(request, 'admin/assign_subjects.html', context)

    assign_subjects_to_students.short_description = "Assign subjects to selected students"

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'student_class']

@admin.register(StudentSubject)
class StudentSubjectAdmin(admin.ModelAdmin):
    list_display = ['student', 'subject', 'full_marks', 'obtained_marks']
    list_filter = ['subject']
    search_fields = ['student__name', 'subject__name']
=======
from django.contrib import admin
from .models import Student
# Register your models here.


admin.site.register(Student)
>>>>>>> origin/master
