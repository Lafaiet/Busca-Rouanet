import requests
from django.conf import settings
import logging
import re

logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)



def get_item(item_name, item_args = '', offset = None, max_items = None):

	uri_call = settings.SALIC_API_SERVER+item_name+("/?"+item_args if item_args else "/")
	items = []

	try:
		#logger.debug("api call : "+uri_call)

		resp = requests.get(uri_call)
		if resp.status_code == 200:
		    #logger.debug("Successfull api call")
		    items  =  resp.json()
		    total_count = resp.headers.get('X-Total-Count')

		    # if total_count is not None:
		    # 	total_count = int(total_count)
		    	
		    # 	if offset is not None:
		    # 		start_offset = total_count-offset
		    # 	else:
		    # 		start_offset = len(items)

		    # 	logger.debug("There are %d more items to be fetched"%(total_count-start_offset)) 
		    # 	items += get_remaining_items(uri_call, start_offset, total_count, len(items), max_items or settings.MAX_API_ITEMS)
		else :
			#logger.warn("Call return code was %d"%resp.status_code)
			pass

	except Exception as e:
	    logger.error( str(e))

	return items

def get_remaining_items(uri_call, start_offset, total_count, steps, max_items):

	items = []

	for offset in range(start_offset, max_items, steps ):
		try:
			if "offset" in uri_call:
				new_uri_call = re.sub(r"offset=[\d+]*","offset="+str(offset), uri_call)
			else:
				new_uri_call = uri_call + "?offset="+str(offset) if "?" not in uri_call else uri_call + "offset="+str(offset)

			logger.debug("api call : "+new_uri_call)

			resp = requests.get(new_uri_call)
			if resp.status_code == 200:
			    logger.debug("Successfull api call")
			    items +=  resp.json()

		except Exception as e:
		    logger.error( 'Could not fetch all items '+str(e))
		    return items

	return items
