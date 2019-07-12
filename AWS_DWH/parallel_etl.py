import boto3
import configparser
import matplotlib.pyplot as plt
import pandas as pd
from time import time
import psycopg2


# STEP 1: Get the params of the created redshift cluster
config = configparser.ConfigParser()
config.read_file(open('dwh.cfg'))
KEY=config.get('AWS','key')
SECRET= config.get('AWS','secret')

DWH_DB= config.get("DWH","DWH_DB")
DWH_DB_USER= config.get("DWH","DWH_DB_USER")
DWH_DB_PASSWORD= config.get("DWH","DWH_DB_PASSWORD")
DWH_PORT = config.get("DWH","DWH_PORT")

# FILL IN THE REDSHIFT ENPOINT HERE
# e.g. DWH_ENDPOINT="redshift-cluster-1.csmamz5zxmle.us-west-2.redshift.amazonaws.com"
DWH_ENDPOINT="dwhcluster.c7ytdzszmvzr.us-west-2.redshift.amazonaws.com:5439"

#FILL IN THE IAM ROLE ARN you got in step 2.2 of the previous exercise
#e.g DWH_ROLE_ARN="arn:aws:iam::988332130976:role/dwhRole"
DWH_ROLE_ARN="arn:aws:iam::004051775499:role/dwhRole"


# STEP2: CONNECT TO THE REDSHIFT CLUSTER

conn_string="postgresql://{}:{}@{}:{}/{}".format(DWH_DB_USER, DWH_DB_PASSWORD, DWH_ENDPOINT, DWH_PORT,DWH_DB)
print(conn_string)
#%sql $conn_string



import boto3

s3 = boto3.resource('s3',
                       region_name="us-west-2",
                       aws_access_key_id=KEY,
                       aws_secret_access_key=SECRET
                     )

sampleDbBucket =  s3.Bucket("udacity-labs")

for obj in sampleDbBucket.objects.filter(Prefix="tickets"):
    print(obj)


# STEP3: CREATE TABLES

# First connection with psycopg2
try:
    conn = psycopg2.connect("postgresql://{}:{}@{}:{}/{}".format(DWH_DB_USER, DWH_DB_PASSWORD, DWH_ENDPOINT, DWH_PORT,DWH_DB))
    print("1. works")
except psycopg2.Error as e:
    print("Error")
    print(e)


try:
    cur = conn.cursor()
    print("2. cursor works")
except psycopg2.Error as e:
    print("Error")
    print(e)

conn.set_session(autocommit=True)

print("3. create first table")
cur.execute("""
            DROP TABLE IF EXISTS "sporting_event_ticket";
            CREATE TABLE "sporting_event_ticket" (
                "id" double precision DEFAULT nextval('sporting_event_ticket_seq') NOT NULL,
                "sporting_event_id" double precision NOT NULL,
                "sport_location_id" double precision NOT NULL,
                "seat_level" numeric(1,0) NOT NULL,
                "seat_section" character varying(15) NOT NULL,
                "seat_row" character varying(10) NOT NULL,
                "seat" character varying(10) NOT NULL,
                "ticketholder_id" double precision,
                "ticket_price" numeric(8,2) NOT NULL);
            """)

qry = """
    copy sporting_event_ticket from 's3://udacity-labs/tickets/split/part'
    credentials 'aws_iam_role={}'
    gzip delimiter ';' compupdate off region 'us-west-2';
""".format(DWH_ROLE_ARN)

print("4. insert into first table")
cur.execute(qry)

print("5. create second table")
cur.execute("""
            DROP TABLE IF EXISTS "sporting_event_ticket_full";
            CREATE TABLE "sporting_event_ticket_full" (
                "id" double precision DEFAULT nextval('sporting_event_ticket_seq') NOT NULL,
                "sporting_event_id" double precision NOT NULL,
                "sport_location_id" double precision NOT NULL,
                "seat_level" numeric(1,0) NOT NULL,
                "seat_section" character varying(15) NOT NULL,
                "seat_row" character varying(10) NOT NULL,
                "seat" character varying(10) NOT NULL,
                "ticketholder_id" double precision,
                "ticket_price" numeric(8,2) NOT NULL
            );
            """)

qry2 = """
    copy sporting_event_ticket_full from 's3://udacity-labs/tickets/full/full.csv.gz'
    credentials 'aws_iam_role={}'
    gzip delimiter ';' compupdate off region 'us-west-2';
""".format(DWH_ROLE_ARN)

print("6. insert into second table")
cur.execute(qry2)
