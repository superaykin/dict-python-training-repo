# file manager module
from datetime import datetime

def readDB() :
    #method that open and read db config
    dbFile = "db.config"
    credentials = {}
    file = open(dbFile, "r")
    for line in file:
        line = line.strip()

        # skip
        if line.startswith(";") or line == "":
            continue

        # split
        if "=" in line:
            key, value = line.split("=", 1)
            credentials[key.strip()] = value.strip()

    file.close()
    return credentials

def logToFile(logDetails:str) :
    logDate = datetime.now()
    fileName = "logFile.txt"
    file = open(fileName, "w")
    print(F"{logDate} | {logDetails}", file=file)
    print("Successfully saved...")
    file.close()