import logging
logger = logging.getLogger('web2py.app.'+request.application)
logger.setLevel(logging.DEBUG)
def index(): 
	return BEAUTIFY(request)
