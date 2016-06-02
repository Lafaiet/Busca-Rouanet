from __future__ import unicode_literals
from django.db import models



class Doacao(models.Model):

	nome_projeto = models.CharField(max_length=400)
	nome_doador = models.CharField(max_length=300)
	cgccpf = models.CharField(max_length=20)
	valor = models.DecimalField(max_digits=20, decimal_places=2)
	data_recibo = models.DateField(null=True)
	PRONAC = models.CharField(max_length=20)
	projeto_related  = 	models.ForeignKey('Projeto', on_delete=models.CASCADE)
	incentivador_related  = models.ForeignKey('Incentivador', on_delete=models.CASCADE)


	def __unicode__(self):
		return '%s' % self.PRONAC+':'+self.cgccpf

class Projeto(models.Model):

	PRONAC = models.CharField(primary_key=True, max_length=20)
	situacao = models.CharField(max_length=250)
	area = models.CharField(max_length=100)
	segmento = models.CharField(max_length=100)
	cgccpf = models.CharField(max_length=20)
	nome = models.CharField(max_length=400)
	proponente = models.CharField(max_length=200)
	mecanismo = models.CharField(max_length=100)
	enquadramento = models.CharField(max_length=100)
	UF = models.CharField(max_length=2)
	municipio = models.CharField(max_length=100)
	data_inicio = models.DateField(null=True)
	ano_projeto = models.CharField(max_length=2)
	data_termino = models.DateField(null=True)
	valor_projeto = models.DecimalField(max_digits=20, decimal_places=2)
	outras_fontes = models.DecimalField(max_digits=20, decimal_places=2, null=True)
	valor_captado = models.DecimalField(max_digits=20, decimal_places=2)
	valor_proposta = models.DecimalField(max_digits=20, decimal_places=2)
	valor_solicitado = models.DecimalField(max_digits=20, decimal_places=2)
	valor_aprovado = models.DecimalField(max_digits=20, decimal_places=2)

	etapa = models.TextField(null=True)
	providencia = models.TextField(null=True)
	objetivos = models.TextField(null=True)
	ficha_tecnica = models.TextField(null=True)
	acessibilidade = models.TextField(null=True)
	estrategia_execucao = models.TextField(null=True)
	justificativa = models.TextField(null=True)
	resumo = models.TextField(null=True)
	sinopse = models.TextField(null=True)
	impacto_ambiental = models.TextField(null=True)
	democratizacao = models.TextField(null=True)
	especificacao_tecnica = models.TextField(null=True)

	proponente_related = models.ForeignKey('Proponente', on_delete=models.CASCADE)


	def __unicode__(self):
		return '%s' % self.PRONAC

	def get_absolute_ulr(self):
		return '/%s/' % self.PRONAC



class Interessado(models.Model):
	
	cgccpf = models.CharField(max_length=20, primary_key=True)
	nome = models.CharField(max_length=300)
	responsavel = models.CharField(null=True, max_length=150)
	UF = models.CharField(max_length=2)
	municipio = models.CharField(max_length=100)
	tipo_pessoa = models.CharField(max_length=20)

	def __unicode__(self):
		return '%s' % self.cgccpf

	def get_absolute_ulr(self):
		return '/%s/' % self.cgccpf

class Proponente(Interessado):
	
	quantidade_projetos = models.IntegerField()

class Incentivador(Interessado):
	
	total_doado	 = models.DecimalField(max_digits=20, decimal_places=2)
