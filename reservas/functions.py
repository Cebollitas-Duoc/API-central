from . import procedimientos
from departamentos import procedimientos as dptoP

def addExtraService(id_reserve, id_extSrv, included=True):
    serviceAdded = procedimientos.getUserReserves(id_reserve, id_extSrv, included)
    return serviceAdded

def calculateReservePrice(request):
    total = 0
    idDpto = request.data["Id_Departamento"]

    days = round((int(request.data["EndDate"]) - int(request.data["StartDate"])) / 86400000)

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

def rangeColidesWithReserves(newRange, idDpto):
    reservedRanges = procedimientos.getReservedRanges(idDpto)
    for reservedrange in reservedRanges[0]:
        if rangeCollision(newRange, reservedrange):
            return True
    return False

def rangeCollision(range1, range2):
    if valueInRange(range1[0], range2[0], range2[1]): # colicion de cola
        return True
    elif valueInRange(range1[1], range2[0], range2[1]): # colicion de cabeza
        return True
    elif valueInRange(range2[0], range1[0], range1[1]): # colicion interna
        return True
    elif (range1[0] == range2[0]):
        return True
    elif (range1[1] == range2[1]):
        return True

    return False

def valueInRange(value, start, end):
    return start < value < end