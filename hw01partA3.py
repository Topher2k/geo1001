#-- GEO1001.2020--hw01
#-- Chris Poon
#-- 4395538

from hw01partA1 import readdata
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from plotScatter import pScatter
import pandas as pd

def calcCorrelation(a,b):
    # Step 1 --- remove nan numbers
    a = np.array(a)
    b = np.array(b)
    a = a[~np.isnan(a)]
    b = b[~np.isnan(b)]

    # Step 2 --- interpolate to equal size samples
    a1 = np.interp(np.linspace(0,b.size,b.size),np.linspace(0,a.size,a.size),a)

    # Step 3 --- normalize because variables have different units
    a_normalized = (a1 - a1.mean())/a1.std()
    b_normalized = (b - b.mean())/b.std()

    # Step 4 --- compute statistics
    pcoef,pvps = stats.pearsonr(a_normalized,b_normalized)
    prcoef,pvsp = stats.spearmanr(a_normalized,b_normalized)
    return pcoef,prcoef,pvps,pvsp

def showCorrelation(A,B,C,D,E,vari):
    TD, WS, CwSA, HwSA, TempA, GTemp, WC, RH, HSI, DP, PWBTempA, SP, BP, Alt, DAlt, NAWBTemp, WBGTA, TWL, MD = readdata(A)
    TD, WS, CwSB, HwSB, TempB, GTemp, WC, RH, HSI, DP, PWBTempB, SP, BP, Alt, DAlt, NAWBTemp, WBGTB, TWL, MD = readdata(B)
    TD, WS, CwSC, HwSC, TempC, GTemp, WC, RH, HSI, DP, PWBTempC, SP, BP, Alt, DAlt, NAWBTemp, WBGTC, TWL, MD = readdata(C)
    TD, WS, CwSD, HwSD, TempD, GTemp, WC, RH, HSI, DP, PWBTempD, SP, BP, Alt, DAlt, NAWBTemp, WBGTD, TWL, MD = readdata(D)
    TD, WS, CwSE, HwSE, TempE, GTemp, WC, RH, HSI, DP, PWBTempE, SP, BP, Alt, DAlt, NAWBTemp, WBGTE, TWL, MD = readdata(E)
    
    if vari == 'T':
        D = [TempA,TempB,TempC,TempD,TempE]
    elif vari == 'WBGT':
        D = [WBGTA,WBGTB,WBGTC,WBGTD,WBGTE]
    elif vari == 'CwS':
        D = [CwSA,CwSB,CwSC,CwSD,CwSD,CwSE]
    
    a = np.zeros((5,5))
    b = np.zeros((5,5))
    c = np.zeros((5,5))
    d = np.zeros((5,5))
    for i in range(5):
        for j in range(5):
            a[i][j],b[i][j],c[i][j],d[i][j] = calcCorrelation(D[i],D[j])
    if vari == 'T':
        B = 'Temperature'
    elif vari == 'WBGT':
        B = 'Wet Bulb Globe Temperature'
    elif vari == 'CwS':
        B = 'Crosswind Speed'
    print("\nPearson's coefficients for",B)
    print(a)
    print("\nSpearmann's coefficients for",B)
    print(b)

def plotScatter(A,B,C,D,E,vari):
    TD, WS, CwSA, HwSA, TempA, GTemp, WC, RH, HSI, DP, PWBTempA, SP, BP, Alt, DAlt, NAWBTemp, WBGTA, TWL, MD = readdata(A)
    TD, WS, CwSB, HwSB, TempB, GTemp, WC, RH, HSI, DP, PWBTempB, SP, BP, Alt, DAlt, NAWBTemp, WBGTB, TWL, MD = readdata(B)
    TD, WS, CwSC, HwSC, TempC, GTemp, WC, RH, HSI, DP, PWBTempC, SP, BP, Alt, DAlt, NAWBTemp, WBGTC, TWL, MD = readdata(C)
    TD, WS, CwSD, HwSD, TempD, GTemp, WC, RH, HSI, DP, PWBTempD, SP, BP, Alt, DAlt, NAWBTemp, WBGTD, TWL, MD = readdata(D)
    TD, WS, CwSE, HwSE, TempE, GTemp, WC, RH, HSI, DP, PWBTempE, SP, BP, Alt, DAlt, NAWBTemp, WBGTE, TWL, MD = readdata(E)
    
    if vari == 'T':
        D = [TempA,TempB,TempC,TempD,TempE]
    elif vari == 'WBGT':
        D = [WBGTA,WBGTB,WBGTC,WBGTD,WBGTE]
    elif vari == 'CwS':
        D = [CwSA,CwSB,CwSC,CwSD,CwSD,CwSE]

    fig = plt.figure(figsize=(14,5))
    ax1 = plt.subplot(251)
    ax2 = plt.subplot(252)
    ax3 = plt.subplot(253)
    ax4 = plt.subplot(254)
    ax5 = plt.subplot(255)
    ax6 = plt.subplot(256)
    ax7 = plt.subplot(257)
    ax8 = plt.subplot(258)
    ax9 = plt.subplot(259)
    ax10 = plt.subplot(2,5,10)
    axes = [ax1,ax2,ax3,ax4,ax5,ax6,ax7,ax8,ax9,ax10]
    X = ['A','B','C','D','E']
    a = 0
    if vari == 'T':
        vname = 'Temperature'
    elif vari == 'WBGT':
        vname = 'WBGT'
    elif vari == 'CwS':
        vname = 'Crosswind Speed'
    #fig.suptitle('Scatter plots of ' + vname + ' values between sensors')
    for i in range(5):
        for j in range(i+1,5):
            dat = pScatter(D[i],D[j])
            axes[a].scatter(dat,D[j],c='b',s=0.2)
            axes[a].set_xlabel(vname + "(Sensor "+X[i]+")")
            axes[a].set_ylabel(vname + "(Sensor " + X[j] + ")")
            a = a+1
    plt.tight_layout()
    plt.show()