from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import PersonSerializer
from .models import Person

# Create your views here.
class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()