import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.pylab import rcParams
import fetcher as f
import globalvars as gv
import pictobinary as p2b


def plotter():
	f.fetcher()
	rcParams['figure.figsize'] = 20, 10
	df = pd.read_csv(f'{gv.userin}{gv.usercountry}info.csv', parse_dates=True)
	df = df[['Date', 'Close']]
	df.head()
	print(df.dtypes)
	df = df.astype({'Close': float})
	df['Date'] = pd.to_datetime(df['Date'])
	print(df.dtypes)
	df.index = df['Date']
	plt.plot(df['Close'], label=f'{gv.userin} {gv.usercountry} Close Price History')
	plt.savefig(f'{gv.userin}{gv.usercountry}plot')

	df = df.sort_index(ascending=True, axis=0)
	data = pd.DataFrame(index=range(0, len(df)), columns=['Date', 'Close'])
	for i in range(0, len(data)):
		data['Date'][i] = df['Date'][i]
		data['Close'][i] = df['Close'][i]
	data.head()

	data.index = data['Date']
	data.drop('Date', axis=1, inplace=True)


def main():
	plotter()
	p2b.main()


if __name__ == '__main__':
	main()
