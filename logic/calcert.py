from engineerset import EngineerStandard


def loadStandard(setName: str):
    standard = EngineerStandard
    return standard.from_file(f"{setName}.txt")

def calcert(wavelengthResults, absorbanceResults, setName: str):
    standard = loadStandard(setName).return_attributes()
    wlresults=[]
    absresults=[]
    wlvariance = []
    absvariance = []
    with open("wavelengths.txt") as f:
        wavelengths = f.read().splitlines()
    i=0
    for i in range(0,5):
        wlvariance.append(abs(float(wavelengths[i])-wavelengthResults[i]))
        absvariance.append(abs(standard[i]-absorbanceResults[i]))
    for v in wlvariance:
        if v > 1:
            wlresults.append("Fail")
        else:
            wlresults.append("Pass")
    for a in absvariance:
        if a > 0.01:
            absresults.append("Fail")
        else:
            absresults.append("Pass")
    return wlresults, absresults, wlvariance, absvariance

