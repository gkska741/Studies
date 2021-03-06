from django.core.exceptions import BadRequest
from django.http import response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer

from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny


@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):

    password = request.data.get('password')
    passowrd_confirmation = request.data.get('passwordConfirmation')

    if password != passowrd_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = UserSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        user = serializer.save()

        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    pass