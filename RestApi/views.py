from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from RestApi.models import User
from RestApi.serializers import UserSerializer

@api_view(['GET'])
def accounts_list(request, format=None):
    if request.method == 'GET':
        accounts = User.objects.all()
        serializer = UserSerializer(accounts, many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def account_detail(request, pk, format=None):
    try:
        account = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(account)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
