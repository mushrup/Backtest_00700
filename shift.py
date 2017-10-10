import pandas as pd

def shift(df,timedelta):
	try:
		df.Advertising_and_promotion = df.Advertising_and_promotion.shift(timedelta)
	except:
		pass
	try:
		df.Nonrecurring_expense = df.Nonrecurring_expense.shift(timedelta)
	except:
		pass
	try:
		df.Other_assets = df.Other_assets.shift(timedelta)
	except:
		pass
	try:
		df.Other_expense = df.Other_expense.shift(timedelta)
	except:
		pass
	try:
		df.Total_interest_expense = df.Total_interest_expense.shift(timedelta)
	except:
		pass
	try:
		df.Net_interest_income = df.Net_interest_income.shift(timedelta)
	except:
		pass
	try:
		df.Commissions_and_fees = df.Commissions_and_fees.shift(timedelta)
	except:
		pass
	try:
		df.Principal_transactions = df.Principal_transactions.shift(timedelta)
	except:
		pass
	try:
		df.Securities_gains__losses_ = df.Securities_gains__losses_.shift(timedelta)
	except:
		pass
	try:
		df.Credit_card_income = df.Credit_card_income.shift(timedelta)
	except:
		pass
	try:
		df.Insurance_premium = df.Insurance_premium.shift(timedelta)
	except:
		pass
	try:
		df.Income__loss__from_cont_ops_before_taxes = df.Income__loss__from_cont_ops_before_taxes.shift(timedelta)
	except:
		pass
	try:
		df.Total_Provision__benefit__for_taxes = df.Total_Provision__benefit__for_taxes.shift(timedelta)
	except:
		pass
	try:
		df.Provision__benefit__for_taxes = df.Provision__benefit__for_taxes.shift(timedelta)
	except:
		pass
	try:
		df.Total_Weighted_average_shares_outstanding = df.Total_Weighted_average_shares_outstanding.shift(timedelta)
	except:
		pass
	try:
		df.Total_Other_income__expense_ = df.Total_Other_income__expense_.shift(timedelta)
	except:
		pass
	try:
		df.Total_Net_income = df.Total_Net_income.shift(timedelta)
	except:
		pass
	try:
		df.Total_nonoperating_income__net = df.Total_nonoperating_income__net.shift(timedelta)
	except:
		pass
	try:
		df.Other_income__expense__1 = df.Other_income__expense__1.shift(timedelta)
	except:
		pass
	try:
		df.Total_Preferred_dividend = df.Total_Preferred_dividend.shift(timedelta)
	except:
		pass
	try:
		df.Total_noninterest_expenses = df.Total_noninterest_expenses.shift(timedelta)
	except:
		pass
	try:
		df.Net_income_available_to_common_shareholders = df.Net_income_available_to_common_shareholders.shift(timedelta)
	except:
		pass
	try:
		df.Other_income = df.Other_income.shift(timedelta)
	except:
		pass
	try:
		df.Total_noninterest_revenue = df.Total_noninterest_revenue.shift(timedelta)
	except:
		pass
	try:
		df.Total_net_revenue = df.Total_net_revenue.shift(timedelta)
	except:
		pass
	try:
		df.Provisions_for_credit_losses = df.Provisions_for_credit_losses.shift(timedelta)
	except:
		pass
	try:
		df.Compensation_and_benefits = df.Compensation_and_benefits.shift(timedelta)
	except:
		pass
	try:
		df.Tech__communication_and_equipment = df.Tech__communication_and_equipment.shift(timedelta)
	except:
		pass
	try:
		df.Amortization_of_intangibles = df.Amortization_of_intangibles.shift(timedelta)
	except:
		pass
	try:
		df.Other_special_charges = df.Other_special_charges.shift(timedelta)
	except:
		pass
	try:
		df.Other_expenses = df.Other_expenses.shift(timedelta)
	except:
		pass
	try:
		df.Total_expenses = df.Total_expenses.shift(timedelta)
	except:
		pass
	try:
		df.Revenue = df.Revenue.shift(timedelta)
	except:
		pass
	try:
		df.Total_interest_income = df.Other_expense.shift(timedelta)
	except:
		pass
	try:
		df.Basic_1 = df.Basic_1.shift(timedelta)
	except:
		pass
	try:
		df.Diluted_1 = df.Diluted_1.shift(timedelta)
	except:
		pass
	try:
		df.Net_income = df.Net_income.shift(timedelta)
	except:
		pass
	try:
		df.Earnings_per_share = df.Earnings_per_share.shift(timedelta)
	except:
		pass
	try:
		df.Basic = df.Basic.shift(timedelta)
	except:
		pass
	try:
		df.Diluted = df.Diluted.shift(timedelta)
	except:
		pass
	try:
		df.Research_and_development = df.Research_and_development.shift(timedelta)
	except:
		pass
	try:
		df.Cost_of_revenue = df.Cost_of_revenue.shift(timedelta)
	except:
		pass
	try:
		df.Gross_profit = df.Gross_profit.shift(timedelta)
	except:
		pass
	try:
		df.Operating_expenses = df.Operating_expenses.shift(timedelta)
	except:
		pass
	try:
		df.Other_operating_expenses = df.Other_operating_expenses.shift(timedelta)
	except:
		pass
	try:
		df.Interest_income = df.Interest_income.shift(timedelta)
	except:
		pass
	try:
		df.Net_income_from_continuing_operations = df.Net_income_from_continuing_operations.shift(timedelta)
	except:
		pass
	try:
		df.Net_interest_income = df.Net_interest_income.shift(timedelta)
	except:
		pass
	try:
		df.Total_net_revenue = df.Total_net_revenue.shift(timedelta)
	except:
		pass
	try:
		df.Sales__General_and_administrative = df.Sales__General_and_administrative.shift(timedelta)
	except:
		pass
	try:
		df.Total_operating_expenses = df.Total_operating_expenses.shift(timedelta)
	except:
		pass
	try:
		df.Operating_income = df.Operating_income.shift(timedelta)
	except:
		pass
	try:
		df.Interest_Expense = df.Interest_Expense.shift(timedelta)
	except:
		pass
	try:
		df.Interest_expense = df.Interest_expense.shift(timedelta)
	except:
		pass
	try:
		df.Interest_expenses = df.Interest_expenses.shift(timedelta)
	except:
		pass
	try:
		df.Other_income__expense_ = df.Other_income__expense_.shift(timedelta)
	except:
		pass
	try:
		df.Income_before_taxes = df.Income_before_taxes.shift(timedelta)
	except:
		pass
	try:
		df.Income_before_income_taxes = df.Income_before_income_taxes.shift(timedelta)
	except:
		pass
	try:
		df.Provision_for_income_taxes = df.Provision_for_income_taxes.shift(timedelta)
	except:
		pass
	try:
		df.Expenses = df.Expenses.shift(timedelta)
	except:
		pass
	try:
		df.EBITDA = df.EBITDA.shift(timedelta)
	except:
		pass

def drop(df):
	df.drop('Diluted',1,inplace=True)
	df.drop('Basic',1,inplace=True)
	try:
		df.drop('Other',1,inplace=True)
		df.drop('Basic_1',1,inplace=True)
		df.drop('Diluted_1',1,inplace=True)
	except:
		pass

timelag = 90
with open('All_tokens.txt','r') as file:
	for line in file:
		segments = line.split()
		token = segments[0]
		df = pd.read_csv(token+'_ratios_adj.csv',encoding ='utf-8',index_col = 'Date',skipinitialspace=True)
		df.columns = [c.replace(' ', '_') for c in df.columns]
		df.columns = [c.replace('(', '_') for c in df.columns]
		df.columns = [c.replace(')', '_') for c in df.columns]
		df.columns = [c.replace('.', '_') for c in df.columns]
		df.columns = [c.replace(',', '_') for c in df.columns]
		shift(df,timelag)
		drop(df)
		df.to_csv(token+'_timelag_'+str(timelag)+'d'+'.csv',encoding = 'utf-8')











