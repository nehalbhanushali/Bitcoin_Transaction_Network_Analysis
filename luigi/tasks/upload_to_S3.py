import luigi

import handlingMissingValues
from luigi import configuration, s3
from luigi.s3 import S3Target, S3Client

from boto.s3.key import Key
from boto.s3.connection import S3Connection
class UploadDataToS3(luigi.Task):


    aws_access_key_id = luigi.Parameter()

    aws_secret_access_key = luigi.Parameter()

    def requires(self):
        return handlingMissingValues.HandleMissingData()

    def input(self):
        return luigi.LocalTarget('Data/Processed_Accepted.csv')




    def run(self):

        conn=S3Connection(self.aws_access_key_id,self.aws_secret_access_key)


        bucket = conn.create_bucket("team1_lending_club")

        k=Key(bucket)
        k.key = 'Processed_Accepted.csv' # to-do $$$$
        k.set_contents_from_string(self.input().path) # to-do $$$$
        print('uploading to S3')


# if __name__ == "__main__":

#     luigi.run()
