from django.shortcuts import render
from enroll.models import Students
# Create your views here.


def studentInfo(request):
    stud = Students.objects.all()
    print('sstude --> ', stud)
    return render(request, 'enroll/studentdata.html', {'stu': stud})
