from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Example
from .serializers import Student_Serializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin


@api_view(["GET"])
def home(request):
    return Response("hiii")


@api_view(["GET"])
def home1(request):
    ex = Example.objects.all()
    serializer = Student_Serializer(ex, many=True)
    return Response({"pay": serializer.data})


@api_view(["POST"])
def home2(request):
    # Create a new instance of Example using the data from the request
    serializer = Student_Serializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Data added successfully", "data": serializer.data}, status=201)
    else:
        return Response({"error": serializer.errors}, status=400)


@api_view(["POST"])
def home3(request, id):
    ex1 = Example.objects.get(id=id)
    serializer = Student_Serializer(ex1, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response("UPDATED")


@api_view(["DELETE"])
def home4(request, id):
    ex1 = Example.objects.get(id=id)
    ex1.delete()
    return Response("DELETED")


class Studentlist(GenericAPIView, ListModelMixin):
    queryset = Example.objects.all()
    serializer_class = Student_Serializer 

    def get(self, request):
        return self.list(request)


class Studentlist_add(GenericAPIView, CreateModelMixin):
    queryset = Example.objects.all()
    serializer_class = Student_Serializer

    def post(self, request):
        return self.create(request)


class Studentlist_display(GenericAPIView, RetrieveModelMixin):
    queryset = Example.objects.all()
    serializer_class = Student_Serializer

    def get(self, request, **kwargs):
        return self.retrieve(request, **kwargs)


class Studentlist_destroy(GenericAPIView, DestroyModelMixin):
    queryset = Example.objects.all()
    serializer_class = Student_Serializer

    def delete(self, request, **kwargs):
        return self.destroy( request, **kwargs)


