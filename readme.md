# Recommendation System for shopping website

## Data we need for the system.

Using Collaborative-filtering and Content-based recommending system, we will need the following atrribute. 

### Data Collection:

#### 1. User Data:
Collect comprehensive details about our users to understand their preferences and behaviors.

- **Demographics**: 
  - `Age`
  - `Gender`
  - `Location`
  - `Occupation`
  - `Education Level`

- **User Behavior**:
  - `Browsing History`
  - `Search Queries`
  - `Time Spent on Site`
  - `Frequency of Visits`

- **User Preferences**:
  - `Product Categories Frequently Browsed`
  - `Wish Lists`
  - `Alerts & Notifications Set`
  - `Feedback and Reviews Given`

- **Purchase History**:
  - `Items Purchased`
  - `Frequency of Purchases`
  - `Average Purchase Value`
  - `Return History`

#### 2. Item Data:
Details about the products or services to understand their attributes and categories. 

- **Basic Information**:
  - `Item ID`
  - `Name/Title`
  - `Description`
  - `Price`
  - `Image`

- **Categorical Information**:
  - `Category`
  - `Sub-Category`
  - `Brand`
  - `Manufacturer`

- **Item Attributes**:
  - `Color`
  - `Size`
  - `Material`
  - `Usage Instructions`
  - `Warranty Details`

- **Item Ratings and Reviews**:
  - `Average Rating`
  - `Number of Reviews`
  - `Positive/Negative Review Count`

#### 3. User-Item Interaction Data:
Insights into how users interact with specific items, which are critical for building effective recommendation systems.

- **Browsing Data**:
  - `Items Viewed`
  - `Duration of View`
  - `Sequence of Items Browsed`

- **Engagement Data**:
  - `Items Added to Cart`
  - `Items Removed from Cart`
  - `Items Added to Wish List`
  - `Items Shared on Social Media`

- **Purchase Data**:
  - `Items Purchased Together`
  - `Time of Purchase (Seasonality)`
  - `Purchase Method (Online, In-Store, Mobile)`

- **Feedback Data**:
  - `User Ratings for Items`
  - `User Reviews`
  - `Items Marked as "Not Interested"`

 
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

## Data Cleaning and Feature 


## Model building

### Hybrid Recommendation System:
Content-based Filtering:

Uses features of items (like tags, categories, or descriptions) to find similarities and recommend items similar to what the user has previously interacted with.
Implementation:
Extract features from items using techniques like TF-IDF or word embeddings.
Use cosine similarity or other distance metrics to find the similarity between items based on these features.
Collaborative Filtering:

Predicts user preferences based on past behaviors of similar users.
Implementation:
Utilize matrix factorization techniques such as Singular Value Decomposition (SVD) or Alternating Least Squares (ALS).
Knowledge-based Algorithm:

Taps into explicit knowledge about users and items.
Implementation:
Capture explicit user preferences through user profiles or questionnaires.
Use this knowledge to filter and rank items based on a set of predefined rules.
Constructing the Neural Network for the Hybrid Model:
Input Layer: This will contain neurons representing:

Features from the content-based model (item embeddings, item metadata).
Features from the collaborative filtering model (user and item embeddings).
Features from the knowledge-based model (explicit user preferences or rules).
Hidden Layers: Multiple dense layers can be used to capture intricate patterns and interactions between the different recommendation methods.

Output Layer: Represents the likelihood of a user interacting with an item. This could be in the form of scores or probabilities.


## Model deployment 

1. Model Registry:
we will catalog and manage versions of our models.
Register our models, assign them versions, and store metadata about them.
Easily roll back to previous versions if necessary.

2. Deployment:
Amazon SageMaker Endpoints: we will deploy our trained model to a SageMaker real-time endpoint.
Ensure that autoscaling set up to handle varying loads.

3. A/B Testing:
SageMaker allows us to perform A/B testing by deploying multiple models to an endpoint.
Define multiple variants of models. E.g., Variant A uses an older model while Variant B uses the newly trained model.
Allocate a percentage of traffic to each variant. E.g., 90% to Variant A and 10% to Variant B.
Monitor performance metrics for each variant using Amazon CloudWatch.

4. Continuous Integration and Continuous Deployment (CI/CD):
AWS CodePipeline & AWS CodeBuild: Set up a CI/CD pipeline.
Automate model training, evaluation, and deployment when changes are made or new data becomes available.
Incorporate quality gates to ensure only models that meet certain criteria (like a specific accuracy threshold) are deployed.



## Feedback Loop:

As we generate recommendations or insights based on the combined data, we may also want to introduce a feedback mechanism. For instance, users' reactions to recommendations can be captured in real-time, fed back into the system, and used to refine future recommendations.
