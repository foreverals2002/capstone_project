from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response


class TestJson(APIView):
    def get(self, request):
        an_list = [
            'this is a test for json response.',
            'do you get this message?',
            'I hope you do.'
        ]
        return Response({'type':'json', 'message':an_list})

# Create your views here.
def hello(request):
    text = """<h1>welcome to my app!</h1>"""
    return HttpResponse(text)

def morning(request, test):
    text = f"<h1>Good Morning! {test}</h1>"
    return HttpResponse(text)
