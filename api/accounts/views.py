from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import userProfile
from .serializers import userProfileSerializer

@csrf_exempt
@api_view(['GET', 'POST'])
def account_list(request):
    if request.method == 'GET':
        accounts = userProfile.objects.all()
        serializer = userProfileSerializer(accounts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = userProfileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def account_detail(request, id):
    try:
        user = userProfile.objects.get(id=id)
    except userProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = userProfileSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = userProfileSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
