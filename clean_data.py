from zipline.api import *
from matplotlib import style
import csv
import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Date_template.csv',index_col = ['Date'])
df = df.drop(['Symbol','Open','High','Low','Close','Close_Adj'], 1)

with open('All_tokens.txt','r') as file:
	for line in file:
		segments = line.split()
		token = segments[0]
		try:
			df2 = pd.read_csv(token+'_adj.csv',index_col = ['Date'])
			df2.replace(0,np.nan,inplace=True)
			df2.fillna(method = 'ffill',inplace=True)
			result = df.join( df2, how = 'outer')
			result.index.name = 'Date'
			result.fillna(method = 'ffill',inplace=True)
			result.fillna(method = 'bfill',inplace=True)
			result.drop(['Volumn'] , 1 , inplace=True)
			result.to_csv(token+'_adj_.csv', encoding ='utf-8')
		except:
			pass

'''
df1 = pd.read_csv()
pd.concat()
'''

