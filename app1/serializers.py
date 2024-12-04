from rest_framework import serializers

from app1.models import Example


class Student_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Example
        fields = "__all__"



