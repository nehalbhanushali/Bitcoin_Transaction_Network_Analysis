`python -m luigi --module merge_accepted_loans MergeDataDownloaded --local-scheduler`

`python3 -m luigi --module download_accepted_loans  DownloadLendingClubDataSet  --local-scheduler`


Pipeline- Accepted and Declined loans
The luigi pipline id divided in 4 tasks:
1. DownloadLendingClubDataSet- Using mechanical soup login happens, then the values from dropdown are extracted to download files. The output is directed using luigi folder.
2. MergeDataDownloaded -The downloaded data is now merged to create a dataframe. Due to memmory constraints on docker the downloaded files once merge are deleted. 
3. HandleMissingData- this luigi task handles missing data and does feture engineering to derive new features. The clean file is saved to disk. The format is gzip due to memory constraints of docker.
4. UploadDataToS3- This task uploads processed file to S3 bucket.


We have used luigi logging, email on error fetaure, configuration file. Also we used multiple workers when running task on ec2 instance for parallel computation.

Screenshots for luigi pipline from luigi interactive interface


