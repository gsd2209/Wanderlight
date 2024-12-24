<<<<<<< HEAD
=======
from django.shortcuts import render
>>>>>>> 6472ae2acf6526a1fb1173eadcbb7c15ed4b071a
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EmailSerializer
<<<<<<< HEAD


class SendEmailView(APIView):
    def post(self, request):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.send_email()
            return Response(
                {"message": "Email sent successfully!"}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
=======


# Create your views here.
class SendEmailView(APIView):
    def post(self,request):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.send_email()
            return Response({'message':'Email sent succesfully'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
>>>>>>> 6472ae2acf6526a1fb1173eadcbb7c15ed4b071a
