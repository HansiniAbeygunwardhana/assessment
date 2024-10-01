from django.shortcuts import render
from .serializer import RequestSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .permissions import IsReadOnly
from .seriali

# Create your views here.

class RequestAPIView(APIView):
    authentication_classes = []
    permission_classes = [IsAuthenticated, IsReadOnly]
    
    def post(self, request):
        serializer = RequestSerializer(data = request.data)
        if serializer.is_valid():
            return Response({"message":"Data is Valid", "data":serializer.validate_data}, status = status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)