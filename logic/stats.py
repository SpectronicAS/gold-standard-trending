import pandas as pd
import numpy as np
from db.crud import query_values

def get_results():
    results = query_values()
    wl1 = []
    wl2 = []
    wl3 = []
    wl4 = []
    wl5 = []
    abs1 = []
    abs2 = []
    abs3 = []
    abs4 = []
    abs5 = []
    for result in results:
        wls = result[1:5]
        absorbances = result[6:10]
        for i, values in enumerate(wls):
            match i:
                case 0:
                    wl1.append(values.wl1)
                case 1:
                    wl2.append(values.wl2)
                case 2:
                    wl3.append(values.wl3)
                case 3:
                    wl4.append(values.wl4)
                case 4:
                    wl5.append(values.wl5)

        for i, values in enumerate(absorbances):
            match i:
                case 0:
                    abs1.append(values.abs1)
                case 1:
                    abs2.append(values.abs2)
                case 2:
                    abs3.append(values.abs3)
                case 3:
                    abs4.append(values.abs4)
                case 4:
                    abs5.append(values.abs5)

def calc_means():
    