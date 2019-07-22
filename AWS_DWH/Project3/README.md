**Udacity Project 3: Creating AWS Redshift Data Warehouse**

**Project Overview**

The main goal of this project is to create a data warehouse in the cloud on an AWS Redshift cluster for a music streaming service called Sparkify. The initial situation is that Sparkify wants to map both its song database and the data of its users completely in ETL processes in the cloud. The song and user data are stored in Amazon S3 memory, in directories with JSON logs.
My approach to implementation was as follows:
1.	I first created a Redshift cluster.
2.	Next, I built an ETL pipeline that reads the data from the JSON logs and then fills the database. Data is extracted from the S3 and converted into the fact and dimension tables of the star schema.
3.	For a better processing speed, the order of the data was defined with sort keys.


**Setup**

To execute the ETL process, the following prerequisites must be met:
1. dwh.cfg must contain login data for an active AWS Redshift cluster.
2. an ARN must be present in dwh.cfg
3. the IAM role associated with the ARN must have access to the S3



**As soon as the prerequisites are fulfilled, the following steps must be carried out:**

1. execute sql_queries.py (terminal or Python console)
2. run create_tables.py (terminal or Python console)
3. running etl.py (terminal or Python console)


**Description of the data**

The database represented in the Star Schema file consists of five tables. The fact table Songplays contains the individual songplay events. In addition to the fact table, there are four other dimension tables. These contain the normalized data of the users, artists, songs and timestamps.

