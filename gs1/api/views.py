from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import io

@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return JsonResponse({'success': True, 'message': serializer.data}, safe=False)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return JsonResponse({'success': True, 'message': serializer.data}, safe=False)
    
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'success': True, 'message': 'Data created.' })
        return JsonResponse({'success': False, 'message': serializer.errors })
    
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=python_data, partial=True) # partial: True(partial data update)/Fasle(full data update means all fields are required)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'success': True, 'message': 'Data is updated.' })
        return JsonResponse({'success': False, 'message': serializer.errors })

    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')

        stu = Student.objects.get(id=id)
        stu.delete()
        serializer = StudentSerializer(stu, data=python_data, partial=True) # partial: True(partial data update)/Fasle
        return JsonResponse({'success': True, 'message': 'Data is deleted.' })
        





        
# Model Object - one data
def student_detail(request, pk):
    stu = Student.objects.get(id=pk)
    serializer = StudentSerializer(stu)
    
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type="application/json")
    return JsonResponse(serializer.data)

# Query Set - student list
def student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type="application/json")
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythonData = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythonData)
        if serializer.is_valid():
            serializer.save()
            res = {'success': True, 'message': 'Data created.' }
            # json_data = JSONRenderer().render(res)
            # return HttpResponse(json_data, content_type='application/json')
            return JsonResponse(res)
        # json_data = JSONRenderer().render(serializer.errors)
        # return HttpResponse(json_data, content_type='application/json')
        return JsonResponse(serializer.errors)