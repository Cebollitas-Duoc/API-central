from . import procedimientos
from departamentos import procedimientos as dptoP

def addExtraService(id_reserve, id_extSrv, included=True):
    serviceAdded = procedimientos.getUserReserves(id_reserve, id_extSrv, included)
    return serviceAdded

def calculateReservePrice(request):
    total = 0
    idDpto = request.data["Id_Departamento"]

    days = ((int(request.data["EndDate"]) - int(request.data["StartDate"])) / 86400000) + 1

    dptoData = dptoP.viewDpto(idDpto)
    if (dptoData[1]):
        total += (dptoData[0][6] * days)

    allDptoExtraSrv = dptoP.listExtraServices(idDpto)[0]

    if ("extraServices" in request.data):
        for extSrvId in request.data["extraServices"].split(","):
            if extSrvId == "":
                continue
            for DptoExtraSrv in allDptoExtraSrv:
                if (DptoExtraSrv["Id_ExtraService"] == int(extSrvId)):
                    total += DptoExtraSrv["Valor"] 
    
    return total