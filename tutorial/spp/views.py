from django.shortcuts import render
from rest_framework.views import APIView
from .models import Books
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .serializers import listAuthorSerializer , AuthorSerializer
# Create your views here.


class ListAuthors(APIView):

    def get(self , request):
        queryset = Books.objects.all()
        serializer = listAuthorSerializer(queryset , many=True)
        return Response(serializer.data)


class ListByid(APIView):

    def get(self , request , pk):
        queryset = Books.objects.get(id=pk)
        serializer = listAuthorSerializer(queryset , many=False)
        return Response(serializer.data)

class ListAuthorsName(APIView):

    def get(self , request , auth_name):
        queryset = Books.objects.filter(author__name=auth_name)
        serializer = listAuthorSerializer(queryset , many=True)
        return Response(serializer.data)


class AddAuthor(APIView):

    def post(self , request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'messgae' : 'Author Added'})

