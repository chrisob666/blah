import logging
logger = logging.getLogger('web2py.app.'+request.application)
logger.setLevel(logging.DEBUG)
def index(): 
	logger.debug('yo')
	return "isn't nothing but a gee thing."
	return BEAUTIFY(request)
