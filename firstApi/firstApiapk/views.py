from django.shortcuts import render
from .models import Student
from .serializer import studentserializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse

# Make the functio for getting one data ino the json 

def student_detail(request, pk=None):
    if pk is not None:
        stu = Student.objects.get(id=pk)
        serializer = studentserializer(stu)
    else:
        stu = Student.objects.all()
        serializer = studentserializer(stu, many=True)

    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data,safe=False)
 