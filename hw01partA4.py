#-- GEO1001.2020--hw01
#-- Chris Poon
#-- 4395538

from hw01partA1 import readdata
import numpy as np
import scipy.stats
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd

def calcCi(A,B,C,D,E,vari):
    TD, WSA, CwS, HwS, TempA, GTemp, WC, RH, HSI, DP, PWBTemp, SP, BP, Alt, DAlt, NAWBTemp, WBGT, TWL, MD = readdata(A)
    TD, WSB, CwS, HwS, TempB, GTemp, WC, RH, HSI, DP, PWBTemp, SP, BP, Alt, DAlt, NAWBTemp, WBGT, TWL, MD = readdata(B)
    TD, WSC, CwS, HwS, TempC, GTemp, WC, RH, HSI, DP, PWBTemp, SP, BP, Alt, DAlt, NAWBTemp, WBGT, TWL, MD = readdata(C)
    TD, WSD, CwS, HwS, TempD, GTemp, WC, RH, HSI, DP, PWBTemp, SP, BP, Alt, DAlt, NAWBTemp, WBGT, TWL, MD = readdata(D)
    TD, WSE, CwS, HwS, TempE, GTemp, WC, RH, HSI, DP, PWBTemp, SP, BP, Alt, DAlt, NAWBTemp, WBGT, TWL, MD = readdata(E)

    if vari == 'T':
        A = [TempA,TempB,TempC,TempD,TempE]
        print('For Temperature:')
    if vari == 'WS':
        A = [WSA,WSB,WSC,WSD,WSE]
        print('For Windspeed:')
    sensor_list = ['A','B','C','D','E']
    lower_list = []
    upper_list = []
    for i in range(5):
        mu, sigma = np.mean(A[i]), np.std(A[i])
        size = len(A[i])
        lower, upper = scipy.stats.t.interval(0.95, size - 1, mu, sigma)
        lower_list.append(lower)
        upper_list.append(upper)
    intervals_list = pd.DataFrame([sensor_list, lower_list, upper_list]).transpose()
    intervals_list.columns = ['Sensor', 'Lower boundary', 'Upper boundary']
    print(intervals_list)

def hypothesisTest(sensor1,sensor2,vari):
    TD, WS1, CwS, HwS, Temp1, GTemp, WC, RH, HSI, DP, PWBTemp, SP, BP, Alt, DAlt, NAWBTemp, WBGT, TWL, MD = readdata(sensor1)
    TD, WS2, CwS, HwS, Temp2, GTemp, WC, RH, HSI, DP, PWBTemp, SP, BP, Alt, DAlt, NAWBTemp, WBGT, TWL, MD = readdata(sensor2)

    if vari == 'T':
        A = Temp1
        B = Temp2
    elif vari == 'WS':
        A = WS1
        B = WS2

    t,p = stats.ttest_ind(A,B)
    t = abs(t)

    if vari == 'T':
        print('t(Temperature) =',t)
        print('p-value(Temperature) =',p)
    elif vari == 'WS':
        print('t(Wind speed) =', t)
        print('p-value(Wind speed) =', p)