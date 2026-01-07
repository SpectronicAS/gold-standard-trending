from engineerset import EngineerStandard


def loadStandard(setName):
    standard = EngineerStandard.from_file(f"{setName}.txt")
    return standard

def calcert(wavelengthResults, absorbanceResults, setName):
    standard = loadStandard(setName).return_attributes()
    wlresults=[]
    absresults=[]
    wlvariance = []
    absvariance = []
    with open("wavelengths.txt") as f:
        wavelengths = f.read().splitlines()
    i=0
    for i in range(0,4):
        wlvariance.append(abs(wavelengths[i]-wavelengthResults[i]))
        absvariance.append(abs(standard[i]-absorbanceResults[i]))
    for v in wlvariance:
        if v > 0.6:
            wlresults.append("Fail")
        else:
            wlresults.append("Pass")
    for a in absvariance:
        if a > 0.1:
            absresults.append("Fail")
        else:
            absresults.append("Pass")
    return wlresults, absresults

