
from django.urls import path , include
from .views import ListAuthors , ListByid , ListAuthorsName , AddAuthor


urlpatterns = [
    path('list/' , ListAuthors.as_view() , name='authors'),
     path('author/<int:pk>/' , ListByid.as_view() , name='list_id'),
     path('author/<str:auth_name>/' , ListAuthorsName.as_view() , name='list_name'),
     path('add/author/' , AddAuthor.as_view() , name='add_auth')
]
