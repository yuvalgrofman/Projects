import requests
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

myAccessKey = 'd5489368eb76d8e66c23812b4b74ee4f'

def getStockHistory(access_key, symbols, timeInterval = 'eod' ,startDate = 'unspecified' , endDate = 'unspecified'):

    if startDate == 'unspecified' and endDate == 'unspecified':
        return requests.get(('http://api.marketstack.com/v1/{timeInterval}?access_key={access_key}&symbols={symbols}'.format(timeInterval = timeInterval, access_key = access_key, symbols = symbols))).json()

    elif endDate == 'unspecified': 
        return requests.get(('http://api.marketstack.com/v1/{timeInterval}?access_key={access_key}&symbols={symbols}&date_from={startDate}'.format(timeInterval = timeInterval, access_key = access_key, symbols = symbols, startDate = startDate))).json()

    return requests.get(('http://api.marketstack.com/v1/{timeInterval}?access_key={access_key}&symbols={symbols}&date_from={startDate}&date_to={endDate}'.format(timeInterval = timeInterval, access_key = access_key, symbols = symbols, startDate = startDate, endDate = endDate))).json()


def plotStock(access_key, symbol, startDate, endDate = 'unspecified', timeInterval = 'eod' ):

    if endDate == 'unspecified':
        stock_history = getStockHistory(access_key, symbol, timeInterval, startDate) 

    else:     
        stock_history = getStockHistory(access_key, symbol, timeInterval , startDate, endDate) 

    dates = []    
    values = []    

    for stock_data in stock_history['data']:
        dates.append((stock_data['date'].split('T')[0]).replace('-','/'))                        
        values.append(stock_data['close'])    

    x = [dt.datetime.strptime(d,'%Y/%m/%d').date() for d in dates]
    x.reverse()

    y = values 
    y.reverse()    

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m/%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=10))
    plt.plot(x,y)
    plt.gcf().autofmt_xdate()
    plt.show()

plotStock(myAccessKey, 'AMZN', '2021-01-01')


# stock_history = getStockHistory('d5489368eb76d8e66c23812b4b74ee4f','AAPL','eod','2020-05-21', '2020-05-23')

# for stock_data in stock_history['data']:
#     print(stock_data['symbol'])
#     print(stock_data['date'])
#     print(stock_data['high'])