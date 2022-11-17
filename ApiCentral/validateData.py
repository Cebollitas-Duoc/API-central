import re

def validateDictionary(data, format):
    for k, v in format.items():
        r = validateData(data.get(k), v)
        name = v.get("name", "")
        if name != "":
            name += ": "
        if (not r[0]):
            return (r[0], name + r[1])
    return (True, "")


def validateData(data, format):
    validators = [
        isOfType,
        isUnderMax,
        isOverMin,
        lenEquals,
        hasPattern

    ]

    r = canBeNull(data, format)
    if (not r[0]):
        return r
    elif (data == None):
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
    lenght = format.get("len", None)
    if (lenght == None):
        return (True, "")
    
    if (len(data) != lenght):
        if lenght == 1:
            return (False, f"Debe tener 1 caracter")
        return (False, f"Debe tener {lenght} caracteres")
    return (True, "")

def isUnderMax(data, format):
    max = format.get("max", None)
    if (max == None):
        return (True, "")
    
    if (len(data) > max):
        return (False, f"Tiene mas de {max} caracteres")
    return (True, "")

def isOverMin(data, format):
    min = format.get("min", None)
    if (min == None):
        return (True, "")
    
    if (len(data) < min):
        if min == 1:
            return (False, f"Debe tener por lo menos 1 caracter")
        return (False, f"Debe tener por lo menos {min} caracteres")
    return (True, "")

def canBeNull(data, format):
    if (data == None):
        if (format.get("isNull", False)):
            return (True, "")
        else:
            return (False, "No esta")
    
    return (True, "")

def isOfType(data, format):
    t = format.get("type", "txt")
    valid = False
    msg = ""
    if t == "int":
        valid = data.isnumeric()
        if (not valid):
            msg = "Tiene que ser un numero entero"
    elif t == "float":
        data = data.replace(",", ".")
        valid = isFloat(data)
        if (not valid):
            msg = "Tiene que ser un numero flotante"
    elif t == "txt":
        valid = True
    elif t == "email":
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        valid = re.fullmatch(regex, data)
        if (not valid):
            msg = "Tiene que ser un email valido"

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