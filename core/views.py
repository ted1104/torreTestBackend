from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework import status


# Create your views here.


# Default route
class HomeView(APIView):
    def get(self, request):
        return Response({
            "status": status.HTTP_200_OK,
            "message": "Welcome to Torre Test APis"
        })
