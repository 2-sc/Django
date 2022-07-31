# example > views.py
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
# from django.shortcuts import render

# Create your views here.
# @: 데코레이터, 함수를 꾸미는 역할
@api_view(['GET']) # HelloAPI()가 GET 요청을 받을 수 있는 API다
def HelloAPI(request):
    return Response("hello world!")