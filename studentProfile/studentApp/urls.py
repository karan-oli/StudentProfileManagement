from django.urls import path
from . import views

urlpatterns = [
    path('', views.class_list, name='class_list'),
    path('class/<int:class_id>/', views.student_list, name='student_list'),
    path('student/<int:pk>/', views.student_detail, name='student_detail'),
    path('generate_grade_sheet/<int:student_id>/', views.generate_grade_sheet, name='generate_grade_sheet'),
    path('add_all_subjects/<int:student_id>/', views.add_all_subjects_to_student, name='add_all_subjects'),
]
