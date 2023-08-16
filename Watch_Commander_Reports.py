# -*- coding: utf-8 -*-
"""Watch_Commander_Data.py

# **Read in Data & Libraries**
"""

import numpy as np
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
import os

cardinal_df = pd.read_csv('Cardinal_March23.csv') #CHANGE FILE NAME TO CORRESPONDING FILES
westland_df = pd.read_csv('Westland_March23.csv')
ashford_df = pd.read_csv('Ashford_March23.csv')
#INSERT WATCH COMMANDER DATA
WC_df = pd.read_csv('WC.csv')

"""# **Number of Alerts Cleared**"""

#Combine Datasets
df = pd.concat([cardinal_df,westland_df, ashford_df])
#Get Rid of Unneccesary Columns
df = df.drop(columns = ['ID', 'Event Type', 'Latitude', 'Longitude', 'MIN', 'Clear','Threat Level'])
df = df.dropna()
WC_df = WC_df.drop(columns = ['Account', 'Position'])
WC_df = WC_df.dropna()
#Leaving Only Commander ID for Comments
df['Comments'] = df['Comments'].str.replace('\D', '', regex=True)


#Unique Values In Comments = All Watch Commander IDs
all_IDs = df.Comments.unique()
dictionary ={}
for i in all_IDs:
  x = df.loc[df['Comments']== i]
  dictionary[i] = x #Dictionary with Key: User ID and Value: DF of every alert cleared

for i in all_IDs:
  print("User {} Cleared {} Alerts".format(i,len(dictionary[i])))
  #THIS IS NUMBER OF TOTAL ALERTS CLEARED

"""# **Average Response Time**



"""

#Formatting Date and Time


df['Clear Date'] = df['Clear Date'].str.replace(r"(","")
df['Clear Date'] = df['Clear Date'].str.replace(r")","")
df['Clear Date'] = df['Clear Date'].str.replace(r"'","")
df['Clear Date'] = df['Clear Date'].str.replace(r",","")

df['Clear Time'] = df['Clear Time'] .str.replace(r"(","")
df['Clear Time'] = df['Clear Time'] .str.replace(r")","")
df['Clear Time'] = df['Clear Time'] .str.replace(r"'","")
df['Clear Time']  = df['Clear Time'] .str.replace(r",","")

def datetime(df):

  #Functionality: Converts 4 date & time columns to two DateTime columns
  #Asssumes: 4 Columns, 2 clean dates, 2 clean times

  df['Date Time' ] = df['Date'] + " " +  df['Time']
  df['Clear Date Time' ] = df['Clear Date'] + " " +  df['Clear Time']

  df['Date Time'] = pd.to_datetime(df['Date Time'], errors='coerce')
  df['Clear Date Time'] = pd.to_datetime(df['Clear Date Time'], errors='coerce')

datetime(df)


def time_passed(df):
  #Functionality: Get Time Difference between Two DF Columns
  #Assumes: Two Datetime formated Columns (see datetime)

  time1 = 'Date Time'
  time2 = 'Clear Date Time'

  df['m'] = (df[time2] - df[time1]).dt.total_seconds() / 60
  df['s'] = (df[time2] - df[time1]).dt.total_seconds()
  df['h'] = (df[time2] - df[time1]).dt.total_seconds() / 60 /60
  df['d'] = (df[time2] - df[time1]).dt.total_seconds() / 60 / 60 / 24
  df['full_d'] = (df[time2] - df[time1]).dt.days

time_passed(df)

#Formatting Previously Made Dictionary
for i in all_IDs:
  dictionary[i]['Clear Date'] = dictionary[i]['Clear Date'].str.replace(r"(","")
  dictionary[i]['Clear Date'] = dictionary[i]['Clear Date'].str.replace(r")","")
  dictionary[i]['Clear Date'] = dictionary[i]['Clear Date'].str.replace(r"'","")
  dictionary[i]['Clear Date'] = dictionary[i]['Clear Date'].str.replace(r",","")

  dictionary[i]['Clear Time'] = dictionary[i]['Clear Time'] .str.replace(r"(","")
  dictionary[i]['Clear Time'] = dictionary[i]['Clear Time'] .str.replace(r")","")
  dictionary[i]['Clear Time'] = dictionary[i]['Clear Time'] .str.replace(r"'","")
  dictionary[i]['Clear Time']  = dictionary[i]['Clear Time'] .str.replace(r",","")

  datetime(dictionary[i])
  time_passed(dictionary[i])

for i in all_IDs:
  mean = dictionary[i]['m'].mean()
  print("User {} Cleared Responses with an Average Time Of: {:.2f}".format(i,mean))
  #TOTAL AVERAGE RESPONSE TIME

#CLEANING THE WATCH COMMANDER DATA
def datetime(df):

  #Functionality: Converts 4 date & time columns to two DateTime columns
  #Asssumes: 4 Columns, 2 clean dates, 2 clean times

  df['Clock-In Date Time' ] = df['Start Date'] + " " +  df['Clocked-In']
  df['Clock-Out Date Time' ] = df['End Date'] + " " +  df['Clockout']

  df['Clock-In Date Time'] = pd.to_datetime(df['Clock-In Date Time'], errors='coerce')
  df['Clock-Out Date Time'] = pd.to_datetime(df['Clock-Out Date Time'], errors='coerce')

datetime(WC_df)
WC_df

#CREATES A DATA FRAME FOR EACH WATCH COMMANDER WITH THEIR PERSONAL ALERTS
#Note: Likely wont accuratley represent 9158 & 8235 as their hours are client specific, this does not account for this as
df_9169 = pd.DataFrame(columns = ["Date", "Time", "Sector Name","Clear Date", "Clear Time", "Sign-off Name", "Comments", "Date Time", "Clear Date Time", "m", "s", "h", "d", "full_d"])
df_7732 = pd.DataFrame(columns = ["Date", "Time", "Sector Name","Clear Date", "Clear Time", "Sign-off Name", "Comments", "Date Time", "Clear Date Time", "m", "s", "h", "d", "full_d"])
df_9162 = pd.DataFrame(columns = ["Date", "Time", "Sector Name","Clear Date", "Clear Time", "Sign-off Name", "Comments", "Date Time", "Clear Date Time", "m", "s", "h", "d", "full_d"])
df_9168 = pd.DataFrame(columns = ["Date", "Time", "Sector Name","Clear Date", "Clear Time", "Sign-off Name", "Comments", "Date Time", "Clear Date Time", "m", "s", "h", "d", "full_d"])
df_8235 = pd.DataFrame(columns = ["Date", "Time", "Sector Name","Clear Date", "Clear Time", "Sign-off Name", "Comments", "Date Time", "Clear Date Time", "m", "s", "h", "d", "full_d"])
df_9133 = pd.DataFrame(columns = ["Date", "Time", "Sector Name","Clear Date", "Clear Time", "Sign-off Name", "Comments", "Date Time", "Clear Date Time", "m", "s", "h", "d", "full_d"])
 # df_9158 = pd.DataFrame(columns = ["Date", "Time", "Sector Name","Clear Date", "Clear Time", "Sign-off Name", "Comments", "Date Time", "Clear Date Time", "m", "s", "h", "d", "full_d"])
x = 0
while x <= 82:
  start_date = WC_df['Clock-In Date Time'][x]
  end_date = WC_df['Clock-Out Date Time'][x]
  print(WC_df['Eid'][x])
  if WC_df['Eid'][x] == 9169:
    df_9169 = pd.concat([df_9169, df.loc[(df['Date Time'] > start_date) & (df['Date Time'] < end_date)]])
  if WC_df['Eid'][x] == 7732:
    df_7732 = pd.concat([df_7732, df.loc[(df['Date Time'] > start_date) & (df['Date Time'] < end_date)]])
  if WC_df['Eid'][x] == 9162:
    df_9162 = pd.concat([df_9162, df.loc[(df['Date Time'] > start_date) & (df['Date Time'] < end_date)]])
  if WC_df['Eid'][x] == 9168:
    df_9168 = pd.concat([df_9168, df.loc[(df['Date Time'] > start_date) & (df['Date Time'] < end_date)]])
  if WC_df['Eid'][x] == 8235:
    df_8235 = pd.concat([df_8235, df.loc[(df['Date Time'] > start_date) & (df['Date Time'] < end_date)]])
  if WC_df['Eid'][x] == 9133:
    df_9133 = pd.concat([df_9133, df.loc[(df['Date Time'] > start_date) & (df['Date Time'] < end_date)]])
  # if WC_df['Eid'][x] != 9169 and WC_df['Eid'][x] != 7732 and WC_df['Eid'][x] != 9162 and WC_df['Eid'][x] != 9168 and WC_df['Eid'][x] != 8235 and WC_df['Eid'][x] != 9133:
    # df_9158 = pd.concat([df_9158, df.loc[(df['Date Time'] > start_date) & (df['Date Time'] < end_date)]])
  x+=1

print("Average Response Time During Shift ")
print(" Commander 9169: {:.2f}  ".format(df_9169['m'].mean()))
print(" Commander 7732: {:.2f}  ".format(df_7732['m'].mean()))
print(" Commander 9162: {:.2f}  ".format(df_9162['m'].mean()))
print(" Commander 9168: {:.2f}  ".format(df_9168['m'].mean()))
print(" Commander 9133: {:.2f}  ".format(df_9133['m'].mean()))
print(" Commander 8235: {:.2f}  ".format(df_8235['m'].mean()))

"""# **Response Time by Minute**"""

for i in all_IDs:
  df = dictionary[i]
  within_5 = df.loc[df['m'] <= 5]
  within_10 = df.loc[(df['m'] <= 10) & (df['m'] > 5)]
  within_15 = df.loc[(df['m'] <= 15) & (df['m'] > 10)]
  within_30 = df.loc[(df['m'] <= 30) & (df['m'] > 15)]
  over_30 = df.loc[(df['m'] > 30)]

  all_alerts = [within_5,within_10,within_15,within_30,over_30]
  Number_Cleared = []
  Percentage = []

  for t in all_alerts:
    Number_Cleared.append(len(t.index))

  for m in Number_Cleared:
    Percentage.append(100*(m/sum(Number_Cleared)))

  #TABLE
  if i == '9158':
    None
  else:
    print("Number of Alerts Cleared...{}".format(i))
    print("  Within 5 Minutes: {} ({:.2f}%)".format(Number_Cleared[0], Percentage[0]))
    print("  Within 10 Minutes: {} ({:.2f}%)".format(Number_Cleared[1], Percentage[1]))
    print("  Within 15 Minutes: {} ({:.2f}%)".format(Number_Cleared[2], Percentage[2]))
    print("  Within 30 Minutes: {} ({:.2f}%)".format(Number_Cleared[3], Percentage[3]))
    print("  Over 30 Minutes: {} ({:.2f}%)".format(Number_Cleared[4], Percentage[4]))
    print("Total Number of Cleared Alerts: {}".format(sum(Number_Cleared)))
    print(" ")
    print("-----------------------------------------------------------------------------")

within_5 = df_9169.loc[df_9169['m'] <= 5]
within_10 = df_9169.loc[(df_9169['m'] <= 10) & (df_9169['m'] > 5)]
within_15 = df_9169.loc[(df_9169['m'] <= 15) & (df_9169['m'] > 10)]
within_30 = df_9169.loc[(df_9169['m'] <= 30) & (df_9169['m'] > 15)]
over_30 = df_9169.loc[(df_9169['m'] > 30)]

print(within_5.shape)
print(within_10.shape)
print(within_15.shape)
print(within_30.shape)
print(over_30.shape)

within_5 = df_7732.loc[df_7732['m'] <= 5]
within_10 = df_7732.loc[(df_7732['m'] <= 10) & (df_7732['m'] > 5)]
within_15 = df_7732.loc[(df_7732['m'] <= 15) & (df_7732['m'] > 10)]
within_30 = df_7732.loc[(df_7732['m'] <= 30) & (df_7732['m'] > 15)]
over_30 = df_7732.loc[(df_7732['m'] > 30)]

print(within_5.shape)
print(within_10.shape)
print(within_15.shape)
print(within_30.shape)
print(over_30.shape)

within_5 = df_9162.loc[df_9162['m'] <= 5]
within_10 = df_9162.loc[(df_9162['m'] <= 10) & (df_9162['m'] > 5)]
within_15 = df_9162.loc[(df_9162['m'] <= 15) & (df_9162['m'] > 10)]
within_30 = df_9162.loc[(df_9162['m'] <= 30) & (df_9162['m'] > 15)]
over_30 = df_9162.loc[(df_9162['m'] > 30)]

print(within_5.shape)
print(within_10.shape)
print(within_15.shape)
print(within_30.shape)
print(over_30.shape)

within_5 = df_9168.loc[df_9168['m'] <= 5]
within_10 = df_9168.loc[(df_9168['m'] <= 10) & (df_9168['m'] > 5)]
within_15 = df_9168.loc[(df_9168['m'] <= 15) & (df_9168['m'] > 10)]
within_30 = df_9168.loc[(df_9168['m'] <= 30) & (df_9168['m'] > 15)]
over_30 = df_9168.loc[(df_9168['m'] > 30)]

print(within_5.shape)
print(within_10.shape)
print(within_15.shape)
print(within_30.shape)
print(over_30.shape)

import numpy as np
import matplotlib.pyplot as plt

#THE PLOT

category_names = ['Within 5 Minutes', 'Within 10 Minutes',
                  'Within 15 Minutes', 'Within 30 Minutes', 'Over 30 Minutes']
results = {
    'Total Alerts Cleared': [99,52,34,56,177],
    'Alerts Cleared During a Shift': [110,57,36,54,151]
    #MUST MANUALLY INPUT DATA HERE ACCORDING TO ABOVE RESULTS
}



def survey(results, category_names):

    labels = list(results.keys())
    data = np.array(list(results.values()))
    data_cum = data.cumsum(axis=1)
    category_colors = ['indianred', 'coral','mediumvioletred','peachpuff','lightseagreen'] #plt.colormaps['RdYlGn'](
        #np.linspace(0.15, 0.85, data.shape[1]))

    fig, ax = plt.subplots(figsize=(9.2, 3))
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.sum(data, axis=1).max())

    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        rects = ax.barh(labels, widths, left=starts, height=0.5,
                        label=colname, color=color)


        text_color ='white'
        ax.bar_label(rects, label_type='center', color=text_color)
    ax.legend(ncols=len(category_names), bbox_to_anchor=(0, 1),
              loc='lower left', fontsize='small')

    return fig, ax


survey(results, category_names)
plt.show()
