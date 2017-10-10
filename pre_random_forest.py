import urllib2
import html2text
import re
import datetime
import os
import requests
import pandas as pd
import csv
import numpy as np

#http://financials.morningstar.com/ajax/ReportProcess4CSV.html?t=00005&reportType=is&period=12&dataType=A&order=asc&columnYear=5&number=3
#curl http://financials.morningstar.com/ajax/ReportProcess4CSV.html?t=00005&reportType=is&period=12&dataType=A&order=asc&columnYear=5&number=3 > Chicago.csv

def add_close_price(token,date_template):
    
  #try:
  df = pd.read_csv(token+'_adj_.csv',encoding ='utf-8',index_col = 'Date',skipinitialspace=True)
  for index,row in date_template.iterrows():
    try:
      date_template.set_value(index,'Close',df.at[index,'Close'])
      date_template['Symbol'] = token
      # date_template.set_value(index,'Symbol',token)
      date = index
    except:
      pass
    # print date_template
  #except Exception as e:
   # print (1,token,date,e)

def get_ratios(token,date_template):
  try:
    df = pd.read_csv(token+'_ratios.csv',encoding ='utf-8',index_col=0,skipinitialspace=True)
    df.index.name = 'Date'
    df.drop('TTM',1,inplace = True)
    df = df.transpose()

    date_range = pd.date_range('2012-12-31', '2017-09-28')
    df.index = pd.DatetimeIndex(df.index)
    df = df.reindex(date_range, method = 'ffill')
    result = pd.concat([df,date_template], axis=1) 
    result.index = date_template.index
    result.drop(['Close','Symbol'],1,inplace=True)
    result = pd.concat([result,date_template], axis=1)
    result.to_csv(token+'_ratios_adj.csv', encoding = 'utf-8')
  except:
    pass

df = pd.DataFrame(pd.io.parsers.read_csv('Date_template_FDMT.csv',skipinitialspace=True))
df.set_index('Date', inplace=True)
with open('All_tokens.txt','r') as file:
  for line in file:
    segments = line.split()
    token = segments[0]
    add_close_price(token,df)
    get_ratios(token,df)
    


