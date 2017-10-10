import pandas as pd

def add_dummy(df):
	df['Ytd_close'] =  df.Close.shift(1)
	df['OneDayMomentum'] = df['Close'] - df['Ytd_close']
	df['Dummy'] = df['OneDayMomentum'].gt(0)

timelag = 90
with open('All_tokens.txt','r') as file:
	for line in file:
		segments = line.split()
		token = segments[0]
		df = pd.read_csv(token+'_lagged_'+str(timelag)+'d'+'.csv',encoding ='utf-8',index_col = 'Date',skipinitialspace=True)
		add_dummy(df)
		df.to_csv(token+'_\wdummy.csv',encoding = 'utf-8')