import numpy as np
from scipy.signal import find_peaks
from calcert import calcert

def parseFile(filepath):
    with open(filepath) as f:
        lines = f.read().splitlines()
    return lines


def wavelengthResults(lines):
    wavelengths = []
    absorbances = []
    wlpeaks = []
    for line in lines[6:-4]:
        wl, ab = line.split()
        wavelengths.append(float(wl))
        absorbances.append(float(ab))
    peaks, _ = find_peaks(absorbances, height=0.3)
    for peak in peaks:
        with open("wavelengths.txt") as f:
            wls = f.read().splitlines()
        for wl in wls:
            if wavelengths[peak] <= (float(wl) + 5) and wavelengths[peak] >= (float(wl) - 5):
                wlpeaks.append(round(wavelengths[peak], 2))
    return wlpeaks


def absorbanceResults(lines):
    absorbances = []
    for line in lines[49:-17]:
        _, ab = line.split("=")
        absorbances.append(float(ab))
    return absorbances

wlresults = wavelengthResults(parseFile("coords.txt"))
absresults = absorbanceResults(parseFile("absorbance.txt"))
cert = calcert(wlresults, absresults, "as")
print(cert[0], cert[1])
