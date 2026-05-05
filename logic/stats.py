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
        wls = result[:5]
        absorbances = result[5:]
        for i, values in enumerate(wls):
            match i:
                case 0:
                    wl1.append(values)
                case 1:
                    wl2.append(values)
                case 2:
                    wl3.append(values)
                case 3:
                    wl4.append(values)
                case 4:
                    wl5.append(values)

        for i, values in enumerate(absorbances):
            match i:
                case 0:
                    abs1.append(values)
                case 1:
                    abs2.append(values)
                case 2:
                    abs3.append(values)
                case 3:
                    abs4.append(values)
                case 4:
                    abs5.append(values)
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
    swl1 = []
    swl2 = []
    swl3 = []
    swl4 = []
    swl5 = []
    sabs1 = []
    sabs2 = []
    sabs3 = []
    sabs4 = []
    sabs5 = []

    for i, report in enumerate(results):
        for result in report:
            match i:
                case 0:
                    temp = []
                    temp.append(result)
                    wl1.append(s.mean(temp))
                    if len(temp) > 1:
                        swl1.append(s.stdev(temp))
                    else:
                        swl1.append(0)
                case 1:
                    temp = []
                    temp.append(result)
                    wl2.append(s.mean(temp))
                    if len(temp) > 1:
                        swl2.append(s.stdev(temp))
                    else:
                        swl2.append(0)
                case 2:
                    temp = []
                    temp.append(result)
                    wl3.append(s.mean(temp))
                    if len(temp) > 1:
                        swl3.append(s.stdev(temp))
                    else:
                        swl3.append(0)
                case 3:
                    temp = []
                    temp.append(result)
                    wl4.append(s.mean(temp))
                    if len(temp) > 1:
                        swl4.append(s.stdev(temp))
                    else:
                        swl4.append(0)
                case 4:
                    temp = []
                    temp.append(result)
                    wl5.append(s.mean(temp))
                    if len(temp) > 1:
                        swl5.append(s.stdev(temp))
                    else:
                        swl5.append(0)
                case 5:
                    temp = []
                    temp.append(result)
                    abs1.append(s.mean(temp))
                    if len(temp) > 1:
                        sabs1.append(s.stdev(temp))
                    else:
                        sabs1.append(0)
                case 6:
                    temp = []
                    temp.append(result)
                    abs2.append(s.mean(temp))
                    if len(temp) > 1:
                        sabs2.append(s.stdev(temp))
                    else:
                        sabs2.append(0)
                case 7:
                    temp = []
                    temp.append(result)
                    abs3.append(s.mean(temp))
                    if len(temp) > 1:
                        sabs3.append(s.stdev(temp))
                    else:
                        sabs3.append(0)    
                case 8:
                    temp = []
                    temp.append(result)
                    abs4.append(s.mean(temp))
                    if len(temp) > 1:
                        sabs4.append(s.stdev(temp))
                    else:
                        sabs4.append(0)
                case 9:
                    temp = []
                    temp.append(result)
                    abs5.append(s.mean(temp))
                    if len(temp) > 1:
                        sabs5.append(s.stdev(temp))
                    else:
                        sabs5.append(0)

    return [wl1, wl2, wl3, wl4, wl5, abs1, abs2, abs3, abs4, abs5, swl1, swl2, swl3, swl4, swl5, sabs1, sabs2, sabs3, sabs4, sabs5]                
