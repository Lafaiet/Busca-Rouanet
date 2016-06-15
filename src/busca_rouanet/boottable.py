# -*- coding: utf-8 -*-

class ColumnField(object):

    def __init__(self, name, verbose_name = None, base_url = None, isReal = False):
        self.name = name

        if verbose_name != None:
            self.verbose_name = verbose_name
        else:
             self.verbose_name = name

        if base_url != None:
            self.is_linkable = True
            self.base_url = base_url

        self.isReal = isReal

class BootstrapTable(object):

    toggle = "table"
    locale = "pt-BR"
    toolbar = "#toolbar"
    data_url = ""
    show_refresh = "true"
    click_to_select = "true"
    show_columns = "true"
    show_export = "true"
    height = "500"
    width = "400"
    pagination = "true"
    page_list = "[5, 10, 20, 50, 100]"
    side_pagination = "server"

    sequence = []


class ProjetoTable(BootstrapTable):

    column_fields =  [
        ColumnField('PRONAC', base_url = 'projetos'),
        ColumnField('nome'),
        ColumnField('ano_projeto', verbose_name="Ano do projeto"),
        ColumnField('proponente'),
        ColumnField('cgccpf', verbose_name=u"CPF/CGC"),
        ColumnField('UF'),
    	ColumnField('municipio', verbose_name=u"município"),
        ColumnField('enquadramento'),
        ColumnField('area', verbose_name=u"Área"),
        ColumnField('segmento'),
        ColumnField('mecanismo'),
    	ColumnField('data_inicio', verbose_name = u"Data de início"),
    	ColumnField('data_termino', verbose_name = u"Data de término"),
        ColumnField('valor_proposta', isReal = True),
        ColumnField('valor_projeto', isReal = True),
        ColumnField('valor_solicitado', isReal = True),
        ColumnField('valor_aprovado', isReal = True),
    	ColumnField('outras_fontes', isReal = True),
    	ColumnField('valor_captado', isReal = True),
        ColumnField('situacao', verbose_name=u"Situação"),
    ]

    table_id = "projetotable"
    data_url = 'http://localhost:8000/data/projetos/?'
    link_url = '/projetos/'

class IncentivadorTable(BootstrapTable):
    column_fields =  [
    ColumnField('nome'),
    ColumnField('cgccpf', verbose_name=u"CPF/CGC", base_url = 'incentivadores'),
	ColumnField('tipo_pessoa',verbose_name=u"Tipo de pessoa"),
    ColumnField('UF'),
	ColumnField('municipio', verbose_name=u"Município"),
    ColumnField('total_doado', isReal=True),
    ColumnField('responsavel', verbose_name=u"Responsável"),
    ]

    data_url = 'http://localhost:8000/data/incentivadores/?'
    link_url = '/incentivadores/'
    table_id = "incentivadortable"

class ProponenteTable(BootstrapTable):
    column_fields =  [
        ColumnField('nome'),
        ColumnField('cgccpf', verbose_name=u"CPF/CGC", base_url = 'proponentes'),
    	ColumnField('tipo_pessoa',verbose_name=u"Tipo de pessoa"),
    	ColumnField('UF'),
    	ColumnField('municipio', verbose_name=u"Município"),
        ColumnField('responsavel', verbose_name=u"Responsável"),
    ]

    data_url = 'http://localhost:8000/data/proponentes/?'
    link_url = '/proponentes/'
    table_id = "proponentetable"

class DoacaoTable(BootstrapTable):
    column_fields =  [
        ColumnField('PRONAC', base_url = 'projetos'),
    	ColumnField('nome_projeto', verbose_name='Projeto'),
    	ColumnField('valor', isReal=True),
    	ColumnField('data_recibo', verbose_name=u"Data do recibo"),
    ]

    data_url = 'http://localhost:8000/data/doacoes/?'
    link_url = '/projetos/'
    table_id = "doacaotable"

class CaptacaoTable(BootstrapTable):
    column_fields =  [
        ColumnField('cgccpf', verbose_name=u"CPF/CGC", base_url = 'incentivadores'),
        ColumnField('nome_doador', verbose_name='Doador'),
    	ColumnField('valor', isReal=True),
    	ColumnField('data_recibo', verbose_name=u"Data do recibo"),
    ]

    data_url = 'http://localhost:8000/data/doacoes/?'
    link_url = '/incentivadores/'
    table_id = "captacaotable"
