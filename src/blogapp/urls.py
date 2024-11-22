
from django.urls import path,include
from .views import *

urlpatterns = [
    path('/<int:id>',GetUpdateDeleteBlog.as_view()),
    path('',CreateAndGetAllBlogs.as_view())
]