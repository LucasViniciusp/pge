# Generated by Django 3.1.3 on 2020-11-25 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_user_password'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Diretor',
        ),
        migrations.RemoveConstraint(
            model_name='matriculaaluno',
            name='conjunto aluno-turma-ano unico por matricula',
        ),
        migrations.AddConstraint(
            model_name='matriculaaluno',
            constraint=models.UniqueConstraint(fields=('aluno', 'ano_letivo'), name='Aluno não pode ter 2 matriculas no mesmo Ano Letivo'),
        ),
    ]
