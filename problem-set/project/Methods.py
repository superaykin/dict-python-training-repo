from datetime import datetime
import time

# file variables
bloodDict = { "000" : "O-", "001" : "O+", "100" : "A-", "101" : "A+", "010" : "B-", "011" : "B+", "110" : "AB-", "111" : "AB+"}

def isValidDob(dateString:str) :
    try:
        datetime.strptime(dateString, "%Y-%m-%d")
        return True
    except ValueError:
        return False
    
def handleDob():
    while True:
        dob = input("Enter dob (YYYY-MM-DD): ")
        if isValidDob(dob):
            return dob
        else:
            print("Date of birth invalid. Please try again...")
    
                    
def extractBlood(lastName:str, firstName:str, dateOfBirth) :
    d1 = lastName[0].upper()
    d2 = firstName[0].upper()

    # initials to alpha sequence
    keyList = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    d1index = keyList.index(d1) + 1
    d2index = keyList.index(d2) + 1

    # dob to timestamp
    dt = datetime.strptime(dateOfBirth, "%Y-%m-%d")
    timeStamp = int(dt.timestamp())
    #timeStamp = int(time.mktime(dt.timetuple()))

    d3index = dt.month
    key = (d1index + d2index + d3index) / 8.0
    
    bIndex = key

    if key < 1:
        bIndex = 1 / key
    
    elif key > 8:
        bIndex = 8
    

    bloodSeq = round(bIndex)
    bdKeys = list(bloodDict.keys())

    bloodCode = bdKeys[bloodSeq - 1]
    bloodSample = str(d1index).zfill(2) + str(d2index).zfill(2) + bloodCode + str(timeStamp)

    # today to timestamp
    logTimeStamp = int(datetime.today().timestamp())
    
    # log blood sample taken
    with open("BoodBank.txt", "a") as file:
        logDetails = logTimeStamp, lastName.upper(), firstName.upper(), bloodSample
        file.write(','.join(map(str, logDetails)) + '\n')

    return bloodSample


def identifyBlood(bloodString:str) :
    # extract the blood
    bloodGroup = bloodString[4:7]

    antigenCodes = [
        ["100", "A ANTIGEN"],
        ["010", "B ANTIGEN"],
        ["001", "RH FACTOR"]
    ]
    
    bloodResult = []
    #apply antigen
    for a in antigenCodes :
        res = applyAntigen(bloodGroup, a[0])
        print(F"Applying {a[1]}...")
        if res :
            print(F"Sample reacted to reagent {a[1]}.")
            reaction = 1
        else :
            print(F"Sample did not react to reagent {a[1]}.")
            reaction = 0
        # append reaction to result holder
        bloodResult.append(reaction)

    # display result   
    print(F"Result set: {bloodResult}")

    # create string index result
    stringResult = ''
    for i in bloodResult :
        stringResult += str(i)

    # compare and get blood type in dictionary and return values
    result = {
        "RESULTSET" : bloodResult,
        "REMARKS" : bloodDict[stringResult]
    }

    return result

def applyAntigen(bloodSample, antigen) :
    # convert to binary
    blood = int(bloodSample, 2)
    antigenSample = int(antigen, 2)

    # test
    reacted = (blood & antigenSample) != 0

    # return bool
    return reacted



