import luigi

import download_blockchain_api_features
from luigi import configuration, s3
from luigi.s3 import S3Target, S3Client

from boto.s3.key import Key
from boto.s3.connection import S3Connection
class S3UploadClassification(luigi.Task):


    aws_access_key_id = luigi.Parameter()

    aws_secret_access_key = luigi.Parameter()

    def requires(self):
        return download_blockchain_api_features.DownloadBlockchainAPIFeatures()

    def input(self):
        return luigi.LocalTarget('Df_for_Classification.csv')


    def run(self):

        conn=S3Connection(self.aws_access_key_id,self.aws_secret_access_key)

        bucket = conn.create_bucket("team1_bitcoin")

        k=Key(bucket)
        k.key = 'Df_for_Classification.csv' 
        k.set_contents_from_string(self.input().path) 
        print('Success uploading to S3')


# if __name__ == "__main__":

#     luigi.run()
