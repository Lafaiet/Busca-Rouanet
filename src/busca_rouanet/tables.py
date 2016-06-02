# -*- coding: utf-8 -*-

import django_tables2 as tables
from models import Projeto, Doacao
from django_tables2.utils import A 
from django.contrib.humanize.templatetags.humanize import intcomma
from django.utils.html import format_html
import datetime


class ColumnWithThousandsSeparator(tables.Column):
    def render(self,value):
    	if int(value)==0:
    		return format_html('<p style="color:red">{}</p>', str(value))
        return str(intcomma(value))

class ColumnAno(tables.Column):
    def render(self,value):
    	if int(value) >= 82:
    		return '19'+str(value)
        return '20'+str(value)

class ColumnDate(tables.Column):
	def render(self,value):

		splited_value = value.split('-')
		if len(splited_value) > 0: 
			year = int(splited_value[0])
			month = int(splited_value[1])
			day = int(splited_value[2])
			given_date = datetime.datetime(year, month, day)
			todays_date = datetime.datetime.now()

			date_formated = splited_value[2]+'/'+splited_value[1]+'/'+splited_value[0]

			if given_date < todays_date:
				return format_html('<p style="color:red">{}</p>', date_formated)
			else:
				return date_formated
		return value


class ProjetoTable(tables.Table):
	situacao = tables.Column(verbose_name=u"Situação")
	area = tables.Column(verbose_name=u"Área")
	cgccpf = tables.Column(verbose_name=u"CPF/CGC")
	nome = tables.Column()
	proponente = tables.Column()
	PRONAC = tables.LinkColumn('projetosDetail', args=[A('PRONAC')])
	mecanismo = tables.Column()
	enquadramento = tables.Column()
	segmento = tables.Column()
	UF = tables.Column()
	municipio = tables.Column(verbose_name=u"município")
	# data_inicio = ColumnDate(verbose_name=u"Data de início")
	# data_termino = ColumnDate(verbose_name=u"Data de término")
	data_inicio = tables.Column(verbose_name=u"Data de início")
	data_termino = tables.Column(verbose_name=u"Data de término")
	ano_projeto = ColumnAno(verbose_name="Ano do projeto")
	valor_projeto = ColumnWithThousandsSeparator()
	outras_fontes = ColumnWithThousandsSeparator()
	valor_captado = ColumnWithThousandsSeparator()
	valor_proposta = ColumnWithThousandsSeparator()
	valor_solicitado = ColumnWithThousandsSeparator()
	valor_aprovado = ColumnWithThousandsSeparator()

	class Meta:
		attrs = {"class": "paleblue", 'width':'60%'}
		sequence = ("PRONAC", "nome", "ano_projeto", "proponente", "cgccpf", "UF", "municipio",
		 "enquadramento", "area", "segmento", "mecanismo", "data_inicio",
		  "data_termino", "valor_proposta", "valor_solicitado", "valor_aprovado","valor_captado")


class ProponenteTable(tables.Table):	
	nome = tables.Column()
	responsavel = tables.Column(verbose_name=u"Responsável")
	tipo_pessoa = tables.Column(verbose_name=u"Tipo de pessoa")
	municipio = tables.Column(verbose_name=u"Município")
	cgccpf	 = tables.LinkColumn('proponenteDetail',verbose_name=u"CPF/CGC", args=[A('cgccpf')])
	UF = tables.Column()
	#quantidade_projetos = tables.Column(verbose_name=u"Quantidade de projetos apresentados")

	class Meta:
		attrs = {"class": "paleblue", 'width':'100%'}
		sequence = ("cgccpf", "nome", "tipo_pessoa",  "UF",
		 "municipio", "responsavel")

class IncentivadorTable(tables.Table):	
	nome = tables.Column()
	responsavel = tables.Column(verbose_name=u"Responsável")
	tipo_pessoa = tables.Column(verbose_name=u"Tipo de pessoa")
	municipio = tables.Column(verbose_name=u"Município")
	UF = tables.Column()
	cgccpf = tables.LinkColumn('incentivadorDetail',verbose_name=u"CPF/CGC", args=[A('cgccpf')])
	total_doado = ColumnWithThousandsSeparator(verbose_name=u"Total Doado")

	class Meta:
		attrs = {"class": "paleblue", 'width':'100%'}
		sequence = ("cgccpf", "nome", "tipo_pessoa",  "UF",
		 "municipio", "responsavel")

class DoacaoTable(tables.Table):

	nome_projeto = tables.Column()
	valor = ColumnWithThousandsSeparator()
	data_recibo = tables.Column(verbose_name=u"Data do recibo")
	PRONAC = tables.LinkColumn('projetosDetail', args=[A('PRONAC')])

	class Meta:
		attrs = {"class": "paleblue", 'width':'150%'}
		sequence = ("PRONAC", "nome_projeto", "data_recibo",  "valor")