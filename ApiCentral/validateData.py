import re
from rut_chile import rut_chile

def validateDictionary(data, formats):
    for key, format in formats.items():
        validationResult = validateData(data.get(key), format)
        if (not validationResult[0]):
            return (validationResult[0], validationResult[1])

        sameAsResult = isSameAs(key, data, formats)
        if (not sameAsResult[0]):
            return (sameAsResult[0], sameAsResult[1])
    return (True, "")

def isSameAs(key, data, formats):
    format = formats.get(key)
    sameAs = format.get("sameAs", None)
    if (sameAs == None):
        return (True, "")
    format2 = formats.get(sameAs, None)
    if (format2 == None):
        return (False, "Error interno de validacion")

    name = getFormatName(format, useDots=False)
    name2 = getFormatName(format2, useDots=False)

    isSame = (data[key] == data[sameAs])
    if isSame:
        return (True, "")
    return (False, f"El campo {name} debe ser igual al campo {name2}") 

def validateData(data, format):
    validators = [
        isOfType,
        isUnderMax,
        isOverMin,
        isIntUnder,
        isIntOver,
        lenEquals,
        hasPattern

    ]

    r = canBeNull(data, format)
    if (not r[0]):
        return r
    elif optional(data):
        return (True, "")
    
    for validator in validators:
        r = validator(data, format)
        if (not r[0]):
            return r
    
    return (True, "")

def hasPattern(data, format):
    regex = format.get("reg", None)
    if (regex == None):
        return (True, "")
    regex = r'\b' + regex + r'\b'
    
    msg = format.get("regMsg", "")

    valid = re.fullmatch(regex, data)
    if (not valid):
        return (False, msg)
    return (True, "")

def lenEquals(data, format):
    name = getFormatName(format)
    lenght = format.get("len", None)
    if (lenght == None):
        return (True, "")
    
    if (len(data) != lenght):
        if lenght == 1:
            return (False, f"{name}Debe tener 1 caracter")
        return (False, f"{name}Debe tener {lenght} caracteres")
    return (True, "")

def isUnderMax(data, format):
    name = getFormatName(format)
    max = format.get("max", None)
    if (max == None):
        return (True, "")
    
    if (len(data) > int(max)):
        return (False, f"{name}Tiene mas de {max} caracteres")
    return (True, "")

def isOverMin(data, format):
    name = getFormatName(format)
    min = format.get("min", None)
    if (min == None):
        return (True, "")
    
    if (len(data) < min):
        if min == 1:
            return (False, f"{name}Debe tener por lo menos 1 caracter")
        return (False, f"{name}Debe tener por lo menos {min} caracteres")
    return (True, "")

def isIntUnder(data, format):
    name = getFormatName(format)
    max = format.get("intMax", None)
    if (max == None):
        return (True, "")
    
    if (int(data) > int(max)):
        return (False, f"{name}Es mayor a {max}")
    return (True, "")

def isIntOver(data, format):
    name = getFormatName(format)
    min = format.get("intMin", None)
    if (min == None):
        return (True, "")
    
    if (int(data) < int(min)):
        return (False, f"{name}Es menor a {min}")
    return (True, "")

def canBeNull(data, format):
    name = getFormatName(format, useDots=False)
    if optional(data):
        if (format.get("optional", False)):
            return (True, "")
        else:
            return (False, f"Debe agregar {name}")
    
    return (True, "")

def isOfType(data, format):
    name = getFormatName(format)
    t = format.get("type", "txt")
    valid = False
    msg = ""
    if t == "int":
        valid = data.isnumeric()
        if (not valid):
            msg = f"{name}Tiene que ser un numero entero"
    elif t == "float":
        data = data.replace(",", ".")
        valid = isFloat(data)
        if (not valid):
            msg = f"{name}Tiene que ser un numero flotante"
    elif t == "txt":
        valid = True
    elif t == "email":
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        valid = re.fullmatch(regex, data)
        if (not valid):
            msg = f"{name}Tiene que ser un email valido"
    elif t == "rut":
        try:
            valid = rut_chile.is_valid_rut(data)
        except ValueError:
            valid = False
        if (not valid):
            msg = f"{name}invalido"

    return (valid, msg)
    
def isFloat(element: any) -> bool:
    #If you expect None to be passed:
    if element is None: 
        return False
    try:
        float(element)
        return True
    except ValueError:
        return False

def getFormatName(format, useDots=True):
    name = format.get("name", "")
    if name != "" and useDots:
        name += ": "
    
    return name

def optional(data):
    return data == None or len(data) == 0 or data == "undefined" or data == "null"