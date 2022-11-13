from . import procedimientos

def addExtraService(id_reserve, id_extSrv, included=True):
    serviceAdded = procedimientos.getUserReserves(id_reserve, id_extSrv, included)
    return serviceAdded