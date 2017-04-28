import luigi

import pandas as pd
import numpy as np
import os

class DownloadBlockchainAPIFeatures(luigi.Task):


    def run(self):

        # end whtever needs to be run
        print("Started : Creating directory for download data")
        #Create dir for download
        # path = "DATA/DOWNLOAD_BLOCKCHAIN_DATA"


        # try:
        #     if not os.path.exists(path):
        #         os.makedirs(path)
        # except OSError as exception:
        #     if exception.errno != errno.EEXIST:
        #         raise
        print("Finished : Creating directory for download data")

       #constants
        abs_url = "https://blockchain.info/charts/avg-block-size?format=csv&timespan=all"
        avg_blk_size_df = pd.read_csv(abs_url,names = ["time_stamp","avg-block-size"])
        avg_blk_size_df.head()
        avg_blk_size_df['time_stamp'] = pd.to_datetime(avg_blk_size_df["time_stamp"])
        avg_blk_size_df['time_stamp'] = avg_blk_size_df['time_stamp'].dt.strftime("%m/%d/%Y %H:%M:%S")

        download_file_list = ['transaction-fees',
        'total-bitcoins',
        #  'trade-volume',
        'n-unique-addresses',
        'n-transactions-per-block',
        'n-transactions',
        'n-orphaned-blocks',
        'miners-revenue',
        'median-confirmation-time',
        'market-price',
        'market-cap',
        'hash-rate',
        'estimated-transaction-volume-usd',
        'estimated-transaction-volume',
        'difficulty',
        'cost-per-transaction'
                            ]
        #constants
        initial_path = 'https://blockchain.info/charts/'
        trailing_path = '?format=csv&timespan=all'

        base_frame = avg_blk_size_df

        for feature in download_file_list:
            theurl = initial_path+feature+trailing_path
            df = pd.read_csv(theurl, names =["time_stamp",feature])
            df['time_stamp'] = pd.to_datetime(df["time_stamp"])
            df['time_stamp'] = df['time_stamp'].dt.strftime("%m/%d/%Y %H:%M:%S")
        #     df = df.dropna(axis=1)
        #     print(len(df))
            base_frame = pd.merge(df,base_frame, on='time_stamp')
        #     df['time_stamp'] = df['time_stamp'].astype(str)
            # print(len(base_frame))
        #     print(df.head(1))
        #     print(type(df['time_stamp'][0]))
   
            
        base_frame.to_csv("BTC_merged_all_new.csv", index=False)
        print("~~~~~ Merged CSV tail ~~~~~")
        print(base_frame.tail(5))
        
        
        print("Finished : Downloading Blockchain API data")
        print("Started : Prepare additional features")
        print("Adding transaction_to_trade_ratio_D")

        df = base_frame
        df['transaction_to_trade_ratio_D'] = np.where(df['estimated-transaction-volume-usd'] !=0,df['estimated-transaction-volume'] /df['estimated-transaction-volume-usd'],0)
        
        print("Calculating price difference from previous value")
        myarray = np.array(df['market-price'])
        d = np.diff(myarray)
        diff_price = np.insert(d,0,0)

        df['price_diff'] = diff_price.tolist()

        print("Creating Y -1/+1")
        df['up_down_same'] = np.where(df['price_diff'] == 0 ,1,np.where(df['price_diff'] > 0, 1,np.where(df['price_diff'] < 0, -1,np.nan)))

        cols_drop_1 =['price_diff','estimated-transaction-volume-usd','market-price','time_stamp'] 
        print("Drop ",list(cols_drop_1))
        final = df.drop(cols_drop_1, 1)
       
        print("Create CSV for classification")
        final.to_csv("Df_for_Classification.csv")

    def output(self):
    #save file to Data directory
        return luigi.LocalTarget('Df_for_Classification.csv')

# if __name__ == '__main__':
#     luigi.run()
