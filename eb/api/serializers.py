from rest_framework import serializers
from base.models import Mt613, Mt722, Mt723, sesion 

class St722(serializers.ModelSerializer):
    class Meta:
        model = Mt722
        fields = '__all__'

class St723(serializers.ModelSerializer):
    class Meta:
        model = Mt723
        fields = '__all__'
        
class St613(serializers.ModelSerializer):
    class Meta:
        model = Mt613
        fields = '__all__'
        
class Stsession(serializers.ModelSerializer):
    class Meta:
        model = sesion
        fields = '__all__'