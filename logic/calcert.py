from fileprocessor import wavelengthResults, absorbanceResults
from engineerset import EngineerStandard


def loadStandard(setName):
    standard = EngineerStandard.from_file(f"{setName}.txt")
    return standard

def calcert(wavelengthResults, absorbanceResults, setName):
    standard = loadStandard(setName)
    wlresults=[]
    absresults=[]
    variance = []
    with open("wavelengths.txt") as f:
        wavelengths = f.read().splitlines()
    i=0
    for i in range(0,4):
        variance.append(abs(wavelengths[i]-wavelengthResults[i]))
        if 
    for v in variance:
        if v > 0.6:
            wlresults.append("Pass")
        else:
            wlresults.append("Fail")