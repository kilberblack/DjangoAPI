from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Asignatura, Asistencia, PerfilUsuario
from .serializers import UserSerializer,AsignaturaSerializer, AsistenciaSerializer
import logging

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET', 'POST'])
def account_list(request):
    if request.method == 'GET':
        accounts = User.objects.all()
        serializer = UserSerializer(accounts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET', 'PUT', 'DELETE'])
def account_detail(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#User Register
@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():

        user = serializer.save()

        token = Token.objects.create(user=user)

        print(user)
        return Response({'token':token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Set up logging
logger = logging.getLogger(__name__)
#User Login
@api_view(['POST'])
def login(request):
    # Log the incoming request data
    logger.debug(f"Login request data: {request.data}")

    # Validate that 'username' and 'password' are in the request data
    if 'username' not in request.data or 'password' not in request.data:
        return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

    user = get_object_or_404(User, username=request.data['username'])

    if not user.check_password(request.data['password']):
        return Response({"error": "Invalid password"}, status=status.HTTP_400_BAD_REQUEST)

    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)

    return Response({"token": token.key, "user": serializer.data}, status=status.HTTP_200_OK)

#User Profile
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    user = request.user
    return Response({"id": user.id, "username": user.username}, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def asignatura_list(request):
    if request.method == 'GET':
        asignaturas = Asignatura.objects.all()
        serializer = AsignaturaSerializer(asignaturas, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = AsignaturaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def asistencia_list(request, asignatura_id):
    asistencias = Asistencia.objects.filter(asignatura_id=asignatura_id)
    serializer = AsistenciaSerializer(asistencias, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def asistencia_por_usuario(request, usuario_id):
    try:
        perfil_usuario = PerfilUsuario.objects.get(user_id=usuario_id)
        asistencias = Asistencia.objects.filter(usuario=perfil_usuario)
        serializer = AsistenciaSerializer(asistencias, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except PerfilUsuario.DoesNotExist:
        return Response({"error": "No se encontraron asistencias para este usuario."}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def asignatura_por_usuario(request, usuario_id):
    try:
        perfil_usuario = PerfilUsuario.objects.get(user_id=usuario_id)
        asignaturas = perfil_usuario.asignaturas.all()
        serializer = AsignaturaSerializer(asignaturas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except PerfilUsuario.DoesNotExist:
        return Response({"error": "No se encontraron asignaturas para este usuario."}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def incrementar_asistencia(request, asignatura_id, usuario_id):
    try:
        perfil_usuario = PerfilUsuario.objects.get(user_id=usuario_id)
        asignatura = Asignatura.objects.get(id=asignatura_id)
        asistencia, created = Asistencia.objects.get_or_create(asignatura=asignatura, usuario=perfil_usuario)
        asistencia.contador += 1
        asistencia.save()
        return Response({'mensaje': 'Asistencia incrementada exitosamente', 'contador': asistencia.contador})
    except PerfilUsuario.DoesNotExist:
        return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    except Asignatura.DoesNotExist:
        return Response({'error': 'Asignatura no encontrada'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def crear_asignatura(request):
    serializer = AsignaturaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def asignar_asignatura_a_usuario(request, usuario_id, asignatura_id):
    try:
        perfil_usuario = PerfilUsuario.objects.get(user_id=usuario_id)
        asignatura = Asignatura.objects.get(id=asignatura_id)
        Asistencia.objects.create(usuario=perfil_usuario, asignatura=asignatura)
        return Response({'mensaje': 'Asignatura asignada exitosamente'}, status=status.HTTP_201_CREATED)
    except PerfilUsuario.DoesNotExist:
        return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    except Asignatura.DoesNotExist:
        return Response({'error': 'Asignatura no encontrada'}, status=status.HTTP_404_NOT_FOUND)