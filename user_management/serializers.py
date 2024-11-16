from rest_framework.serializers import ModelSerializer
from .models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from datetime import timedelta

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        access = refresh.access_token
        # Agregar tiempo de expiración
        data['expiration'] = access.payload['exp']  #agregar swager 
        data["username"] = self.user.username
        return data


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