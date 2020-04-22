import requests
import pandas as pd
import schedule
import time
import datetime

def save_data():
	url = 'https://www.vivaenergy.com.au/products/terminal-gate-pricing/current-tgp#'
	html = requests.get(url).content
	df_list = pd.read_html(html)
	df = df_list[-1]
	print(df)
	df.to_csv('my data.csv')
	now = datetime.datetime.now()
	print("The table has been updated at:",now)

schedule.every().day.at("11:34").do(save_data)


while True:
	schedule.run_pending()
	time.sleep(1)