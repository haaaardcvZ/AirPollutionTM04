from django.shortcuts import render
from rest_framework.views import APIView


def index(request):
    return render(request, 'index.html')

# # Create your views here.
# class MainView(APIView):
#     def get(self, request):
#         return Response({})