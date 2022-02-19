from django.shortcuts import render,redirect
from stuapp.models import Student
from stuapp.forms import StudentForm
# Create your views here.

def stu_details(request):
    stu_data=Student.objects.all()
    stu_dict={'stu_list':stu_data}
    return render(request,'stu.html',context=stu_dict)

def create_view(request):
    form=StudentForm()
    if request.method =='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/student')

    return render(request,'create.html',{'form':form})

def delete_view(request,id):
    student=Student.objects.get(id=id)
    student.delete() 
    return redirect('/student')

def update_view(request,id):
    student=Student.objects.get(id=id)
    if request.method =='POST':
        form=StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('/student')
    return render(request,'update.html',{'student':student})
    