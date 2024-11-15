from rest_framework.serializers import ModelSerializer
from .models import CustomUser

class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','username','password','image',]
    
    def create(self,validated_data):
        user = CustomUser(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self,instance,validated_data):
        super().update(instance, validated_data)
        instance.set_password(validated_data['password'])
        instance.save()
        return instance