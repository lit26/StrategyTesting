import yfinance as yf

prepost = False

def fetchData(ticker):
    return yf.download(
        tickers=ticker,
        period='2y',
        group_by='ticker',
        auto_adjust=True,
        prepost=prepost,
        progress=False
    )

ticker = 'AAPL'
df = fetchData(ticker)
df.to_csv(f'data/{ticker}.csv')