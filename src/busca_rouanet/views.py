# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseNotFound, HttpResponse
from django.template import RequestContext
from django.core import serializers
from models import Projeto, Proponente, Incentivador
from forms import ProjetoForm, ContactForm, ProponenteForm, IncentivadorForm
import requests
from datetime import datetime
from django.conf import settings
from api_handler import get_item
from django.core.mail import send_mail
from django.utils.encoding import uri_to_iri
from django.conf import settings
from boottable import ProjetoTable, IncentivadorTable, ProponenteTable, DoacaoTable, CaptacaoTable
import json
import simplejson




def projetosSearch(request):

    filter_args = {}
    link_args = u''
    form_initial = {}

    if request.method == 'POST':

        if  'submit' in request.POST:

            projeto = ProjetoForm(request.POST)

            if len(projeto.data['PRONAC']) > 0:
                filter_args['PRONAC'] = projeto.data['PRONAC']

            if len(projeto.data['cgccpf']) > 0:
                filter_args['cgccpf'] = projeto.data['cgccpf']

            if projeto.data['segmento'] != 'SEGMENTO':
                filter_args['segmento'] = projeto.data['segmento']

            if projeto.data['area'] != 'AREA':
                filter_args['area'] = projeto.data['area']

            if projeto.data['UF'] != 'ESTADO':
                filter_args['UF'] = projeto.data['UF']

            if projeto.data['ano_projeto'] != 'ano_projeto':
                filter_args['ano_projeto'] = projeto.data['ano_projeto']

            for key in filter_args:
                link_args += key+"="+filter_args[key]+"&"

            form_initial = filter_args.copy()

            if len(projeto.data['municipio']) > 0:
                filter_args['municipio__icontains'] = projeto.data['municipio']
                link_args +='municipio='+projeto.data['municipio']+'&'
                form_initial['municipio'] = projeto.data['municipio']

            if len(projeto.data['nome']) > 0:
                filter_args['nome__icontains'] = projeto.data['nome']
                link_args +='nome='+projeto.data['nome']+'&'
                form_initial['nome'] = projeto.data['nome']

            if len(projeto.data['proponente']) > 0:
                filter_args['proponente__icontains'] = projeto.data['proponente']
                link_args +='proponente='+projeto.data['proponente']+'&'
                form_initial['proponente'] = projeto.data['proponente']


            if projeto.data['captacao'] != 'captacao':
                form_initial['captacao'] = projeto.data['captacao']

                if form_initial['captacao'] == 'comcaptacoes':
                    filter_args['valor_captado__gt'] = 0
                else:
                    filter_args['valor_captado'] = 0

                link_args+="captacao="+projeto.data['captacao']+"&"

            if projeto.data['conclusao'] != 'conclusao':
                form_initial['conclusao'] = projeto.data['conclusao']
                link_args+="conclusao="+projeto.data['conclusao']+"&"

            #print "link args : " + link_args

    if request.method == 'GET':
        query_params = request.META['QUERY_STRING'].split('&')
        #   print 'Query params : ' + str(query_params)

        exclusion_fields = ['format', 'page', 'sort', 'captacao', 'conclusao', 'limit', 'offset', 'order']
        for param in query_params:
            if param != '':
                k, v = param.split('=')
                form_initial[k] = uri_to_iri(v)
                if k not in exclusion_fields:
                    filter_args[k] = v

        #print 'filter_args : ' + str(filter_args)

    table = ProjetoTable()
    table.data_url+=link_args

    return render(request, 'projetos.html', {'table' : table, 'searchForm' : ProjetoForm(initial=form_initial)})


def proponenteView(request):

    filter_args = {}
    link_args = u''
    form_initial = {}

    if request.method == 'POST':
        proponente = ProponenteForm(request.POST)

        if len(proponente.data['cgccpf']) > 0:
            filter_args['cgccpf'] = proponente.data['cgccpf']

        if len(proponente.data['nome']) > 0:
            filter_args['nome'] = proponente.data['nome']


        if proponente.data['tipo_pessoa'] != 'tipodepessoa':
            filter_args['tipo_pessoa'] = proponente.data['tipo_pessoa']

        if proponente.data['UF'] != 'ESTADO':
            filter_args['UF'] = proponente.data['UF']

        if len(proponente.data['municipio']) > 0:
            filter_args['municipio'] = proponente.data['municipio']

        form_initial = filter_args.copy()

        for key in filter_args:
            link_args += key+"="+filter_args[key]+"&"

    if request.method == 'GET':
        query_params = request.META['QUERY_STRING'].split('&')
        #   print 'Query params : ' + str(query_params)

        for param in query_params:
            if param != '':
                k, v = param.split('=')
                form_initial[k] = uri_to_iri(v)
                if k != 'page'  and k != 'sort' and k != 'captacao'  and k != 'conclusao':
                    filter_args[k] = v

        #print 'filter_args : ' + str(filter_args)

    table = ProponenteTable()
    table.data_url+=link_args

    return render(request, 'proponente.html', {'table' : table, 'searchForm' : ProponenteForm(form_initial)})

def proponenteDetail(request, cgccpf):

    table = ProjetoTable()
    table.data_url+='cgccpf='+str(cgccpf)

    proponente = Proponente.objects.filter(cgccpf=cgccpf)[0]

    return render(request, 'proponenteDetail.html', {"proponente" : proponente, 'table' : table})

def incentivadorView(request):

    filter_args = {}
    link_args = u''
    form_initial = {}

    if request.method == 'POST':
        incentivador = IncentivadorForm(request.POST)

        if len(incentivador.data['cgccpf']) > 0:
            filter_args['cgccpf'] = incentivador.data['cgccpf']

        if len(incentivador.data['nome']) > 0:
            filter_args['nome'] = incentivador.data['nome']


        if incentivador.data['tipo_pessoa'] != 'tipodepessoa':
            filter_args['tipo_pessoa'] = incentivador.data['tipo_pessoa']

        if incentivador.data['UF'] != 'ESTADO':
            filter_args['UF'] = incentivador.data['UF']

        if len(incentivador.data['municipio']) > 0:
            filter_args['municipio'] = incentivador.data['municipio']

        form_initial = filter_args.copy()

        for key in filter_args:
            link_args += key+"="+filter_args[key]+"&"


    if request.method == 'GET':
        query_params = request.META['QUERY_STRING'].split('&')
        #   print 'Query params : ' + str(query_params)

        for param in query_params:
            if param != '':
                k, v = param.split('=')
                form_initial[k] = uri_to_iri(v)
                if k != 'page'  and k != 'sort' and k != 'captacao'  and k != 'conclusao':
                    filter_args[k] = v

    table = IncentivadorTable()
    table.data_url+=link_args

    return render(request, 'incentivador.html', {'table' : table, 'searchForm' : IncentivadorForm(form_initial)})


def incentivadorDetail(request, cgccpf):

    incentivador = Incentivador.objects.filter(cgccpf=cgccpf)[0]

    incentivador_filter='incentivador=%s'%(str(cgccpf))
    doacoes_filter = "cgccpf=%s"%(str(cgccpf))

    projeto_table = ProjetoTable()
    projeto_table.data_url+=incentivador_filter

    doacao_table = DoacaoTable()
    doacao_table.data_url+=doacoes_filter


    return render(request, 'incentivadorDetail.html', {"incentivador" : incentivador,
     "projeto_table" : projeto_table, "doacao_table" : doacao_table})


def estatisticasView(request):

    return render(request, 'estatisticas.html', {})


#@login_required()
def apiView(request):

    return render(request, 'api.html', { })

def sobreView(request):

    return render(request, 'sobre.html', { })

def projetosDetail(request, PRONAC):

    projeto = Projeto.objects.filter(PRONAC=PRONAC)[0]

    #raise Http404 if None

    return render(request, 'projetoDetail.html', { "projeto" : projeto})


def contactView(request):
    if request.method == 'POST':

        remoteip =  request.META.get('REMOTE_ADDR')
        recaptcha = request.POST.get('g-recaptcha-response')
        recaptcha_url = 'https://www.google.com/recaptcha/api/siteverify'

        params = {'secret' : settings.GOOGLE_CAPTCHA_SECRET, 'response' : recaptcha, 'remoteip' : remoteip}

        post_response = requests.post(recaptcha_url, params=params)

        if post_response.json()['success'] != True:
            return render(request, 'contact_2.html', {'form' : ContactForm(), "captcha" : 'False'})

        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        content_mail = "name : %s message : %s"%(name, message)

        return_value = send_mail('Contato Portal Rouanet', content_mail, settings.CONTACT_FROM_MAIL,
         settings.CONTACT_TO_MAIL, fail_silently=False)

        if return_value == 1:
            success = 'True'
        else:
            success = 'False'

        return render(request, 'contact_2.html', {'form' : ContactForm(), "success" : success})



    return render(request, 'contact_2.html', {'form' : ContactForm(), })


def test(request):

    table = ProjetoTable2()

    return render(request, 'test.html', {'table' : table})

def handler404(request):
    response = render_to_response('404_custom.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response
