# -*- coding: utf-8 -*-
"""Alert_Density.py

# Reading in Data & Libraries
"""

import numpy as np
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
import os

cardinalC_df = pd.read_csv('CardinalC_All.csv')
cardinalD_df = pd.read_csv('CardinalD_All.csv') #CHANGE FILE NAME TO CORRESPONDING FILES
westland_df = pd.read_csv('Westland_All.csv')
ashford_df = pd.read_csv('Ashford_All.csv')


#all_df = all_df.drop(columns = ['ID', 'Event Type', 'Latitude', 'Longitude', 'MIN', 'Clear','Threat Level'])
#all_df = all_df.dropna()
cardinalC_df = cardinalC_df.drop(columns = ['ID', 'Event Type', 'Latitude', 'Longitude', 'MIN', 'Clear','Threat Level'])
cardinalC_df = cardinalC_df.dropna()
cardinalD_df = cardinalD_df.drop(columns = ['ID', 'Event Type', 'Latitude', 'Longitude', 'MIN', 'Clear','Threat Level'])
cardinalD_df = cardinalD_df.dropna()
westland_df = westland_df.drop(columns = ['ID', 'Event Type', 'Latitude', 'Longitude', 'MIN', 'Clear','Threat Level'])
westland_df = westland_df.dropna()
ashford_df = ashford_df.drop(columns = ['ID', 'Event Type', 'Latitude', 'Longitude', 'MIN', 'Clear','Threat Level'])
ashford_df = ashford_df.dropna()

all_df = pd.concat([cardinalC_df,cardinalD_df, ashford_df, westland_df])

"""# Cleaning Dataframes"""

#Cleaning Date & Time Values

char_remove = ["(",")","'",","]

for x in char_remove:
  westland_df['Clear Time'] = westland_df['Clear Time'].str.replace(x,"")
  westland_df['Clear Date'] = westland_df['Clear Date'].str.replace(x,"")
  ashford_df['Clear Time'] = ashford_df['Clear Time'].str.replace(x,"")
  ashford_df['Clear Date'] = ashford_df['Clear Date'].str.replace(x,"")
  cardinalD_df['Clear Time'] = cardinalD_df['Clear Time'].str.replace(x,"")
  cardinalD_df['Clear Date'] = cardinalD_df['Clear Date'].str.replace(x,"")
  cardinalC_df['Clear Time'] = cardinalC_df['Clear Time'].str.replace(x,"")
  cardinalC_df['Clear Date'] = cardinalC_df['Clear Date'].str.replace(x,"")
  all_df['Clear Time'] = all_df['Clear Time'].str.replace(x,"")
  all_df['Clear Date'] = all_df['Clear Date'].str.replace(x,"")



def datetime(df):

  #Functionality: Converts 4 date & time columns to two DateTime columns
  #Asssumes: 4 Columns, 2 clean dates, 2 clean times

  df['Date Time' ] = df['Date'] + " " +  df['Time']
  df['Clear Date Time' ] = df['Clear Date'] + " " +  df['Clear Time']

  df['Date Time'] = pd.to_datetime(df['Date Time'], errors='coerce')
  df['Clear Date Time'] = pd.to_datetime(df['Clear Date Time'], errors='coerce')

datetime(all_df)
datetime(cardinalC_df)
datetime(cardinalD_df)
datetime(westland_df)
datetime(ashford_df)

"""# Calculating Alert Density"""

def alert_density (df):
  assign_to = []
  df["hour_integer"] = df["Date Time"].dt.round("H").dt.hour
  assign_to = df["hour_integer"].value_counts()
  assign_to = assign_to.reindex(range(23+1), fill_value= 0)
  assign_to = assign_to.sort_index()
  assign_to = assign_to.values.tolist()
  print(assign_to)
  return assign_to

cd_Data = alert_density(cardinalD_df)
cc_Data = alert_density(cardinalC_df)
a_Data = alert_density(ashford_df)
w_Data = alert_density(westland_df)

"""# Plotting Results"""

import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

labels = ['0', '1', '2', '3', '4','5','6','7','8','9',
          '10','11','12','13','14','15','16','17','18','19','20','21','22','23']

plt.xticks(range(len(a_Data)), labels)
plt.xlabel('Hour')
plt.ylabel('Alerts')
plt.title('Ashford Density')
plt.bar(range(len(a_Data)), a_Data)
plt.show()

plt.xticks(range(len(cc_Data)), labels)
plt.xlabel('Hour')
plt.ylabel('Alerts')
plt.title('Cardinal C Density')
plt.bar(range(len(cc_Data)), cc_Data)
plt.show()

plt.xticks(range(len(cd_Data)), labels)
plt.xlabel('Hour')
plt.ylabel('Alerts')
plt.title('Cardinal D Density')
plt.bar(range(len(cd_Data)), cd_Data)
plt.show()

plt.xticks(range(len(w_Data)), labels)
plt.xlabel('Hour')
plt.ylabel('Alerts')
plt.title('Westland Density')
plt.bar(range(len(w_Data)), w_Data)
plt.show()
