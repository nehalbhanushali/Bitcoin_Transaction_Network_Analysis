import urllib2
import time
import json
from pymongo import MongoClient
import sys
import luigi

class DownloadBookData(luigi.Task):

    def run(self):


        api = 'https://api.bitfinex.com/v1'
        symbol = 'btc'
        limit = 50
        book_url = '{0}/book/{1}usd?limit_bids={2}&limit_asks={2}'\
            .format(api, symbol, limit)

        client = MongoClient()
        db = client['bitmicro']
        ltc_books = db[symbol+'_books']


        def format_book_entry(entry):
            '''
            Converts book data to float
            '''
            if all(key in entry for key in ('amount', 'price', 'timestamp')):
                entry['amount'] = float(entry['amount'])
                entry['price'] = float(entry['price'])
                entry['timestamp'] = float(entry['timestamp'])
            return entry


        def get_json(url):
            '''
            Gets json from the API
            '''
            resp = urllib2.urlopen(url)
            return json.load(resp, object_hook=format_book_entry), resp.getcode()


        print ('Running...')
        for i in range(10):
            start = time.time()
            try:
                book, code = get_json(book_url)
            except Exception as e:
                print (e)
                sys.exc_clear()
            else:
                if code != 200:
                    print code
                else:
                    book['_id'] = time.time()
                    print('book',book)
                    ltc_books.insert_one(book)
                    time_delta = time.time()-start
                    if time_delta < 1.0:
                        time.sleep(1-time_delta)
