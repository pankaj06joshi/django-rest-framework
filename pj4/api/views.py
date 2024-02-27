# ====================== Generic API View and Model Mixins =============================================

from .models import Student
from .serializers import StudentSerializer
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

   
# ========================== View Set =================================

class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response({'success': True, 'message': serializer.data}, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        if pk is None:
            return Response({'success': False, 'message': 'Student id is missing.'}, status=status.HTTP_404_NOT_FOUND)
        stu = Student.objects.get(pk=pk)
        serializer = StudentSerializer(stu)
        return Response({'success': True, 'message': serializer.data}, status=status.HTTP_200_OK)
    
    def create(self, request):
        try:
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid() is False:
                return Response({'success': False, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)    
            serializer.save()
            return Response({'success': True, 'message': 'Data added successfully.'}, status=status.HTTP_201_CREATED)
        except:
            return Response({'success': False, 'message': 'something went wrong CODE: STUC0X02'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    
        
    def update(self, request, pk):
        try:
            stu = Student.objects.get(id=pk)
            serializer = StudentSerializer(stu, data=request.data, partial=True)
            if serializer.is_valid() is False:
                return Response({'success': False, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)    
            serializer.save()
            return Response({'success': True, 'message': 'Data updated successfully.'})
        except:
            return Response({'success': False, 'message': 'something went wrong CODE: STUC0X03'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    
           
    def destroy(self, request, pk):
        try:
            stu = Student.objects.get(id=pk)
            stu.delete()
            return Response({'success': True, 'message': 'Data deleted successfully.'})
        except:
            return Response({'success': False, 'message': 'something went wrong CODE: STUC0X04'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    