from django.shortcuts import render
from django.http import JsonResponse
blogs=[{
    'id':1,
    'title':'python',
    'description':'python is a high level progrramming language'
},
{ 'id':2,
    'title':'java',
    'description':'java is a based on oops and high level progrramming language'
}]

# Create your views here.
def createAndGetAllBlogs(request):
    if(request.method=='GET'):
        return JsonResponse({'blogs':blogs},safe=False)
    elif(request.method=='POST'):
        pass