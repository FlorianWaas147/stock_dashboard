# Yahoo recently has become an unstable data source.
# If it gives an error, you may run the cell again, or try yfinance
import pandas as pd
from pandas_datareader import data
# Set the start and end date
start_date = '1990-01-01'
end_date = '2030-05-10'
# Set the ticker
ticker = 'TUI1.DE'
# Get the data
df = data.get_data_yahoo(ticker, start_date, end_date)
df.tail()

import yfinance as yf

msft = yf.Ticker("OMV.DE")

# get stock info
msft.info

# get historical market data
hist = msft.history(period="max")

# show actions (dividends, splits)
msft.actions

# show dividends
msft.dividends

# show splits
msft.splits

# show financials
msft.financials
msft.quarterly_financials

# show major holders
stock.major_holders

# show institutional holders
stock.institutional_holders

# show balance heet
msft.balance_sheet
msft.quarterly_balance_sheet

# show cashflow
msft.cashflow
msft.quarterly_cashflow

# show earnings
msft.earnings
msft.quarterly_earnings

# show sustainability
msft.sustainability

# show analysts recommendations
msft.recommendations

# show next event (earnings, etc)
msft.calendar

# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
msft.isin

# show options expirations
msft.options

# get option chain for specific expiration
opt = msft.option_chain('YYYY-MM-DD')
# data available via: opt.calls, opt.puts

import numpy as np
tmp = pd.Series({'OMV.DE':'OMV', '^DJI':'Dow Jones'})

tmp.loc[tmp.values != 'OMV']
tmp = pd.read_csv('list_of_investments.csv')
tmp.set_index('0')
tmp[]