### Prediction
`python -m luigi --module collect_books  DownloadBookData  --local-scheduler`

### Classification

`python -m luigi --module  upload_to_S3_classification  S3UploadClassification  --local-scheduler --aws-access-key-id <your-aws-access-key-id> --aws-secret-access-key <your-aws-secret-access-key>`

Pipeline- To Download data and Process it. Data is downloaded from bitfinex. From two rest api one is books and other is trade api.
The luigi pipline id divided in 3 tasks:
1. DownloadBookData- Data is downloaded from `https://api.bitfinex.com/v1\btc\book\usd`
2. DownloadTradeData -Data is downloaded from `https://api.bitfinex.com/v1\btc\trade\usd` 

Downloaded data is stored in MongoDB

3. DataCleaningAndParsing- Data downloaded from rest api's is in json format. It is parsed to extract revlant fields and stored in processed csv file
4. UploadDataToS3- This task uploads processed file to S3 bucket.

We have used luigi logging, email on error fetaure, configuration file. Also we used multiple workers when running task on ec2 instance for parallel computation.

Screenshots for luigi pipline from luigi interactive interface


