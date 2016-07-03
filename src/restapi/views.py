from django.shortcuts import render
from django.db.models.functions import Coalesce
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from serializers import CustomSerializer
from models import Projeto, Incentivador, Proponente, Doacao
from filters import ProjetoFilter
from django.http import HttpResponse


exclusion_fields = ['limit', 'offset', 'order', 'format', 'conclusao', 'sort']

class ProjetoApiView(APIView):

    def get(self, request):

        query_params = request.META['QUERY_STRING'].split('&')

        icontain_fields = ['municipio', 'proponente', 'nome']
        filter_args = {}
        order_by = ['ano_projeto', 'PRONAC']
        order_desc = True

        for param in query_params:
            if param != '':
                k, v = param.split('=')
                if k not in exclusion_fields:
                    if k in icontain_fields:
                        k+='__icontains'
                    elif k == 'captacao':
                        if v == 'comcaptacoes':
                            k='valor_captado__gt'
                        else:
                            k='valor_captado'
                        v = 0
                    filter_args[k] = v
                elif k == 'sort':
                     order_by[0] = v
                elif k == 'order' and v == 'asc':
                    order_desc = False


        offset = int(request.GET.get('offset') or 0 )
        limit = int(request.GET.get('limit') or 100)+offset

        if 'incentivador' in filter_args:
            incentivador = Incentivador.objects.filter(cgccpf=filter_args['incentivador'])[0]

            #projetos = incentivador.projetos.all().order_by(order_by)
            projetos = incentivador.projetos.all()

        #projetos = ProjetoFilter(request.GET, queryset = Projeto.objects.values(*Projeto.basic_fields))
        else:
            projetos = Projeto.objects.filter(**filter_args).values(*Projeto.basic_fields)

        total = projetos.count()


        if order_desc:
            projetos = projetos.order_by(Coalesce(*order_by).desc())
        else:
            projetos = projetos.order_by(*order_by)


        projetos = projetos[offset:limit]

        projetos_serialized = CustomSerializer(projetos)

        return Response({'rows' : projetos_serialized.data, 'total' : total})
        #serialized = CustomSerializer(projetos, total)
        #return HttpResponse(serialized.data, content_type='application/json; charset=utf-8')

class ProponenteApiView(APIView):

    def get(self, request):

        query_params = request.META['QUERY_STRING'].split('&')

        icontain_fields = ['municipio', 'nome']
        filter_args = {}

        for param in query_params:
            if param != '':
                k, v = param.split('=')
                if k not in exclusion_fields:
                    if k in icontain_fields:
                        k+='__icontains'
                    filter_args[k] = v

        offset = int(request.GET.get('offset') or 0 )
        limit = int(request.GET.get('limit') or 100)+offset

        proponentes = Proponente.objects.filter(**filter_args).values(*Proponente.basic_fields)
        total = proponentes.count()
        proponentes = proponentes[offset:limit]
        proponentes_serialized = CustomSerializer(proponentes)

        return Response({'rows' : proponentes_serialized.data, 'total' : total})

class IncentivadorApiView(APIView):

    def get(self, request):

        query_params = request.META['QUERY_STRING'].split('&')

        icontain_fields = ['municipio', 'nome']
        filter_args = {}

        for param in query_params:
            if param != '':
                k, v = param.split('=')
                if k not in exclusion_fields:
                    if k in icontain_fields:
                        k+='__icontains'
                    filter_args[k] = v

        offset = int(request.GET.get('offset') or 0 )
        limit = int(request.GET.get('limit') or 100)+offset

        incentivadores = Incentivador.objects.filter(**filter_args).values(*Incentivador.basic_fields)
        total = incentivadores.count()
        incentivadores = incentivadores[offset:limit]
        incentivadores_serialized = CustomSerializer(incentivadores)

        return Response({'rows' : incentivadores_serialized.data, 'total' : total})

class DoacaoApiView(APIView):

    def get(self, request):

        query_params = request.META['QUERY_STRING'].split('&')

        icontain_fields = ['proponente', 'nome']
        filter_args = {}

        for param in query_params:
            if param != '':
                k, v = param.split('=')
                if k not in exclusion_fields:
                    if k in icontain_fields:
                        k+='__icontains'
                    filter_args[k] = v

        offset = int(request.GET.get('offset') or 0 )
        limit = int(request.GET.get('limit') or 100)+offset

        doacoes = Doacao.objects.filter(**filter_args).values(*Doacao.basic_fields)
        total = doacoes.count()
        doacoes = doacoes[offset:limit]
        return Response({'rows' : list(doacoes), 'total' : total})
