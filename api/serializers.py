from .models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
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
        fields = ['id', 'escola', 'name']
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
    # turma = TurmaSerializer(many=False)
    class Meta:
        model = Lotacao
        fields = ['id', 'turma', 'professor', 'disciplina', 'ano_letivo']
        depth = 1