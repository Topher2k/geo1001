# geo1001

# geo1001_hw01.py
geo1001_hw01.py is the main file to run the code.
It includes specifying the path location of the datasets.
And calls the functions that are needed for each part of the assignment.

By default the functions are all 'turned on', put hashtag in front of the functions to 'turn it off' to avoid flooding the terminal with data and opening all the figures at once.

# hw01partA1.py
Code for hw01 part A1.

isfloat() turns the given value into a float.

readdata() reads the data from the given path location of the datasets and returns the data in the form of a list for each of the senors variable.

mean_stats() prints the mean, variance and standard deviation for each of the sensors variables of the given dataset.

plotTempHistogram() plots Temperature histograms of all the given datasets, the last argument determines the amount of bins that is used.

plotTempPoligons() plots Temperature frequency poligons of all the given datasets in 1 plot.

plotBoxplot() plots boxplots of all the given datasets, the last argument determines of which variable the boxplot are made. Options are 'WS' for Wind Speed, 'Temp' for Temperature and 'WD' for Wind Direction.

# hw01partA2.py
Code for hw01 part A2

plotPmf() plots the PMFs for the 5 sensors Temperature values.

plotCdf() plots the CDFs for the 5 sensors, the second to last argument determines the variable of the CDFs. Options are 'T' for Temperature and 'WS' for Wind Speed. The last argument determines the amount of bins that is used.

plotPdf() plots the PDFs for the 5 sensors Temperature values.

plotWSPdfkde() plots the PDF and kernel density estimation for the 5 sensors Wind Speed values. The last argument determines the amount of bins that is used.

# hw01partA3.py
Code for hw01 part A3

calcCorrelation() removes the nan numbers first, then interpolate size samples of the given datasets, normalizes both datasets and lastly computes the correlation of the two datasets using the Pearson's and Spearmann's rank coefficients.

showCorrelation() prints the correlation between the 5 sensors in a table, the last argument determines the variable that is used. Options are 'T' for Temperature, 'WBGT' for Wet Bulb Globe Temperature and 'CwS' for the Crosswind Speed.

plotScatter() plots the scatter plots for the 5 sensors correlations, the last argument determines the variable that is used. Options are 'T' for Temperature, 'WBGT' for Wet Bulb Globe Temperature and 'CwS' for the Crosswind Speed.

# hw01partA4.py
Code for hw01 part A4

calcCi() computes and prints the 95% confidence intervals, the last argument determines the variable that is used. Options are 'T' for Temperature and 'WS' for Wind Speed.

hypothesisTest() performs the hypothesis tests prints the results for the two given sensors, the last argument determines the variable that is used. Options are 'T' for Temperature and 'WS' for Wind Speed.
