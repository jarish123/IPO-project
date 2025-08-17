# views.py
from rest_framework import viewsets, filters
from .models import IPO
from .serializers import IPOSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import jwt
from django.conf import settings
from datetime import datetime, timedelta



@method_decorator(csrf_exempt, name='dispatch')
class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user:
            return Response({"message": "Login successful", "username": username})
        return Response({"error": "Invalid credentials"}, status=401)

class IPOViewSet(viewsets.ModelViewSet):
    queryset = IPO.objects.all().order_by('-open_date')
    serializer_class = IPOSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['company_name', 'status']
    ordering_fields = ['open_date', 'listing_date', 'ipo_price']
    ordering = ['-open_date']


class IpoListAPIView(APIView):
    def get(self, request):
        ipos = Ipo.objects.all()
        serializer = IpoSerializer(ipos, many=True)
        return Response(serializer.data)