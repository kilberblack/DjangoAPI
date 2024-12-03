from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Asignatura, Asistencia, PerfilUsuario

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        PerfilUsuario.objects.create(user=user)
        return user

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise ValidationError("A user with that username already exists.")
        return value

class AsistenciaSerializer(serializers.ModelSerializer):
    asignatura = serializers.StringRelatedField()
    usuario = serializers.StringRelatedField(source='usuario.user.username')

    class Meta:
        model = Asistencia
        fields = ['id', 'asignatura', 'fecha_asistencia', 'usuario', 'contador']

class AsignaturaSerializer(serializers.ModelSerializer):
    asistencias = AsistenciaSerializer(many=True, read_only=True)

    class Meta:
        model = Asignatura
        fields = ['id', 'nombre', 'descripcion', 'asistencias']