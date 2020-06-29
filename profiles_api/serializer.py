from rest_framework import serializers

class HelloSerializer(serializer.Serializer):
    #Serializer is a name field for testing our APIView
    name = serializers.CharField(max_length=10)
