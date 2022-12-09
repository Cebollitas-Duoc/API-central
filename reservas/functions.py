from . import procedimientos
from departamentos import procedimientos as dptoP
from reservas import procedimientos as resP
from datetime import datetime, timedelta
import random
from transbank.webpay.webpay_plus.transaction import Transaction



def addExtraService(id_reserve, id_extSrv, included=True):
    serviceAdded = procedimientos.getUserReserves(id_reserve, id_extSrv, included)
    return serviceAdded

def calculateReservePrice(request):
    total = 0
    idDpto = request.data["Id_Departamento"]

    startDate = datetime.fromtimestamp(int(request.data["StartDate"]) / 1000)
    endDate   = datetime.fromtimestamp(int(request.data["EndDate"]) / 1000)
    delta = endDate - startDate
    dptoData = dptoP.viewDpto(idDpto)
    if (dptoData[1]):
        total += (dptoData[0][6] * delta.days)

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

def getDateRanges(start, end):
    startDate = datetime.fromtimestamp(start / 1000)
    endDate   = datetime.fromtimestamp(end / 1000)
    delta = endDate - startDate

    dates = []
    for i in range(delta.days):
        day = startDate + timedelta(days=i)
        dates.append(day.strftime("%Y-%m-%d"))
    
    return dates

def TransbankMakePay(request):
    buy_order = request.data["Id_Reserva"]
    session_id = str(random.randrange(1000000, 99999999))
    cursor = resP.getReserva(request.data["Id_Reserva"])
    total = cursor["VALORTOTAL"]
    amount = total
    request_domain = request._current_scheme_host
    return_url = "http://mrmeme.cl/pagos/verificarpago"
    if ("localhost" in request_domain):
        return_url =  "http://localhost:8080/pagos/verificarpago"
    create_request = {
        "buy_order": buy_order,
        "session_id": session_id,
        "amount": amount,
        "return_url": return_url
    }
    response = (Transaction()).create(buy_order, session_id, amount, return_url)
    link = response['url'] + '?token_ws=' + response['token']
    print(link)
    return link

def TransbankCommit(token):
    response = (Transaction()).commit(token=token)
    return response
