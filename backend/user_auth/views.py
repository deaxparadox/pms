
        
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.conf import settings
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


from rest_framework.authentication import (
    TokenAuthentication,
    BasicAuthentication, 
    SessionAuthentication
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status

from api.helpers.auth import get_token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)




@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def authenticate_user(request, formt=None):
    print(request.user)
    content = {
        'user': str(request.user),  # `django.contrib.auth.User` instance.
        'auth': str(request.auth),  # None
    }
    return Response(content, status=status.HTTP_200_OK)


# ############## RETREIVE TOKEN FOR AUTHORIZED USER ####################
# # 
# def get_token(user: User | None):
#     """Return the Token
    
#     If token does not exist return 404

#     Returns:
#         Reponse: dictionary of user auth token
#     """
#     try:
#         token: Token = Token.objects.get(user=user)
#     except Token.DoesNotExist as e:
#         return Response({"message": "token not found"}, status=status.HTTP_404_NOT_FOUND)
#     except Token.MultipleObjectsReturned as e:
#         return Response({"message": "multiple object found"}, status=status.HTTP_404_NOT_FOUND)
#     return Response({"token": token.key}, status=status.HTTP_200_OK)



############## CREATE USER ####################
# 
@api_view(["POST"])
@permission_classes([AllowAny])
def create_user(request):
    """
    CREATE USER VIEW:

    1. take from `username` and `password` from api.
    2. create user 
    3. generate user token
    4. return token
    """
    username = request.data.get("username")
    password = request.data.get("password")
    print(username, password)
    
    
    
    # create user
    try:
        user = User.objects.create_user(username=username, password=password)
    except User.DoesNotExist as e:
        print(e)
        return Response({}, status=status.HTTP_404_NOT_FOUND)
    except User.MultipleObjectsReturned as e:
        print(e)
        return Response({}, status=status.HTTP_404_NOT_FOUND)
    except IntegrityError as e:
        return Response({"message": "user already exists"}, status=status.HTTP_406_NOT_ACCEPTABLE)
    
    return get_token(user)



############## LOGIN USER ####################
# 
@api_view(["POST"])
@permission_classes([AllowAny])
def login_user(request):
    """
    LOGIN USER VIEW:

    1. take from `username` and `password` from api.
    2. check if user exiss
    3. get user token
    4. return token
    """
    username = request.data.get("username")
    password = request.data.get("password")
    
    
    try:
        user = User.objects.get(username=username)
        if user.check_password(password):
            return get_token(user)
    except User.DoesNotExist as e:
        return Response({}, status=status.HTTP_404_NOT_FOUND)
    except User.MultipleObjectsReturned as e:
        return Response({}, status=status.HTTP_404_NOT_FOUND)
    return Response({}, status=status.HTTP_404_NOT_FOUND)

