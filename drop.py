import pandas as pd

def drop(df,timelag):
	for i in range(timelag):
		df.drop(df.index[0],inplace=True)

timelag = 90
with open('All_tokens.txt','r') as file:
	for line in file:
		segments = line.split()
		token = segments[0]
		df = pd.read_csv(token+'_timelag_'+str(timelag)+'d'+'.csv',encoding ='utf-8',index_col = 'Date',skipinitialspace=True)
		drop(df,timelag)
		df.to_csv(token+'_lagged_'+str(timelag)+'d'+'.csv',encoding = 'utf-8')