#-- GEO1001.2020--hw01
#-- Chris Poon
#-- 4395538

import xlrd                                     # Reading an excel file using Python 
import numpy as np
import matplotlib.pyplot as plt

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

def readdata(loc):
    wb = xlrd.open_workbook(loc) 
    sheet = wb.sheet_by_index(0) 

    TD = []                                     # 1.  True Direction
    WS = []                                     # 2.  Wind Speed (m/s)
    CwS = []                                    # 3.  Crosswind Speed (m/s)
    HwS = []                                    # 4.  Headwind Speed (m/s)
    Temp = []                                   # 5.  Temperature (degrees celsius)
    GTemp = []                                  # 6.  Globe Temperature (degrees celsius)
    WC = []                                     # 7.  Wind Chill (degrees celsius)
    RH = []                                     # 8.  Relative Humidity (%)
    HSI = []                                    # 9.  Heat Stress Index (degrees celsius)
    DP = []                                     # 10. Dew Point (degrees celsius)
    PWBTemp = []                                # 11. Psychro Wet Bulb Temperature (degrees celsius)
    SP = []                                     # 12. Station Press (mb)
    BP = []                                     # 13. Barometric Pressure (mb)
    Alt = []                                    # 14. Altitude (m)
    DAlt = []                                   # 15. Density Altitude (m)
    NAWBTemp = []                               # 16. NA Wet Bulb Temperature (degrees celsius)
    WBGT = []                                   # 17. WBGT (degrees celsius)
    TWL = []                                    # 18. TWL (w/m^2)
    MD = []                                     # 19. Mag Direction (degrees)

    for i in range(sheet.nrows):
        if isfloat(sheet.cell_value(i,1)) and i >= 5:
            TD.append(float(sheet.cell_value(i,1)))
        if isfloat(sheet.cell_value(i,2)) and i >= 5:
            WS.append(float(sheet.cell_value(i,2)))
        if isfloat(sheet.cell_value(i,3)) and i >= 5:
            CwS.append(float(sheet.cell_value(i,3)))
        if isfloat(sheet.cell_value(i,4)) and i >= 5:
            HwS.append(float(sheet.cell_value(i,4)))
        if isfloat(sheet.cell_value(i,5)) and i >= 5:
            Temp.append(float(sheet.cell_value(i,5)))
        if isfloat(sheet.cell_value(i,6)) and i >= 5:
            GTemp.append(float(sheet.cell_value(i,6)))
        if isfloat(sheet.cell_value(i,7)) and i >= 5:
            WC.append(float(sheet.cell_value(i,7)))
        if isfloat(sheet.cell_value(i,8)) and i >= 5:
            RH.append(float(sheet.cell_value(i,8)))
        if isfloat(sheet.cell_value(i,9)) and i >= 5:
            HSI.append(float(sheet.cell_value(i,9)))
        if isfloat(sheet.cell_value(i,10)) and i >= 5:
            DP.append(float(sheet.cell_value(i,10)))
        if isfloat(sheet.cell_value(i,11)) and i >= 5:
            PWBTemp.append(float(sheet.cell_value(i,11)))
        if isfloat(sheet.cell_value(i,12)) and i >= 5:
            SP.append(float(sheet.cell_value(i,12)))
        if isfloat(sheet.cell_value(i,13)) and i >= 5:
            BP.append(float(sheet.cell_value(i,13)))
        if isfloat(sheet.cell_value(i,14)) and i >= 5:
            Alt.append(float(sheet.cell_value(i,14)))
        if isfloat(sheet.cell_value(i,15)) and i >= 5:
            DAlt.append(float(sheet.cell_value(i,15)))
        if isfloat(sheet.cell_value(i,16)) and i >= 5:
            NAWBTemp.append(float(sheet.cell_value(i,16)))
        if isfloat(sheet.cell_value(i,17)) and i >= 5:
            WBGT.append(float(sheet.cell_value(i,17)))
        if isfloat(sheet.cell_value(i,18)) and i >= 5:
            TWL.append(float(sheet.cell_value(i,18)))
        if isfloat(sheet.cell_value(i,19)) and i >= 5:
            MD.append(float(sheet.cell_value(i,19)))

    TD = np.array(TD)
    WS = np.array(WS)
    CwS = np.array(CwS)
    HwS = np.array(HwS)
    Temp = np.array(Temp)
    GTemp = np.array(GTemp)
    WC = np.array(WC)
    RH = np.array(RH)
    HSI = np.array(HSI)
    DP = np.array(DP)
    PWBTemp = np.array(PWBTemp)
    SP = np.array(SP)
    BP = np.array(BP)
    Alt = np.array(Alt)
    DAlt = np.array(DAlt)
    NAWBTemp = np.array(NAWBTemp)
    WBGT = np.array(WBGT)
    TWL = np.array(TWL)
    MD = np.array(MD)

    return TD,WS,CwS,HwS,Temp,GTemp,WC,RH,HSI,DP,PWBTemp,SP,BP,Alt,DAlt,NAWBTemp,WBGT,TWL,MD

def mean_stats(loc):
    TD, WS, CwS, HwS, Temp, GTemp, WC, RH, HSI, DP, PWBTemp, SP, BP, Alt, DAlt, NAWBTemp, WBGT, TWL, MD = readdata(loc)

    print('True Direction:\nMean = ' + str(TD.mean()) + '\nVar = ' + str(TD.var()) + '\nSTD = ' + str(TD.std()))
    print('Wind Speed:\nMean = ' + str(WS.mean()) + '\nVar = ' + str(WS.var()) + '\nSTD = ' + str(WS.std()))
    print('Crosswind Speed:\nMean = ' + str(CwS.mean()) + '\nVar = ' + str(CwS.var()) + '\nSTD = ' + str(CwS.std()))
    print('Headwind Speed:\nMean = ' + str(HwS.mean()) + '\nVar = ' + str(HwS.var()) + '\nSTD = ' + str(HwS.std()))
    print('Temperature:\nMean = ' + str(Temp.mean()) + '\nVar = ' + str(Temp.var()) + '\nSTD = ' + str(Temp.std()))
    print('Globe Temperature:\nMean = ' + str(GTemp.mean()) + '\nVar = ' + str(GTemp.var()) + '\nSTD = ' + str(GTemp.std()))
    print('Wind Chill:\nMean = ' + str(WC.mean()) + '\nVar = ' + str(WC.var()) + '\nSTD = ' + str(WC.std()))
    print('Relative Humidity:\nMean = ' + str(RH.mean()) + '\nVar = ' + str(RH.var()) + '\nSTD = ' + str(RH.std()))
    print('Heat Stress Index:\nMean = ' + str(HSI.mean()) + '\nVar = ' + str(HSI.var()) + '\nSTD = ' + str(HSI.std()))
    print('Dew Point:\nMean = ' + str(DP.mean()) + '\nVar = ' + str(DP.var()) + '\nSTD = ' + str(DP.std()))
    print('Psychro Wet Bulb Temperature:\nMean = ' + str(PWBTemp.mean()) + '\nVar = ' + str(PWBTemp.var()) + '\nSTD = ' + str(PWBTemp.std()))
    print('Station Press:\nMean = ' + str(SP.mean()) + '\nVar = ' + str(SP.var()) + '\nSTD = ' + str(SP.std()))
    print('Barometric Pressure:\nMean = ' + str(BP.mean()) + '\nVar = ' + str(BP.var()) + '\nSTD = ' + str(BP.std()))
    print('Altitude:\nMean = ' + str(Alt.mean()) + '\nVar = ' + str(Alt.var()) + '\nSTD = ' + str(Alt.std()))
    print('Density Altitude:\nMean = ' + str(DAlt.mean()) + '\nVar = ' + str(DAlt.var()) + '\nSTD = ' + str(DAlt.std()))
    print('NA Wet Bulb Temperature:\nMean = ' + str(NAWBTemp.mean()) + '\nVar = ' + str(NAWBTemp.var()) + '\nSTD = ' + str(NAWBTemp.std()))
    print('WBGT:\nMean = ' + str(WBGT.mean()) + '\nVar = ' + str(WBGT.var()) + '\nSTD = ' + str(WBGT.std()))
    print('TWL:\nMean = ' + str(TWL.mean()) + '\nVar = ' + str(TWL.var()) + '\nSTD = ' + str(TWL.std()))
    print('Mag Direction:\nMean = ' + str(MD.mean()) + '\nVar = ' + str(MD.var()) + '\nSTD = ' + str(MD.std()))

def plotTempHistogram(A,B,C,D,E,n):
    TD, WS, CwS, HwS, TempA, GTemp, WC, RH, HSI, DP, PWBTemp, SP, BP, Alt, DAlt, NAWBTemp, WBGT, TWL, MD = readdata(A)
    TD, WS, CwS, HwS, TempB, GTemp, WC, RH, HSI, DP, PWBTemp, SP, BP, Alt, DAlt, NAWBTemp, WBGT, TWL, MD = readdata(B)
    TD, WS, CwS, HwS, TempC, GTemp, WC, RH, HSI, DP, PWBTemp, SP, BP, Alt, DAlt, NAWBTemp, WBGT, TWL, MD = readdata(C)
    TD, WS, CwS, HwS, TempD, GTemp, WC, RH, HSI, DP, PWBTemp, SP, BP, Alt, DAlt, NAWBTemp, WBGT, TWL, MD = readdata(D)
    TD, WS, CwS, HwS, TempE, GTemp, WC, RH, HSI, DP, PWBTemp, SP, BP, Alt, DAlt, NAWBTemp, WBGT, TWL, MD = readdata(E)

    fig = plt.figure(figsize=(15,10))
    ax1 = fig.add_subplot(231)
    ax2 = fig.add_subplot(232)
    ax3 = fig.add_subplot(233)
    ax4 = fig.add_subplot(234)
    ax5 = fig.add_subplot(235)
    ax1.hist(x=TempA, bins=n, color='b', alpha=0.7, rwidth=0.85)
    ax1.set_ylabel('Frequency')
    ax1.set_xlabel('Temperature [\N{DEGREE SIGN}C]\nSensor A')
    ax2.hist(x=TempB, bins=n, color='b', alpha=0.7, rwidth=0.85)
    ax2.set_ylabel('Frequency')
    ax2.set_xlabel('Temperature [\N{DEGREE SIGN}C]\nSensor B')
    ax3.hist(x=TempC, bins=n, color='b', alpha=0.7, rwidth=0.85)
    ax3.set_ylabel('Frequency')
    ax3.set_xlabel('Temperature [\N{DEGREE SIGN}C]\nSensor C')
    ax4.hist(x=TempD, bins=n, color='b', alpha=0.7, rwidth=0.85)
    ax4.set_ylabel('Frequency')
    ax4.set_xlabel('Temperature [\N{DEGREE SIGN}C]\nSensor D')
    ax5.hist(x=TempE, bins=n, color='b', alpha=0.7, rwidth=0.85)
    ax5.set_ylabel('Frequency')
    ax5.set_xlabel('Temperature [\N{DEGREE SIGN}C]\nSensor E')
    #fig.suptitle('Histograms for 5 sensors Temperature values')
    plt.subplots_adjust(wspace=0.5)
    plt.subplots_adjust(hspace=0.5)
    plt.show()

def plotTempPoligons(A,B,C,D,E):
    TD, WS, CwS, HwS, TempA, GTemp, WC, RH, HSI, DP, PWBTemp, SP, BP, Alt, DAlt, NAWBTemp, WBGT, TWL, MD = readdata(A)
    TD, WS, CwS, HwS, TempB, GTemp, WC, RH, HSI, DP, PWBTemp, SP, BP, Alt, DAlt, NAWBTemp, WBGT, TWL, MD = readdata(B)
    TD, WS, CwS, HwS, TempC, GTemp, WC, RH, HSI, DP, PWBTemp, SP, BP, Alt, DAlt, NAWBTemp, WBGT, TWL, MD = readdata(C)
    TD, WS, CwS, HwS, TempD, GTemp, WC, RH, HSI, DP, PWBTemp, SP, BP, Alt, DAlt, NAWBTemp, WBGT, TWL, MD = readdata(D)
    TD, WS, CwS, HwS, TempE, GTemp, WC, RH, HSI, DP, PWBTemp, SP, BP, Alt, DAlt, NAWBTemp, WBGT, TWL, MD = readdata(E)

    plt.figure(figsize=(14,5))
    [frequency1, bins1] = np.histogram(TempA, bins=50)
    [frequency2, bins2] = np.histogram(TempB, bins=50)
    [frequency3, bins3] = np.histogram(TempC, bins=50)
    [frequency4, bins4] = np.histogram(TempD, bins=50)
    [frequency5, bins5] = np.histogram(TempE, bins=50)
    plt.plot(bins1[:-1], frequency1, label='Sensor A')
    plt.plot(bins2[:-1], frequency2, label='Sensor B')
    plt.plot(bins3[:-1], frequency3, label='Sensor C')
    plt.plot(bins4[:-1], frequency4, label='Sensor D')
    plt.plot(bins5[:-1], frequency5, label='Sensor E')
    plt.ylabel('Frequency')
    plt.xlabel('Temperature [\N{DEGREE SIGN}C]')
    plt.legend(loc='best')
    #plt.title('Frequency poligons for the 5 sensors Temperature values')
    plt.show()

def plotBoxplot(A,B,C,D,E,vari):
    TDA, WSA, CwS, HwS, TempA, GTemp, WC, RH, HSI, DP, PWBTemp, SP, BP, Alt, DAlt, NAWBTemp, WBGT, TWL, MD = readdata(A)
    TDB, WSB, CwS, HwS, TempB, GTemp, WC, RH, HSI, DP, PWBTemp, SP, BP, Alt, DAlt, NAWBTemp, WBGT, TWL, MD = readdata(B)
    TDC, WSC, CwS, HwS, TempC, GTemp, WC, RH, HSI, DP, PWBTemp, SP, BP, Alt, DAlt, NAWBTemp, WBGT, TWL, MD = readdata(C)
    TDD, WSD, CwS, HwS, TempD, GTemp, WC, RH, HSI, DP, PWBTemp, SP, BP, Alt, DAlt, NAWBTemp, WBGT, TWL, MD = readdata(D)
    TDE, WSE, CwS, HwS, TempE, GTemp, WC, RH, HSI, DP, PWBTemp, SP, BP, Alt, DAlt, NAWBTemp, WBGT, TWL, MD = readdata(E)

    fig,axes = plt.subplots(1, 5,figsize=(14,5))
    ax1, ax2, ax3, ax4, ax5 = axes.ravel()
    if vari == 'WS':
        ax1.boxplot(WSA, showmeans=True)
        ax2.boxplot(WSB, showmeans=True)
        ax3.boxplot(WSC, showmeans=True)
        ax4.boxplot(WSD, showmeans=True)
        ax5.boxplot(WSE, showmeans=True)
        ax1.set_ylabel('Wind speed [m/s]')
        #fig.suptitle("5 sensors boxplot for Wind speed")
    if vari == 'Temp':
        ax1.boxplot(TempA, showmeans=True)
        ax2.boxplot(TempB, showmeans=True)
        ax3.boxplot(TempC, showmeans=True)
        ax4.boxplot(TempD, showmeans=True)
        ax5.boxplot(TempE, showmeans=True)
        ax1.set_ylabel('Temperature [\N{DEGREE SIGN}C]')
        #fig.suptitle("5 sensors boxplot for Temperature")
    if vari == 'WD':
        ax1.boxplot(TDA, showmeans=True)
        ax2.boxplot(TDB, showmeans=True)
        ax3.boxplot(TDC, showmeans=True)
        ax4.boxplot(TDD, showmeans=True)
        ax5.boxplot(TDE, showmeans=True)
        ax1.set_ylabel('Wind direction [\N{DEGREE SIGN}]')
        #fig.suptitle("5 sensors boxplot for Wind direction")
    plt.subplots_adjust(wspace=0.5)
    plt.subplots_adjust(hspace=0.5)
    plt.show()