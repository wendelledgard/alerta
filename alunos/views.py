from django.shortcuts import render
from .models import Aluno
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from . import conhecimento
import csv

def index(request):
    alunos_aprovados = Aluno.objects.all().filter(filtro=0)
    alunos_reprovados = Aluno.objects.all().filter(filtro=1)
    alunos_evadidos = Aluno.objects.all().filter(filtro=2)

    page = request.GET.get('page', 1)
    paginator = Paginator(alunos_aprovados, 50)

    try:
        alunos = paginator.page(page)
    except PageNotAnInteger:
        alunos = paginator.page(1)
    except EmptyPage:
        alunos = paginator.page(paginator.num_pages)

    context = {
        'aprovados': alunos,
        'reprovados': alunos_reprovados,
        'evadidos': alunos_evadidos
    }
    return render(request, 'alunos/index.html', context)

#Chamar este método para inserir os dados do csv no banco
def atualiza_dados():
    with open('alunos/TecnologiasNovo.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        next(csv_reader) #ignora a primeira linha com as labels
        for line in csv_reader:
            try:
                # (Media_Final, Faltas, Renda, CoefRendimento, Frequencia)
                results = conhecimento.verificarEstado(float(line[3]), float(line[2]), float(line[6]), float(line[10]), float(line[4]))
                if((results[0] > results[1]) and (results[0] > results[2])):
                    valor = 0
                elif((results[1] > results[0]) and (results[1] > results[2])):
                    valor = 1
                else:
                    valor = 2
                Aluno.objects.create(Matricula=line[0], Ano_letivo=line[1], Faltas=line[2], Media_Final=line[3], Frequencia=line[4], Sexo=line[5], Renda=line[6], Tipo_Escola_Origem=line[7], Etnia=line[8], Reside=line[9], CoefRendimento=line[10], AcessoBiblioteca=line[11], ETEP=line[12], Projeto=line[13], BolsaEstudo=line[14], Situacao=line[15], filtro=valor)
            except:
                pass
    alunos = Aluno.objects.all()
    return alunos