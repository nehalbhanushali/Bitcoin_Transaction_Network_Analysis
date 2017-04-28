import urllib2
import time
import json
from pymongo import MongoClient
import sys
import luigi
import collect_books

class DownloadTradeData(luigi.Task):
    def requires(self):
        return collect_books.DownloadBookData()

    def run(self):

        api = 'https://api.bitfinex.com/v1'
        symbol ='btc'
        limit = 5000

        client = MongoClient()
        db = client['bitmicro']
        ltc_trades = db[symbol+'_trades']


        def format_trade(trade):
            '''
            Formats trade data
            '''

            if all(key in trade for key in ('tid', 'amount', 'price', 'timestamp')):

                trade['_id'] = trade.pop('tid')
                trade['amount'] = float(trade['amount'])
                trade['price'] = float(trade['price'])
                trade['timestamp'] = float(trade['timestamp'])

            return trade


        def get_json(url):
            '''
            Gets json from the API
            '''
            resp = urllib2.urlopen(url)
            return json.load(resp, object_hook=format_trade), resp.getcode()


        print 'Running...'
        last_timestamp = 0
        for i in range(10):
            start = time.time()
            url = '{0}/trades/{1}usd?timestamp={2}&limit_trades={3}'\
                .format(api, symbol, last_timestamp, limit)
            #print("the url",url)
            try:
                trades, code = get_json(url)
                print("code",code)
            except Exception as e:
                print e
                sys.exc_clear()
            else:
                if code != 200:
                    print code
                else:
                    for trade in trades:
                        #print("trade is",trade)
                        #print("trade is",ltc_trades)
                        ltc_trades.update_one({'_id': trade['_id']},
                                              {'$setOnInsert': trade}, upsert=True)
                    last_timestamp = trades[0]['timestamp'] - 5
                    time_delta = time.time()-start
                    if time_delta < 1.0:
                        time.sleep(1-time_delta)
