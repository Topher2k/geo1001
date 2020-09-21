#-- GEO1001.2020--hw01
#-- Chris Poon
#-- 4395538

from hw01partA1 import mean_stats
from hw01partA1 import readdata
from hw01partA1 import plotTempHistogram
from hw01partA1 import plotTempPoligons
from hw01partA1 import plotBoxplot
from hw01partA2 import plotPmf
from hw01partA2 import plotPdf
from hw01partA2 import plotCdf
from hw01partA2 import plotWSPdfkde
from hw01partA3 import showCorrelation
from hw01partA3 import plotScatter
from hw01partA4 import calcCi
from hw01partA4 import hypothesisTest

# Give the locations of the datafiles
#Local
A = '/Users/chris/Desktop/MSc Geomatics/GEO1001/geo1001.2020-master/data_hw01/HEAT - A_final.xls'
B = '/Users/chris/Desktop/MSc Geomatics/GEO1001/geo1001.2020-master/data_hw01/HEAT - B_final.xls'
C = '/Users/chris/Desktop/MSc Geomatics/GEO1001/geo1001.2020-master/data_hw01/HEAT - C_final.xls'
D = '/Users/chris/Desktop/MSc Geomatics/GEO1001/geo1001.2020-master/data_hw01/HEAT - D_final.xls'
E = '/Users/chris/Desktop/MSc Geomatics/GEO1001/geo1001.2020-master/data_hw01/HEAT - E_final.xls'

#Universal
#A = '../data_hw01/HEAT - A_final.xls'
#B = '../data_hw01/HEAT - B_final.xls'
#C = '../data_hw01/HEAT - C_final.xls'
#D = '../data_hw01/HEAT - D_final.xls'
#E = '../data_hw01/HEAT - E_final.xls'

#A1.1 - Compute mean statistics (mean, variance and standard deviation for each of the sensors variables), what do you observe from the results?

#mean_stats(A)
#mean_stats(B)
#mean_stats(C)
#mean_stats(D)
#mean_stats(E)

#A1.2 - Create 1 plot that contains histograms for the 5 sensors Temperature values. Compare histograms with 5 and 50 bins, why is the number of bins important?

#plotTempHistogram(A,B,C,D,E,5)      #5 bins
#plotTempHistogram(A,B,C,D,E,50)     #50 bins

#A1.3 - Create 1 plot where frequency poligons for the 5 sensors Temperature values overlap in different colors with a legend.

#plotTempPoligons(A,B,C,D,E)

#A1.4 - Generate 3 plots that include the 5 sensors boxplot for: Wind Speed, Wind Direction and Temperature.

#plotBoxplot(A,B,C,D,E,'WS')         #Wind Speed
#plotBoxplot(A,B,C,D,E,'WD')         #Wind Direction (True Direction)
#plotBoxplot(A,B,C,D,E,'Temp')       #Temperature

#A2.1 - Plot PMF, PDF and CDF for the 5 sensors Temperature values in independent plots (or subplots).
#       Describe the behaviour of the distributions, are they all similar? what about their tails?

#plotPmf(A,B,C,D,E,50)
#plotPdf(A,B,C,D,E)
#plotCdf(A,B,C,D,E,'T',50)

#A2.2 - For the Wind Speed values, plot the pdf and the kernel density estimation. Comment the differences.

#plotWSPdfkde(A,B,C,D,E,20)

#A3.1 - Compute the correlations between all the sensors for the variables: Temperature, Wet Bulb Globe Temperature (WBGT), Crosswind Speed.
#       Perform correlation between sensors with the same variable, not between two different variables;
#       for example, correlate Temperature time series between sensor A and B. Use Pearson’s and Spearmann’s rank coefficients.
#       Make a scatter plot with both coefficients with the 3 variables.

#showCorrelation(A,B,C,D,E,'T')
#showCorrelation(A,B,C,D,E,'WBGT')
#showCorrelation(A,B,C,D,E,'CwS')
#plotScatter(A,B,C,D,E,'T')
#plotScatter(A,B,C,D,E,'WBGT')
#plotScatter(A,B,C,D,E,'CwS')

#A3.2 - What can you say about the sensors’ correlations?
#A3.3 - If we told you that that the sensors are located as follows, hypothesize which location would you assign to each sensor and reason your hypothesis using the correlations. 

#A4.1 - Plot the CDF for all the sensors and for variables Temperature and Wind Speed,
#       then compute the 95% confidence intervals for variables Temperature and Wind Speed for all the sensors and save them in a table (txt or csv form).

#plotCdf(A,B,C,D,E,'T',50)
#plotCdf(A,B,C,D,E,'WS',50)
#calcCi(A,B,C,D,E,'T')
#calcCi(A,B,C,D,E,'WS')

#A4.2 - Test the hypothesis: the time series for Temperature and Wind Speed are the same for sensors:
#           1) E, D;

#print('For Sensor E and D:')
#hypothesisTest(E,D,'T')
#hypothesisTest(E,D,'WS')

#           2) D, C;

#print('For Sensor D and C:')
#hypothesisTest(D,C,'T')
#hypothesisTest(D,C,'WS')

#           3) C, B;

#print('For Sensor C and B:')
#hypothesisTest(C,B,'T')
#hypothesisTest(C,B,'WS')

#           4) B, A.

#print('For Sensor B and A:')
#hypothesisTest(B,A,'T')
#hypothesisTest(B,A,'WS')

#A4.3 - What could you conclude from the p-values?