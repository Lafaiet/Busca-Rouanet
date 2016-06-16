from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from serializers import CustomSerializer
from models import Projeto, Incentivador, Proponente, Doacao
from filters import ProjetoFilter
from django.http import HttpResponse



exclusion_fields = ['limit', 'offset', 'order', 'format', 'conclusao']

class ProjetoApiView(APIView):

    def get(self, request):

        query_params = request.META['QUERY_STRING'].split('&')

        icontain_fields = ['municipio', 'proponente', 'nome']
        filter_args = {}

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

        offset = int(request.GET.get('offset') or 0 )
        limit = int(request.GET.get('limit') or 100)+offset

        if 'incentivador' in filter_args:
            incentivador = Incentivador.objects.filter(cgccpf=filter_args['incentivador'])[0]

            projetos = incentivador.projetos.all()

        #projetos = ProjetoFilter(request.GET, queryset = Projeto.objects.values(*Projeto.basic_fields))
        else:
            projetos = Projeto.objects.filter(**filter_args).values(*Projeto.basic_fields)
        total = projetos.count()

        projetos = projetos[offset:limit]
        return Response({'rows' : list(projetos), 'total' : total})
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
        serialized = CustomSerializer(proponentes, total)
        #return Response(serializer.data)
        return HttpResponse(serialized.data, content_type='application/json; charset=utf-8')

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
        serialized = CustomSerializer(incentivadores, total)
        #return Response(serializer.data)
        return HttpResponse(serialized.data, content_type='application/json; charset=utf-8')

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
