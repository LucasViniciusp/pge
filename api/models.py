from django.db import models


class Diretor(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Escola(models.Model):
    name = models.CharField(max_length=30, unique=True)
    diretor = models.OneToOneField(Diretor, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class AnoLetivo(models.Model):
    ano = models.IntegerField(unique=True)

    def __str__(self):
        str_ano = str(self.ano)
        return str_ano


class Turma(models.Model):
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Aluno(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class MatriculaAluno(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    ano_letivo = models.ForeignKey(AnoLetivo, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['aluno', 'ano_letivo'],
            name='Aluno não pode ter 2 matriculas no mesmo Ano Letivo')
        ]


    def __str__(self):
        return f'{self.aluno} - {self.turma} - {self.ano_letivo}'.format()


class Professor(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Disciplina(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Lotacao(models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    ano_letivo = models.ForeignKey(AnoLetivo, on_delete=models.CASCADE)


    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['turma', 'professor', 'disciplina', 'ano_letivo'],
            name='conjunto turma-professor-disciplina-ano unico por lotação')
        ]


    def __str__(self):
        return f'{self.turma} - {self.professor} - {self.disciplina} - {self.ano_letivo}'.format()