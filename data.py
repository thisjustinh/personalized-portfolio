import pandas as pd
import numpy as np
from iexfinance.stocks import Stock
from iexfinance.stocks import get_historical_data
from datetime import datetime
from iexfinance.utils.exceptions import IEXAuthenticationError
from bs4 import BeautifulSoup
import requests


def beta(ticker):
    yahoo = requests.get('https://finance.yahoo.com/quote/' + ticker + '?p=' + ticker)
    scraper = BeautifulSoup(yahoo.content, 'html.parser')
    return scraper.findAll(text='Beta (3Y Monthly)')[0].parent.parent.findNext('td').contents[0].contents[0]


def pull_data(ticker):
    stock = Stock(ticker, output_format='pandas')
    f = stock.get_financials()
    stats = stock.get_key_stats()

    eps = stats.loc['ttmEPS'][ticker]
    pe = stats.loc['peRatio'][ticker]
    roe = f.loc[f.index[0], 'netIncome']/f.loc[f.index[0], 'shareholderEquity']
    de = f.loc[f.index[0], 'totalLiabilities']/f.loc[f.index[0], 'shareholderEquity']
    cfps = f.loc[f.index[0], 'cashFlow']/stats.loc['sharesOutstanding', ticker]
    divs = stats.loc['dividendYield', ticker]

    yahoo = requests.get('https://finance.yahoo.com/quote/' + ticker + '?p=' + ticker)
    scraper = BeautifulSoup(yahoo.content, 'html.parser')
    beta = scraper.findAll(text='Beta (3Y Monthly)')[0].parent.parent.findNext('td').contents[0].contents[0]

    df = pd.DataFrame(
        [[eps, pe, roe, de, cfps, divs, beta]],
        index=[ticker],
        columns=['EPS', 'P/E', 'RoE', 'Debt/Equity', 'Cash Flow/Share', 'Div Yield', 'Beta'],
        dtype=float
    )

    return df


def historical_data():
    constituents = pd.read_csv('data.csv').iloc[:, 0]
    hist = pd.DataFrame()
    for i in range(len(constituents)):

        try:
            df = get_historical_data(constituents[i], start=datetime(2017, 2, 23), end=datetime(2018, 2, 23),
                                     output_format='pandas')
            hist[constituents[i]] = df['close']
            print(constituents[i])
        except requests.exceptions.ConnectionError:
            break
        except IEXAuthenticationError:
            break
    hist.to_csv('historical.csv')
    return hist


def sp500():
    constituents = pd.read_csv('constituents.csv').loc[:, 'Symbol'].tolist()
    data = pd.DataFrame(columns=['EPS', 'P/E', 'RoE', 'Debt/Equity', 'Cash Flow/Share', 'Div Yield', 'Beta'])
    for ticker in constituents:
        try:
            data = data.append(pull_data(ticker))
            print(ticker)
        except TypeError:
            continue
        except IEXAuthenticationError:
            continue
        except requests.exceptions.ConnectionError:
            print('Stupid API error }:(')
            break
        except IndexError:
            continue

    return data.to_csv('data.csv')


if __name__ == '__main__':
    # print(beta('BLK'))
    print(pd.read_csv('historical.csv').transpose())
