import os
import pandas as pd

def formatize(individual_name):
	df = pd.DataFrame(pd.read_csv(individual_name,index_col = 1))
	df.index.names = ['Date']
	df.columns = ['Symbol','Open','High','Low','Close','Close_Adj','x','y','z']
	df = df.drop(['x','y','z'], 1)
	return df

file_name = 'All_tokens.txt'
file = open(file_name,'r')
lines = file.read().splitlines() 
for token in lines:
	individual = token+'.csv'
	try:
		df = formatize(individual)
		filename = token+'_adj.csv'
		df.to_csv(filename,encoding='utf-8')
	except:
		pass
	