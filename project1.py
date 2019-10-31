


# import libraries 

import numpy as np
import pandas as pd
#import tensorflow as tf
import matplotlib.pyplot as plt
import strptime
import calendar
#load dataset from excel file (.csv)

#dataset = pd.read_csv('power_meter.csv')
#df1 = dataset[['read_dt']]
#df2 = dataset[['read_tm']]
#dfcombine = df1 + df2


#Removing E columns and plotting the months by the Billed Usage
NYSEGdataset = pd.read_csv('NYSEG.csv')
#NYSEGdataset=NYSEGdataset.dropna(axis=0) 
NYSEGdataset.shape() 
NYSEGdataset=NYSEGdataset[NYSEGdataset['A or E?'] != 'E']
NYSEGdataset.shape() 


    
#NYSEGdataset.plot(x='Date',y='Billed Usage')
NYSEGdataset.info()
NYSEGdataset['Date'] = pd.to_datetime(NYSEGdataset['Date'], format='%B %d, %Y')
NYSEGdataset.info()
NYSEGdataset['Month'] = pd.DatetimeIndex(NYSEGdataset['Date']).month
NYSEGdataset['Month'] = NYSEGdataset['Month'].astype('int')
NYSEGdataset['Month'] = NYSEGdataset['Month'].apply(lambda x: calendar.month_name[x])

#look_up = {'1': 'Jan', '2': 'Feb', '3': 'Mar', '4': 'Apr', '5': 'May',
           # '6': 'Jun', '7': 'Jul', '8': 'Aug', '9': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}

#NYSEGdataset['Month'] = NYSEGdataset['Month'].apply(lambda x: look_up[x])

#NYSEGdataset['Month'] = NYSEGdataset['Month'].apply(lambda x: strptime(x,'%b').tm_mon) 
NYSEGdataset.head()
NYSEGdataset.plot(x='Month', y='Billed Usage',kind = 'scatter')


NYSEGdataset.boxplot(column=["Billed Usage"])

NYSEGdataset["Billed Usage"].mean()
NYSEGdataset["Billed Usage"].max()
NYSEGdataset["Billed Usage"].min()



#months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']









# show the first few rows of the dataset, you can add numbers of rows Ex: dataset.head(40) #40 rows

#dataset.head()
# shape of the dataset (Rows,cols) 

#dataset.shape 
#dataset.columns
#dataset['Date'].mean