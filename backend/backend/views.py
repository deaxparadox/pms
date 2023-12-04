from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def api_error_view(request):
    return Response({}, status=status.HTTP_404_NOT_FOUND)

def error_404(request):
    return render(
        request, 
        "404.html"
    )