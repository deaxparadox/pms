from html5lib import serialize
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

from api.helpers.auth import get_token_from_header

from ..serializers import HeadingModelSerializer
from ..serializers.single_heading import (
    heading_HeadingSerializer_single_task, 
    heading_TaskSerializer_single_task,
)
from app.models.headings import Heading

class GetSingleHeading(APIView):
    # filterset_fields = ['category', 'in_stock']

    def get(self, request, id):
        # id = self.kwargs['id']                                # for query parameter
        user_token = get_token_from_header(request)
        
        try:
            heading = user_token.user.heading.get(id=id)
        except Heading.DoesNotExist:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        
        serializers = heading_HeadingSerializer_single_task(heading)
        
        return Response(
            serializers.data,
            status=status.HTTP_200_OK
        )
        
        
@api_view(["POST"])
def create_heading(request):
    user_token: str | None = get_token_from_header(request)
    if not user_token:
        return Response({}, status=status.HTTP_401_UNAUTHORIZED)
    
    # get `heading` data from request
    heading = request.data.get("heading")
    
    # create new `Heading` object
    new_heading = user_token.user.heading.create(heading=heading)
    
    # serializer the heading
    serializer = HeadingModelSerializer(new_heading)
    
    # return a response
    return Response(serializer.data, status=status.HTTP_201_CREATED)