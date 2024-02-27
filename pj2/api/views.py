from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status

# ================================== Function Based API View ===================================

# @api_view() # By default GET method
'''@api_view(['GET', 'POST', 'PUT', 'DELETE']) 
def student_api(request, pk=None):
    if request.method == 'GET':
        try:
            if pk is None:
                stu = Student.objects.all()
                serializer = StudentSerializer(stu, many=True)
                return Response({'success': True, 'message': serializer.data})
            stu = Student.objects.get(id=pk)
            serializer = StudentSerializer(stu)
            return Response({'success': True, 'message': serializer.data})
        except:
            return Response({'success': False, 'message': 'something went wrong CODE: STUC0X01'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    if request.method == 'POST':
        try:
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid() is False:
                return Response({'success': False, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)    
            serializer.save()
            return Response({'success': True, 'message': 'Data added successfully.'}, status=status.HTTP_201_CREATED)
        except:
            return Response({'success': False, 'message': 'something went wrong CODE: STUC0X02'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    if request.method == 'PUT':
        try:
            id = request.data.get('id')
            stu = Student.objects.get(pk=id)
            serializer = StudentSerializer(stu, data=request.data, partial=True)
            if serializer.is_valid() is False:
                return Response({'success': False, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)    
            serializer.save()
            return Response({'success': True, 'message': 'Data updated successfully.'})
        except:
            return Response({'success': False, 'message': 'something went wrong CODE: STUC0X03'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    if request.method == 'DELETE':
        try:
            stu = Student.objects.get(id=pk)
            stu.delete()
            return Response({'success': True, 'message': 'Data deleted successfully.'})
        except:
            return Response({'success': False, 'message': 'something went wrong CODE: STUC0X04'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)'''
        

# ================================== Class Based API View ===================================
class StudentAPI(APIView):
    def get(self, request, format=None, pk = None):
        try:
            if pk is None:
                stu = Student.objects.all()
                serializer = StudentSerializer(stu, many=True)
                return Response({'success': True, 'message': serializer.data})
            stu = Student.objects.get(id=pk)
            serializer = StudentSerializer(stu)
            return Response({'success': True, 'message': serializer.data})
        except:
            return Response({'success': False, 'message': 'something went wrong CODE: STUC0X01'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def post(self, request, format=None):
        try:
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid() is False:
                return Response({'success': False, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)    
            serializer.save()
            return Response({'success': True, 'message': 'Data added successfully.'}, status=status.HTTP_201_CREATED)
        except:
            return Response({'success': False, 'message': 'something went wrong CODE: STUC0X02'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    
            
    def put(self, request, pk, format=None):
        try:
            stu = Student.objects.get(id=pk)
            serializer = StudentSerializer(stu, data=request.data, partial=True)
            if serializer.is_valid() is False:
                return Response({'success': False, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)    
            serializer.save()
            return Response({'success': True, 'message': 'Data updated successfully.'})
        except:
            return Response({'success': False, 'message': 'something went wrong CODE: STUC0X03'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    
           
    def delete(self, request, pk, format=None):
        try:
            stu = Student.objects.get(id=pk)
            stu.delete()
            return Response({'success': True, 'message': 'Data deleted successfully.'})
        except:
            return Response({'success': False, 'message': 'something went wrong CODE: STUC0X04'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    
        
        
    

















        