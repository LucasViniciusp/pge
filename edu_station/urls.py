"""edu_station URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from  api import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('escolas/', views.EscolaList.as_view()),
    path('escolas/<int:pk_escola>', views.EscolaDetail.as_view()),
    path('escolas/<int:pk_escola>/turmas', views.TurmaList.as_view()),
    path('escolas/<int:pk_escola>/turmas/<int:pk_turma>', views.TurmaDetail.as_view()),
    path('escolas/<int:pk_escola>/turmas/<int:pk_turma>/lotacoes', views.LotacaoList.as_view()),
    path('escolas/<int:pk_escola>/turmas/<int:pk_turma>/lotacoes/<int:pk_lotacao>', views.LotacaoDetail.as_view()),
    path('escolas/<int:pk_escola>/turmas/<int:pk_turma>/matriculas', views.MatriculaList.as_view()),
    path('escolas/<int:pk_escola>/turmas/<int:pk_turma>/matriculas/<int:pk_matricula>', views.MatriculaDetail.as_view()),

    path('diretores/', views.DiretorList.as_view()),
    path('diretores/<int:pk>', views.DiretorDetail.as_view(),name='diretor-detail'),

    path('alunos/', views.AlunoList.as_view()),
    path('alunos/<int:pk>', views.AlunoDetail.as_view()),

    path('professores/', views.ProfessorList.as_view()),
    path('professores/<int:pk>', views.ProfessorDetail.as_view()),

    path('disciplinas/', views.DisciplinaList.as_view()),
    path('disciplinas/<int:pk>', views.DisciplinaDetail.as_view()),

    path('anoletivo/', views.AnoLetivoList.as_view()),  
    path('anoletivo/<int:pk>', views.AnoLetivoDetail.as_view()),  

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]