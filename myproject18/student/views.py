from django.shortcuts import render, get_object_or_404,redirect
from .forms import StudentForms
from . models import Student

# Create your views here.
def student_create(request):
  form = StudentForms()
  if request.method == 'POST':
    form = StudentForms(request.POST)
    if form.is_valid():
      form.save()
      return render(request,'student/student_success.html')
    
  return render(request,'student/student_create.html',{'form':form})
    
def student_list(request):
  students = Student.objects.all()
  return render(request,'student/student_list.html',{'students':students})


def student_detail(request,id):
  student = get_object_or_404(Student, id=id)
  return render(request,'student/student_detail.html',{'student':student})


def student_edit(request, pk):
  student = get_object_or_404(Student,pk=pk)
  if request.method == 'POST':
    form = StudentForms(request.POST,instance=student)
    if form.is_valid():
      form.save()
    return redirect("student_list")
  else:
    form = StudentForms(instance=student)
    return render(request,"student/student_create.html",{'form':form})  
  


def student_delete(request,pk):
  student = get_object_or_404(Student,pk=pk)
  if request.method == 'POST':
    student.delete()
    return redirect('student_list')
  return render(request,'student/student_confirm_delete.html',{'student':student})

