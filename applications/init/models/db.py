#import os
#
#try: 
#	db = DAL(os.environ.get('DATABASE_URL'))
#except:
#	db = DAL('sqlite://storage.sqlite')
