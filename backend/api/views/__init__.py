from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics

from django.shortcuts import render


from app.models.headings import Heading
from app.models.tasks import Task
from ..serializers import (
    HeadingModelSerializer, 
    TaskModelSerializer,
    HeadingModelSerializers_2,
    TaskModel_Serializers_2
)
from ..serializers.single_heading import (
    heading_HeadingSerializer_single_task
)
from ..serializers.single_task import (
    task_TaskSerializers_single_task
)


@api_view(["GET"])
def home_view(request):
    """
    Send a response with all heading
    """
    match request.method:
        case "GET":
            headings = Heading.objects.all()
            serializers = HeadingModelSerializer(headings, many=True)
            return Response(
                serializers.data,
                status=status.HTTP_200_OK
            )

@api_view(["GET"])
def tasks_view(request):
    """
    Get all Tasks
    """
    match request.method:
        case "GET":
            tasks = Task.objects.all()
            serializers = TaskModelSerializer(tasks, many=True)
            print(serializers)
            return Response(
                serializers.data,
                status=status.HTTP_200_OK
            )


@api_view(["GET"])
def get_single_task(request, id):
    match request.method:
        case "GET":
            tasks = Task.objects.get(id=id)
            serializers = task_TaskSerializers_single_task(tasks)
            print(serializers)
            return Response(
                serializers.data,
                status=status.HTTP_200_OK
            )

# @api_view(["GET"])
# def get_single_heading(request, id):
#     match request.method:
#         case "GET":
#             heading = Heading.objects.get(id=id)
#             serializers = heading_HeadingSerializer_single_task(heading)
#             print(serializers)
#             return Response(
#                 serializers.data,
#                 status=status.HTTP_200_OK
#             )
