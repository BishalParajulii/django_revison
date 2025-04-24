from rest_framework import serializers
from .models import Author , Books


class listAuthorSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()
    class Meta:
        model = Books
        fields = ['id'  ,'title' , 'author_name']

    def get_author_name(self , obj):
        if obj.author:
            return obj.author.name

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = 'name'
