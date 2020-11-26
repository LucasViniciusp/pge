from .models import *
from .serializers import *
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login

class DiretorList(APIView):

    def get(self, request, format=None):
        diretor = Diretor.objects.all()
        serializer = DiretorSerializer(diretor, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DiretorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DiretorDetail(APIView):

    def get_object(self, pk):
        try:
            return Diretor.objects.get(pk=pk)
        except Diretor.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):

        diretor = self.get_object(pk)
        serializer = DiretorSerializer(diretor)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        diretor = self.get_object(pk)
        serializer = DiretorSerializer(diretor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        diretor = self.get_object(pk)
        diretor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EscolaList(APIView):
    permission_classes = []

    def get(self, request, format=None):
        escola = Escola.objects.all()
        serializer = EscolaSerializer(escola, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EscolaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EscolaDetail(APIView):

    def get_object(self, pk_escola):
        try:
            return Escola.objects.get(pk=pk_escola)
        except Escola.DoesNotExist:
            raise Http404

    def get(self, request, pk_escola, format=None):
        context = {}
        
        context['request']: request
        escola = self.get_object(pk_escola)
        serializer = EscolaSerializer(escola, context=context)
        return Response(serializer.data)

    def put(self, request, pk_escola, format=None):
        escola = self.get_object(pk_escola)
        serializer = EscolaSerializer(escola, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk_escola, format=None):
        escola = self.get_object(pk_escola)
        escola.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TurmaList(APIView):

    def get(self, request, pk_escola, format=None):
        turma = Turma.objects.filter(escola=pk_escola)
        serializer = TurmaSerializer(turma, many=True)
        return Response(serializer.data)

    def post(self, request, pk_escola, format=None):
        serializer = TurmaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TurmaDetail(APIView):

    def get_object(self, pk_turma):
        try:
            return Turma.objects.get(pk=pk_turma)
        except Turma.DoesNotExist:
            raise Http404

    def get(self, request, pk_escola, pk_turma, format=None):
        turma = self.get_object(pk_turma)
        serializer = TurmaSerializer(turma)
        return Response(serializer.data)

    def put(self, request, pk_escola, pk_turma, format=None):
        turma = self.get_object(pk_turma)
        serializer = TurmaSerializer(turma, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk_escola, pk_turma, format=None):
        turma = self.get_object(pk_turma)
        turma.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LotacaoList(APIView):

    def get(self, request, pk_escola, pk_turma, format=None):
        lotacao = Lotacao.objects.filter(turma=pk_turma)
        serializer = LotacaoSerializer(lotacao, many=True)
        return Response(serializer.data)

    def post(self, request, pk_escola, pk_turma, format=None):
        serializer = LotacaoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LotacaoDetail(APIView):

    def get_object(self, pk_lotacao):
        try:
            return Lotacao.objects.get(pk=pk_lotacao)
        except Lotacao.DoesNotExist:
            raise Http404

    def get(self, request, pk_escola, pk_turma, pk_lotacao, format=None):
        lotacao = self.get_object(pk_lotacao)
        serializer = LotacaoSerializer(lotacao)
        return Response(serializer.data)

    def put(self, request, pk_escola, pk_turma, pk_lotacao, format=None):
        lotacao = self.get_object(pk_lotacao)
        serializer = LotacaoSerializer(lotacao, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk_escola, pk_turma, pk_lotacao, format=None):
        lotacao = self.get_object(pk_lotacao)
        lotacao.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MatriculaList(APIView):

    def get(self, request, pk_escola, pk_turma, format=None):
        matriculas = MatriculaAluno.objects.filter(turma=pk_turma)
        serializer = MatriculaAlunoSerializer(matriculas, many=True)
        return Response(serializer.data)

    def post(self, request, pk_escola, pk_turma, format=None):
        serializer = MatriculaAlunoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MatriculaDetail(APIView):

    def get_object(self, pk_matricula):
        try:
            return MatriculaAluno.objects.get(pk=pk_matricula)
        except MatriculaAluno.DoesNotExist:
            raise Http404

    def get(self, request, pk_escola, pk_turma, pk_matricula, format=None):
        matricula = self.get_object(pk_matricula)
        serializer = MatriculaAlunoSerializer(matricula)
        return Response(serializer.data)

    def put(self, request, pk_escola, pk_turma, pk_matricula, format=None):
        matricula = self.get_object(pk_matricula)
        serializer = MatriculaAlunoSerializer(matricula, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk_escola, pk_turma, pk_matricula, format=None):
        matricula = self.get_object(pk_matricula)
        matricula.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProfessorList(APIView):

    def get(self, request, format=None):
        professor = Professor.objects.all()
        serializer = ProfessorSerializer(professor, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProfessorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfessorDetail(APIView):

    def get_object(self, pk):
        try:
            return Professor.objects.get(pk=pk)
        except Professor.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        professor = self.get_object(pk)
        serializer = ProfessorSerializer(professor)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        professor = self.get_object(pk)
        serializer = ProfessorSerializer(professor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        professor = self.get_object(pk)
        professor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DisciplinaList(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        disciplina = Disciplina.objects.all()
        serializer = DisciplinaSerializer(disciplina, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DisciplinaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DisciplinaDetail(APIView):

    def get_object(self, pk):
        try:
            return Disciplina.objects.get(pk=pk)
        except Disciplina.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        disciplina = self.get_object(pk)
        serializer = DisciplinaSerializer(disciplina)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        disciplina = self.get_object(pk)
        serializer = DisciplinaSerializer(disciplina, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        disciplina = self.get_object(pk)
        disciplina.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AlunoList(APIView):

    def get(self, request, format=None):
        aluno = Aluno.objects.all()
        serializer = AlunoSerializer(aluno, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AlunoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class AlunoDetail(APIView):

    def get_object(self, pk):
        try:
            return Aluno.objects.get(pk=pk)
        except Aluno.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        aluno = self.get_object(pk)
        serializer = AlunoSerializer(aluno)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        aluno = self.get_object(pk)
        serializer = AlunoSerializer(aluno, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        aluno = self.get_object(pk)
        aluno.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AnoLetivoList(APIView):

    def get(self, request, format=None):
        anoletivo = AnoLetivo.objects.all()
        serializer = AnoLetivoSerializer(anoletivo, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AnoLetivoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnoLetivoDetail(APIView):

    def get_object(self, pk):
        try:
            return AnoLetivo.objects.get(pk=pk)
        except AnoLetivo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        anoletivo = self.get_object(pk)
        serializer = AnoLetivoSerializer(anoletivo)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        anoletivo = self.get_object(pk)
        serializer = AnoLetivoSerializer(anoletivo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        anoletivo = self.get_object(pk)
        anoletivo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)