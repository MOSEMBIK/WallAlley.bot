from src.assets import assets
import yfinance as yf
import asyncio

async def get_Price(asset):
    if not(asset in assets) :
        return {'response':'ERROR'}
    ticker = yf.Ticker(assets.get(asset))
    tInfo = ticker.info

    data = {}
    data['response'] = '200'
    try :
        data['name'] = tInfo['shortName']
    except :
        data['name'] = tInfo['name']

    try :
        data['symbol'] = tInfo['symbol'].split('-')[0]
    except :
        data['symbol'] = ''

    try :
        data['price'] = "$"+str('%.2f'%(tInfo['regularMarketPrice']))
    except :
        data['price'] = ''

    try :
        data['dchange'] = str('%.2f'%(((tInfo['regularMarketPrice']/tInfo['regularMarketOpen'])-1)*100))+"%"
    except :
        data['dchange'] = ''
    
    return data
    
async def get_Stats(asset):
    if not(asset in assets) :
        return {'response':'ERROR'}
    ticker = yf.Ticker(assets.get(asset))
    tInfo = ticker.info

    data = {}
    data['response'] = '200'
    try :
        data['name'] = tInfo['shortName']
    except :
        try :
            data['name'] = tInfo['name']
        except :
            data['name'] = 'unknown'

    try :
        data['symbol'] = (tInfo['symbol'].split('-'))[0]
    except :
        data['symbol'] = 'unknown'

    try :
        data['sector'] = tInfo['sector']
    except :
        try :
            data['sector'] = tInfo['quoteType'].capitalize()
        except :
            data['sector'] = 'unknown'

    try :
        data['price'] = "$"+str('%.2f'%(tInfo['regularMarketPrice']))
    except :
        data['price'] = 'unknown'

    try :
        data['dchange'] = str('%.2f'%(((tInfo['regularMarketPrice']/tInfo['regularMarketOpen'])-1)*100))+"%"
    except :
        data['dchange'] = 'unknown'

    try :
        data['dhigh'] = "$"+str('%.2f'%(tInfo['regularMarketDayHigh']))
    except :
        data['dhigh'] = 'unknown'

    try :
        data['dlow'] = "$"+str('%.2f'%(tInfo['regularMarketDayLow']))
    except :
        data['dlow'] = 'unknown'
    
    return data
    
