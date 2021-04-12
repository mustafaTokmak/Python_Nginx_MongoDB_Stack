from dto import *

def health_check():
    if Healthcheck.objects():
        healthcheck_obj = Healthcheck.objects().first()
    else:
        healthcheck_obj = Healthcheck()
    healthcheck_obj.updatedate = datetime.datetime.utcnow()
    healthcheck_obj.save()
    return True,''

def sum(a,b):
    return a+b
    
