import pandas as pd
import numpy as np
from db.crud import query_values
import statistics as s

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
    return [wl1, wl2, wl3, wl4, wl5, abs1, abs2, abs3, abs4, abs5]

def calc_stats(results):
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
    length = len(results[0])

    for i, report in enumerate(results):
        for result in report:
            match i:
                case 0:
                    temp = []
                    temp.append(result)
                    wl1.append(s.mean(temp))
                case 1:
                    temp = []
                    temp.append(result)
                    wl2.append(s.mean(temp))
                case 2:
                    temp = []
                    temp.append(result)
                    wl3.append(s.mean(temp))
                case 3:
                    temp = []
                    temp.append(result)
                    wl4.append(s.mean(temp))
                case 4:
                    temp = []
                    temp.append(result)
                    wl5.append(s.mean(temp))
                case 5:
                    temp = []
                    temp.append(result)
                    abs1.append(s.mean(temp))
                case 6:
                    temp = []
                    temp.append(result)
                    abs2.append(s.mean(temp))
                case 7:
                    temp = []
                    temp.append(result)
                    abs3.append(s.mean(temp))
                case 8:
                    temp = []
                    temp.append(result)
                    abs4.append(s.mean(temp))
                case 9:
                    temp = []
                    temp.append(result)
                    abs5.append(s.mean(temp))                
