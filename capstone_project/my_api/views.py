from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User

from my_api import serializers
from my_api import models
from my_api.models import File


class TestJson(APIView):
    def get(self, request):
        an_list = [
            'this is a test for json response.',
            'do you get this message?',
            'I hope you do.'
        ]
        return Response({'type':'json', 'message':an_list})

class UserProfile(APIView):
    serializer_class = serializers.UserProfileSerializer

    def get(self, request):
        return Response({'message': 'This API end point is not implemented yet. Sorry.'})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username_input = serializer.validated_data.get('username')
            email_input = serializer.validated_data.get('email')
            password_input = serializer.validated_data.get('password')
            password_confirm_input = serializer.validated_data.get('password_confirm')
            if (password_input == password_confirm_input):
                if User.objects.filter(username = username_input).exists():
                    return Response({'message': 'Account creation fail'})
                elif User.objects.filter(email = email_input).exists():
                    return Response({'message': 'Account creation fail'})
                else:
                    newUser=User.objects.create_user(username = username_input, email = email_input, password = password_input)
                    newUser.save()
                    return Response({'message':'User creation successful'})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

class FileUpload(APIView):
    serializer_class = serializers.FileSerializer

    def get(self, request):
        return Response({'message':'This API end point is not implemented yet. Sorry.'})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            username_input = serializer.validated_data.get('username')
            filename_input = serializer.validated_data.get('filename')
            docfile_input = serializer.validated_data.get('docfile')
            newFile = File(username=username_input, filename=filename_input, docfile=docfile_input)
            newFile.save()
            return Response({'message':'File upload successful.'})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

# Create your views here.
def hello(request):
    text = """<h1>welcome to my app!</h1>"""
    return HttpResponse(text)

def morning(request, test):
    text = f"<h1>Good Morning! {test}</h1>"
    return HttpResponse(text)
