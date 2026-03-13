from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'rollno', 'gpa', 'final_grade','dob','joining_date')


admin.site.register(Student, StudentAdmin)
