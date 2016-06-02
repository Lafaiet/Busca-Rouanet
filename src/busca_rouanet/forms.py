# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.forms import AuthenticationForm



from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field,Div, Fieldset, ButtonHolder
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions, AppendedText)

from crispy_forms.bootstrap import InlineField

from api_handler import get_item

from models import *


def get_form_choices(item_name):
    items_from_api = get_item("projetos/%s"%item_name)
    items = []

    items_from_api.sort()

    for item in items_from_api:
        items.append(item.values()[0])

    return items

def humanize_year(year):
    if int(year) >= 82:
        return '19'+str(year)
    return '20'+str(year)

estados = ["ESTADO", "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA",
                "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]

class ProjetoForm(forms.Form):

    PRONAC = forms.IntegerField(label="PRONAC", required = False)
    nome = forms.CharField(label="nome do projeto", required = False)

    proponente = forms.CharField(label="nome do proponente", required = False)
    cgccpf = forms.CharField(label="cgc/cpf do proponente", required = False)

    #segmento_choices  = map( lambda projeto: projeto.segmento, Projeto.objects.distinct('segmento'))
    segmento_choices = []

    segmento  = forms.ChoiceField(choices=[('SEGMENTO', u'SEGMENTO')]+zip(segmento_choices, segmento_choices), required = False)

    #area_choices = map( lambda projeto: projeto.area, Projeto.objects.distinct('area'))
    area_choices = []

    area  = forms.ChoiceField(choices=[('AREA', u'AREA')]+zip(area_choices, area_choices), required = False)

    UF = forms.ChoiceField(help_text='Estados', choices=zip(estados, estados), required = False)

    municipio = forms.CharField(label=u"Município", required = False)

    captacao = forms.ChoiceField(choices = (('captacao', u'CAPTAÇÕES'),
         ('comcaptacoes', u'Com captações'), ('semcaptacoes', u'Sem captações')),
          required = False)

    conclusao = forms.ChoiceField(choices = (('conclusao', u'CONCLUSÃO'), ('concluido', u'Concluído'),
         ('naoconcluido', u'Não Concluído')), required = False)


    #projetos_anos  = map( lambda projeto: projeto.ano_projeto, Projeto.objects.distinct('ano_projeto'))
    projetos_anos = []
    anos_human  = map( lambda ano: humanize_year(ano), projetos_anos)

    ano_projeto = forms.ChoiceField(choices = [('ano_projeto', 'Ano do projeto')]+zip(projetos_anos, anos_human), required = False)


    def __init__(self, *args, **kwargs):


        self.helper = FormHelper()
        self.helper.form_tag = False

        self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'

        self.helper.layout = Layout(
        	Div(
                Div('PRONAC', css_class='col-xs-2'),
                Div('nome', css_class='col-xs-2'),
                Div('ano_projeto', css_class='col-xs-2'),
                Div('proponente', css_class='col-xs-2'),
                Div('cgccpf', css_class='col-xs-2'),
                Div('UF', css_class='col-xs-2'),
                Div('municipio', css_class='col-xs-2'),
                Div('area', css_class='col-xs-2'),
                Div('segmento', css_class='col-xs-2'),
                Div('captacao', css_class='col-xs-2'),
                Div('conclusao', css_class='col-xs-2'),

        		css_class='row-fluid',

        )
            )

        super(ProjetoForm, self).__init__(*args, **kwargs)



class ContactForm(forms.Form):
    Nome = forms.CharField()
    Email = forms.CharField()
    Comentario = forms.CharField(
        widget = forms.Textarea(),
    )

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-lg-3'
    helper.field_class = 'col-lg-3'
    helper.layout = Layout(
        Div(
    	PrependedText('Nome',
                      '<span class="glyphicon glyphicon-user"></span> ',
                      css_class='input-small'),
    	PrependedText('Email',
                      '<span class="glyphicon glyphicon-envelope"></span> ',
                      css_class='iinput-small'),

        Field('Comentario', rows="5", css_class='input-xlarge'),
        )
    )


class ProponenteForm(forms.Form):

    nome = forms.CharField(label="nome do proponente", required = False)
    tipo_pessoa = forms.ChoiceField(choices = (('tipodepessoa', 'TIPO DE PESSOA'), ('fisica', u'física'), ('juridica', u'jurídica')), required = False )
    municipio = forms.CharField(label=u"município do proponente", required = False)
    cgccpf = cgccpf = forms.CharField(label="cgc/cpf do proponente", required = False)
    UF = forms.ChoiceField(help_text='Estados', choices=zip(estados, estados), required = False)

    def __init__(self, *args, **kwargs):


        self.helper = FormHelper()
        self.helper.form_tag = False

        self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'

        self.helper.layout = Layout(
            Div(
                Div('nome', css_class='col-xs-2'),
                Div('tipo_pessoa', css_class='col-xs-2   '),
                Div('cgccpf', css_class='col-xs-2'),
                Div('UF', css_class='col-xs-2   '),
                Div('municipio', css_class='col-xs-3'),

                css_class='row-fluid',

        )
            )

        super(ProponenteForm, self).__init__(*args, **kwargs)


class IncentivadorForm(forms.Form):

    nome = forms.CharField(label="nome do incentivador", required = False)
    tipo_pessoa = forms.ChoiceField(choices = (('tipodepessoa', 'TIPO DE PESSOA'), ('fisica', u'física'), ('juridica', u'jurídica')), required = False )
    municipio = forms.CharField(label=u"município do incentivador", required = False)
    cgccpf = cgccpf = forms.CharField(label="cgc/cpf do incentivador", required = False)
    UF = forms.ChoiceField(help_text='Estados', choices=zip(estados, estados), required = False)

    def __init__(self, *args, **kwargs):


        self.helper = FormHelper()
        self.helper.form_tag = False

        self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'

        self.helper.layout = Layout(
            Div(
                Div('nome', css_class='col-xs-2'),
                Div('tipo_pessoa', css_class='col-xs-2   '),
                Div('cgccpf', css_class='col-xs-2'),
                Div('UF', css_class='col-xs-2   '),
                Div('municipio', css_class='col-xs-3'),

                css_class='row-fluid',

        )
            )

        super(IncentivadorForm, self).__init__(*args, **kwargs)


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Usuário", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Senha", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))
