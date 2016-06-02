from busca_rouanet.models import Projeto, Proponente, Incentivador, Doacao
from busca_rouanet.api_handler import get_item

from Log import Log

def populate_database():

	#total_num = 138714
	total_num = 100
	start_offset = Projeto.objects.count()
	saved_projects = 0
	last_sucessful = None

	for offset in range(start_offset, total_num+start_offset, 100 ):

		projetos = get_item("projetos", item_args = "extra_fields=true&offset="+str(offset))

		for projeto in projetos:

			print "Adding project info with PRONAC: %s"%(str(projeto['PRONAC']))

			proponente = get_item("proponentes", item_args = "cgccpf="+str(projeto['cgccpf']))

			if len(proponente) > 0:
				proponente = proponente[0]

			else:
				Log.error("Error getting proponente from api. Last sucessfull %s"%(str(last_sucessful)))
				return

			try:
				proponente = Proponente(**proponente)
				proponente.save()
			except Exception as e:
				Log.error(str(e))
				Log.error("Error trying to save proponent. Last sucessfull %s"%(str(last_sucessful)))
				return

			print "Adding project..."

			try:
				projeto_persistent = Projeto(proponente_related = proponente, **projeto)
				projeto_persistent.save()
			except Exception as e:
				Log.error(str(e))
				Log.error("Error trying to save project! Last sucessfull %s"%(str(last_sucessful)))
				return


			print "Adding donations..."
			captacoes = get_item("projetos/%s/captacoes"%(str(projeto_persistent.PRONAC)))

			for captacao in captacoes:

				print "Adding backer..."
				incentivador = get_item("incentivadores", item_args = "cgccpf=%s"%(captacao['cgccpf']))

				if len(incentivador) > 0:
					incentivador = incentivador[0]

				else:
					Log.error("Error getting backer from api. Last sucessfull %s"%(str(last_sucessful)))
					return

				try:
					incentivador = Incentivador(**incentivador)
					incentivador.save()
				except Exception as e:
					Log.error(str(e))
					Log.error("Error trying to save backer! Last sucessfull %s"%(str(last_sucessful)))
					return

				try:
					captacao_persistent = Doacao(incentivador_related = incentivador, projeto_related = projeto_persistent, **captacao)
					captacao_persistent.save()
				except Exception as e:
					Log.error(str(e))
					Log.error("Error trying to save donation! Last sucessfull %s"%(str(last_sucessful)))
					return


			saved_projects+=1
			last_sucessful = projeto_persistent.PRONAC
			print "Project with id %s persisted!"%(str(last_sucessful))
			#print '%d projects persisted so far'%(saved_projects)
			#print '\n\n'


		Log.info("%d Projects Populated!"%len(projetos))
		Log.info("%d Projects to go..."%(total_num-saved_projects))
	print "All Populated!"
