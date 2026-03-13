from django.contrib import admin
from .models import Student, StudentProfile


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'rollno', 'gpa', 'final_grade')


class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('student', 'dob', 'joining_date')


admin.site.register(Student, StudentAdmin)
admin.site.register(StudentProfile, StudentProfileAdmin)