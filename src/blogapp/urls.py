
from django.urls import path,include
from .views import *

urlpatterns = [
    path('/<int:pk>',GetUpdateDeleteBlog.as_view()),
    path('',CreateAndGetAllBlogs.as_view()),
    path('/self',GetUserBlogs.as_view())
]