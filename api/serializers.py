from .models import *
from rest_framework import serializers
from rest_framework.reverse import reverse
from django.contrib.auth.models import User

class DiretorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diretor
        fields = ['id', 'name']


class EscolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escola
        fields = ['id', 'name', 'diretor']
        depth = 1


class AnoLetivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnoLetivo
        fields = ['id', 'ano']


class TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = ['id' ,'name', 'escola']
        depth = 1


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'name']


class MatriculaAlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatriculaAluno
        fields = ['id', 'aluno', 'turma', 'ano_letivo']
        depth = 1


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ['id', 'name']


class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = ['id', 'name']


class LotacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lotacao
        fields = ['id', 'turma', 'professor', 'disciplina', 'ano_letivo']
        depth = 1


class LoginSerializer(serializers.ModelSerializer):
    fields = ['username', 'password']

class TokenSerializer(serializers.ModelSerializer):
    fields = ['access', 'refresh']