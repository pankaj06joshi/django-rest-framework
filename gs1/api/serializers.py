from rest_framework import serializers
from .models import Student

# validators (priority : 1)
def starts_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError('Name should be starts with \'r\' letter.')

# ============================ Standard Serializer class ===================================
''' class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, min_length=3, validators=[starts_with_r])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)
    
    # This method is automatically invoked when is_valid() method is called during save(), this approach use when we validate one or two values. (Field level validation) (priority : 2)
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value
    
    # object level validation (priority : 3)
    def validate(self, data):
        nme = data.get('name')
        cty = data.get('city')
        if nme == 'pankaj':
            raise serializers.ValidationError('You cannot add this name.')
        if len(cty) < 3:
            raise serializers.ValidationError(f'City name should be greater then {3} characters.')
        return data

    # create data in students table
    def create(self, validate_data):
        return Student.objects.create(**validate_data)
    
    # Here instance: old data stored in data, validate_data: New Data from user for updation
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance '''
    
    
# ============================ Model Serializer ===================================
class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True) # this approach to validate one or two values
    class Meta:
        model = Student
        # fields = ['name', 'roll', 'city']  
        fields = '__all__' 
        # exclude = ['roll'] 
        # read_only_fields = ['name', 'roll']
        extra_kwargs = {'name': {'max_length': 100, 'min_length': 3, 'validators': [starts_with_r]}, 'city': {'min_length': 3}}
        
    # This method is automatically invoked when is_valid() method is called during save(), this approach use when we validate one or two values. (Field level validation) (priority : 2)
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value  
    
    # object level validation (priority : 3)
    def validate(self, data):
        nme = data.get('name')
        cty = data.get('city')
        if nme == 'pankaj':
            raise serializers.ValidationError('You cannot add this name.')
        if len(cty) < 3:
            raise serializers.ValidationError(f'City name should be greater then {3} characters.')
        return data  

        