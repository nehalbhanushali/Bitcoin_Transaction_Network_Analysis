import luigi
import os.path
import pandas as pd
import download_accepted_loans
from os import listdir, rmdir, remove
import time
import datetime
class MergeDataDownloaded(luigi.Task):
    def requires(self):
        return download_accepted_loans.DownloadLendingClubDataSet()

    def input(self):
        return luigi.LocalTarget('Data/DOWNLOAD_LOAN_DATA')


    def run(self):
        # end whtever needs to be run

        folder = self.input().path
        print("Started : Prepare download data files for merge")
        df_list = []

        #check inorder to avoid inclusion in merge to be tested to-do $$$$
        mergedFile = self.output().path #check / \\  >> \
        if os.path.exists(mergedFile):
            os.remove(mergedFile) ## just os import required??? to-do $$$$





        for filename in os.listdir(folder):


            df=pd.read_csv(folder + "/"+ filename,skiprows=1,low_memory=False, encoding="utf8")
            ts = time.time()
            date_time = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            df.insert(1, "download_timestamp", date_time)
            half_count = len(df.columns) / 2
            df=df.dropna(axis='columns', how='all')
            df = df.dropna(thresh=half_count)
            df_list.append(df)



        for i in listdir(self.input().path):
            os.remove(folder + "/"+i)
        rmdir(self.input().path)
        combined_csv = pd.concat(df_list)
        combined_csv.to_csv(mergedFile, index=False ) #check / \\ \

#         print("Finished : Merging download data files to CombinedDownloadData.gzip ")

        print("COMBINED DATAFRAME HEAD :: ",combined_csv.head())

    def output(self):
        #save file to Data directory
        return luigi.LocalTarget('Data/CombinedDownloadData.csv') ## check to-do $$$

# if __name__ == '__main__':
#     luigi.run()
