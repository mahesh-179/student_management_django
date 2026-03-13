from django.shortcuts import render,get_object_or_404
from .models import Student
# Create your views here.
def home(request):
    return render(request,"myapp/base.html")

def student_result(request):
    students = Student.objects.all()
    context = {
        'students':students
    }
    return render(request,"myapp/student_list.html",context)

def student_detail(request, chai_id):
    details = get_object_or_404(Student, pk=chai_id)
    return render(request,"myapp/student_details.html",{'details':details})
    