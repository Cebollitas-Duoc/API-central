import hashlib, string, random
from sympy import true

def validatePassword(password, encriptedPassword):
    encriptedPassword = sparatePassword(encriptedPassword)
    algorithm = int(encriptedPassword[0])
    weight = int(encriptedPassword[1])
    salt = encriptedPassword[2]
    hash = encriptedPassword[3]

    saltedPass = password+salt
    for i in range(weight):
        newHash = calculateHash(algorithm, saltedPass+str(i))
        if (newHash == hash):
            return True
    return False

def sparatePassword(password):
    return password.split("#")

def calculateHash(algorithm, var):
    algorithm = int(algorithm)
    if algorithm == 1:
        return sha256(var)

def sha256(var):
    return hashlib.sha256(str(var).encode('utf-8')).hexdigest()

def generateRandomStr(size=64):
   return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(size))

def hashPassword(password):
    algorithm = "01"
    weight = "40"
    salt = generateRandomStr(8)
    randomNumber = random.randrange(0, int(weight))
    password = f"{password}{salt}{randomNumber}"
    hashedPassword = f"{algorithm}#{weight}#{salt}#{calculateHash(algorithm, password)}"

    return hashedPassword