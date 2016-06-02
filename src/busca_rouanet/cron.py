from datetime import datetime
from models import Projeto, Proponente, Incentivador, Doacao
from api_handler import get_item

import sys

from utils.Log import Log

def my_scheduled_job():

	f  = open('/home/lafa/django-1.9/projects/salicPortal/file.txt', 'w')
  	f.write('Cron job : '+str(datetime.now())+'\n')
  	f.close()
