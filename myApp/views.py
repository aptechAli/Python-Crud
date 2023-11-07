from django.shortcuts import render
from myApp.models import StudentAddmission

# Create your views here.


def Index(request):
    if request.method == 'POST':
        varuserEmail = request.POST.get('studentEmail')
        varuserName = request.POST.get('studentName')
        varuserCourse = request.POST.get('course')

        member = StudentAddmission(
            studentEmail=varuserEmail, studentName=varuserName, studentCourse=varuserCourse)
        member.save()
        # context = {
        #     "varuserEmail": varuserEmail,
        #     "varuserName": varuserName,
        #     "varuserCourse": varuserCourse,
        # }

        return render(request, 'admissionForm.html')
    else:
        return render(request, 'admissionForm.html', {"Error": "ni chal raha condition"})
