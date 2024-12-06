from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EmailSerializer


# Create your views here.
class SendEmailView(APIView):
    def post(self,request):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.send_email()
            return Response({'message':'Email sent succesfully'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
