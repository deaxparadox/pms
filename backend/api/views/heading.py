from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..serializers.single_heading import (
    heading_HeadingSerializer_single_task, 
    heading_TaskSerializer_single_task
)
from app.models.headings import Heading

class GetSingleHeading(APIView):
    # filterset_fields = ['category', 'in_stock']

    def get(self, request, id):
        # id = self.kwargs['id']                                        # for query parameter
        heading = Heading.objects.get(id=id)
        serializers = heading_HeadingSerializer_single_task(heading)
        print(serializers)
        return Response(
            serializers.data,
            status=status.HTTP_200_OK
        )