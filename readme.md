# Recommendation System for shopping website


## Data Source 

While the user is browsing the website, we 

here we will user 

### Batch Layer:

S3 Bucket (Data Landing Zone): All raw data (historical/batch) can be dumped into an S3 bucket. This serves as the data lake's raw zone.

#### AWS Glue:

ETL: Use Glue ETL jobs to clean, transform, and prepare the raw data. This processed data can be saved back to a different location in S3, which can be termed the processed zone of our data lake.
Crawler: Use the Glue Crawler to explore and catalog the processed data so it's discoverable and usable.
Data Catalog: This serves as a central repository for metadata about the datasets. It assists in querying the data using SQL-based tools and provides schema information.

### Speed (Stream) Layer:

#### Amazon Kinesis Data Streams: Capture real-time user activity data.

#### Amazon EMR: Use EMR to process data from Kinesis Streams. With EMR's powerful distributed data processing capabilities, we can analyze and transform the streaming data.

Combine the streaming data with the batch data. While EMR can directly access data in S3 (thanks to EMRFS, an EMR feature), we'd often perform joins between the recent streaming data and historical data to create enriched datasets.
Serving Layer:

#### S3 Bucket (Processed Data Zone): Once EMR processes and combines the data, store the resultant enriched dataset back to the S3 bucket's processed zone.

Access & Query: Use tools like Amazon Athena or Redshift Spectrum to directly query and analyze the enriched data in S3. This is where the combined insights from both batch and stream data can be made available to business users, analysts, or other applications.

#### Feedback Loop:

As we generate recommendations or insights based on the combined data, we may also want to introduce a feedback mechanism. For instance, users' reactions to recommendations can be captured in real-time, fed back into the system, and used to refine future recommendations.
