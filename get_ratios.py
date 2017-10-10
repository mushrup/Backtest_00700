import urllib2
import html2text
import re
import os
import requests
import pandas as pd
import csv
import numpy as np

#http://financials.morningstar.com/ajax/ReportProcess4CSV.html?t=00005&reportType=is&period=12&dataType=A&order=asc&columnYear=5&number=3
#curl http://financials.morningstar.com/ajax/ReportProcess4CSV.html?t=00005&reportType=is&period=12&dataType=A&order=asc&columnYear=5&number=3 > Chicago.csv

def get_morningstar(index):
  url = "http://financials.morningstar.com/ajax/ReportProcess4CSV.html?t="+index+"&reportType=is&period=12&dataType=A&order=asc&columnYear=5&number=3"
  r = requests.get(url)
  file = open(index+"_ratios_raw.csv",'w')
  file.write(r.content)
  file.close()

def remove_header(name):
    with open(name+'_ratios_raw.csv','r') as f:
      with open(name+"_ratios.csv",'w') as f1:
          f.next() # skip header line
          for line in f:
              f1.write(line)
    os.system('rm '+name+'_ratios_raw.csv')


df = pd.DataFrame(pd.io.parsers.read_csv('Token_template.csv', dtype = {'Symbol':str}))
df.set_index('Symbol', inplace=True)

for index, row in df.iterrows():
  get_morningstar(index)
  try:
    remove_header(index)
  except:
    pass