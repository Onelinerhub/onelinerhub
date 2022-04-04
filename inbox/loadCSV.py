import pandas as pd
# Open the csv file
fname = open('wholesale-trade-survey-dec-2021-quarter-csv.csv')
# Reading the csv file using panda's read_csv method
tradeSurvey = pd.read_csv(fname) 
print(tradeSurvey)
