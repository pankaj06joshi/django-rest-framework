# ====================== Generic API View and Model Mixins =============================================

from .models import Student
from .serializers import StudentSerializer

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView

# ================ OLD CODE Without group of mixin classes ===============================
'''
class StudentList(GenericAPIView, ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    # fetch all students
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
         
    
class StudentCreate(GenericAPIView, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    # fetch all students
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
                  
         
class StudentRetrive(GenericAPIView, RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    # fetch all students
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
                  
         
class StudentUpdate(GenericAPIView, UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    # fetch all students
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
         
         
class StudentDelete(GenericAPIView, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    # fetch all students
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
         
'''


# ========================== With group of mixin classes =================================
'''
class LCStudentAPI(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    # fetch all students
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    # create student
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
         
         
class CUDStudentAPI(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    # fetch single student
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    # update student
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    # delete student
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
'''             
   
   
# ========================== Concrete View Class =================================

# class StudentList(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
    
# class StudentCreate(CreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer   

class StudentLC(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer  
 
# class StudentRetrive(RetrieveAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer  
    
# class StudentUpdate(UpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer 
    
# class StudentRU(RetrieveUpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer  
    
# class StudentRD(RetrieveDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer        
    
# class StudentDestroy(DestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer     
     
class StudentRUD(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer  