from time import time
import configparser
import matplotlib.pyplot as plt
import pandas as pd
import psycopg2


config = configparser.ConfigParser()
config.read_file(open('dwh.cfg'))
KEY=config.get('AWS','key')
SECRET= config.get('AWS','secret')

DWH_DB= config.get("DWH","DWH_DB")
DWH_DB_USER= config.get("DWH","DWH_DB_USER")
DWH_DB_PASSWORD= config.get("DWH","DWH_DB_PASSWORD")
DWH_PORT = config.get("DWH","DWH_PORT")



# FILL IN THE REDSHIFT ENDPOINT HERE
# e.g. DWH_ENDPOINT="redshift-cluster-1.csmamz5zxmle.us-west-2.redshift.amazonaws.com"
DWH_ENDPOINT="dwhcluster2.c7ytdzszmvzr.us-west-2.redshift.amazonaws.com:5439"

#FILL IN THE IAM ROLE ARN you got in step 2.2 of the previous exercise
#e.g DWH_ROLE_ARN="arn:aws:iam::988332130976:role/dwhRole"
DWH_ROLE_ARN="aws:iam::004051775499:role/dwhadmin"

# STEP 2 CONNECT TO THE Clusters:
# First set connection string:
import os
conn_string="postgresql://{}:{}@{}:{}/{}".format(DWH_DB_USER, DWH_DB_PASSWORD, DWH_ENDPOINT, DWH_PORT,DWH_DB)
print(conn_string)
conn_connect = psycopg2.connect(conn_string)

try:
    conn_connect = psycopg2.connect(conn_string)
    print("1. works")
except psycopg2.Error as e:
    print("Error")
    print(e)

# set cursor
try:
    cur = conn_connect.cursor()
    print("2. cursor works")
except psycopg2.Error as e:
    print("Error")
    print(e)

conn_connect.set_session(autocommit=True)



# STEP 3 CREATE TABLES:


create_tables_nodist_sql = """
                    CREATE SCHEMA IF NOT EXISTS nodist;
                    SET search_path TO nodist;

                    DROP TABLE IF EXISTS part cascade;
                    DROP TABLE IF EXISTS supplier;
                    DROP TABLE IF EXISTS supplier;
                    DROP TABLE IF EXISTS customer;
                    DROP TABLE IF EXISTS dwdate;
                    DROP TABLE IF EXISTS lineorder;

                    CREATE TABLE part
                    (
                      p_partkey     INTEGER NOT NULL,
                      p_name        VARCHAR(22) NOT NULL,
                      p_mfgr        VARCHAR(6) NOT NULL,
                      p_category    VARCHAR(7) NOT NULL,
                      p_brand1      VARCHAR(9) NOT NULL,
                      p_color       VARCHAR(11) NOT NULL,
                      p_type        VARCHAR(25) NOT NULL,
                      p_size        INTEGER NOT NULL,
                      p_container   VARCHAR(10) NOT NULL
                    );

                    CREATE TABLE supplier
                    (
                      s_suppkey   INTEGER NOT NULL,
                      s_name      VARCHAR(25) NOT NULL,
                      s_address   VARCHAR(25) NOT NULL,
                      s_city      VARCHAR(10) NOT NULL,
                      s_nation    VARCHAR(15) NOT NULL,
                      s_region    VARCHAR(12) NOT NULL,
                      s_phone     VARCHAR(15) NOT NULL
                    );

                    CREATE TABLE customer
                    (
                      c_custkey      INTEGER NOT NULL,
                      c_name         VARCHAR(25) NOT NULL,
                      c_address      VARCHAR(25) NOT NULL,
                      c_city         VARCHAR(10) NOT NULL,
                      c_nation       VARCHAR(15) NOT NULL,
                      c_region       VARCHAR(12) NOT NULL,
                      c_phone        VARCHAR(15) NOT NULL,
                      c_mktsegment   VARCHAR(10) NOT NULL
                    );

                    CREATE TABLE dwdate
                    (
                      d_datekey            INTEGER NOT NULL,
                      d_date               VARCHAR(19) NOT NULL,
                      d_dayofweek          VARCHAR(10) NOT NULL,
                      d_month              VARCHAR(10) NOT NULL,
                      d_year               INTEGER NOT NULL,
                      d_yearmonthnum       INTEGER NOT NULL,
                      d_yearmonth          VARCHAR(8) NOT NULL,
                      d_daynuminweek       INTEGER NOT NULL,
                      d_daynuminmonth      INTEGER NOT NULL,
                      d_daynuminyear       INTEGER NOT NULL,
                      d_monthnuminyear     INTEGER NOT NULL,
                      d_weeknuminyear      INTEGER NOT NULL,
                      d_sellingseason      VARCHAR(13) NOT NULL,
                      d_lastdayinweekfl    VARCHAR(1) NOT NULL,
                      d_lastdayinmonthfl   VARCHAR(1) NOT NULL,
                      d_holidayfl          VARCHAR(1) NOT NULL,
                      d_weekdayfl          VARCHAR(1) NOT NULL
                    );
                    CREATE TABLE lineorder
                    (
                      lo_orderkey          INTEGER NOT NULL,
                      lo_linenumber        INTEGER NOT NULL,
                      lo_custkey           INTEGER NOT NULL,
                      lo_partkey           INTEGER NOT NULL,
                      lo_suppkey           INTEGER NOT NULL,
                      lo_orderdate         INTEGER NOT NULL,
                      lo_orderpriority     VARCHAR(15) NOT NULL,
                      lo_shippriority      VARCHAR(1) NOT NULL,
                      lo_quantity          INTEGER NOT NULL,
                      lo_extendedprice     INTEGER NOT NULL,
                      lo_ordertotalprice   INTEGER NOT NULL,
                      lo_discount          INTEGER NOT NULL,
                      lo_revenue           INTEGER NOT NULL,
                      lo_supplycost        INTEGER NOT NULL,
                      lo_tax               INTEGER NOT NULL,
                      lo_commitdate        INTEGER NOT NULL,
                      lo_shipmode          VARCHAR(10) NOT NULL
                    );
                    """

try:
    cur.execute(create_tables_nodist_sql)
    print("Tables nodist created")
except psycopg2.Error as e:
    print("Error")
    print(e)


create_tables_dist_sql = """
                        CREATE SCHEMA IF NOT EXISTS dist;
                        SET search_path TO dist;

                        DROP TABLE IF EXISTS part cascade;
                        DROP TABLE IF EXISTS supplier;
                        DROP TABLE IF EXISTS supplier;
                        DROP TABLE IF EXISTS customer;
                        DROP TABLE IF EXISTS dwdate;
                        DROP TABLE IF EXISTS lineorder;

                        CREATE TABLE part (
                          p_partkey     	integer     	not null	sortkey distkey,
                          p_name        	varchar(22) 	not null,
                          p_mfgr        	varchar(6)      not null,
                          p_category    	varchar(7)      not null,
                          p_brand1      	varchar(9)      not null,
                          p_color       	varchar(11) 	not null,
                          p_type        	varchar(25) 	not null,
                          p_size        	integer     	not null,
                          p_container   	varchar(10)     not null
                        );

                        CREATE TABLE supplier (
                          s_suppkey     	integer        not null sortkey,
                          s_name        	varchar(25)    not null,
                          s_address     	varchar(25)    not null,
                          s_city        	varchar(10)    not null,
                          s_nation      	varchar(15)    not null,
                          s_region      	varchar(12)    not null,
                          s_phone       	varchar(15)    not null)
                        diststyle all;

                        CREATE TABLE customer (
                          c_custkey     	integer        not null sortkey,
                          c_name        	varchar(25)    not null,
                          c_address     	varchar(25)    not null,
                          c_city        	varchar(10)    not null,
                          c_nation      	varchar(15)    not null,
                          c_region      	varchar(12)    not null,
                          c_phone       	varchar(15)    not null,
                          c_mktsegment      varchar(10)    not null)
                        diststyle all;

                        CREATE TABLE dwdate (
                          d_datekey            integer       not null sortkey,
                          d_date               varchar(19)   not null,
                          d_dayofweek	      varchar(10)   not null,
                          d_month      	    varchar(10)   not null,
                          d_year               integer       not null,
                          d_yearmonthnum       integer  	 not null,
                          d_yearmonth          varchar(8)	not null,
                          d_daynuminweek       integer       not null,
                          d_daynuminmonth      integer       not null,
                          d_daynuminyear       integer       not null,
                          d_monthnuminyear     integer       not null,
                          d_weeknuminyear      integer       not null,
                          d_sellingseason      varchar(13)    not null,
                          d_lastdayinweekfl    varchar(1)    not null,
                          d_lastdayinmonthfl   varchar(1)    not null,
                          d_holidayfl          varchar(1)    not null,
                          d_weekdayfl          varchar(1)    not null)
                        diststyle all;

                        CREATE TABLE lineorder (
                          lo_orderkey      	    integer     	not null,
                          lo_linenumber        	integer     	not null,
                          lo_custkey           	integer     	not null,
                          lo_partkey           	integer     	not null distkey,
                          lo_suppkey           	integer     	not null,
                          lo_orderdate         	integer     	not null sortkey,
                          lo_orderpriority     	varchar(15)     not null,
                          lo_shippriority      	varchar(1)      not null,
                          lo_quantity          	integer     	not null,
                          lo_extendedprice     	integer     	not null,
                          lo_ordertotalprice   	integer     	not null,
                          lo_discount          	integer     	not null,
                          lo_revenue           	integer     	not null,
                          lo_supplycost        	integer     	not null,
                          lo_tax               	integer     	not null,
                          lo_commitdate         integer         not null,
                          lo_shipmode          	varchar(10)     not null
                        );
                        """

try:
    cur.execute(create_tables_dist_sql)
    print("Tables dist created")
except psycopg2.Error as e:
    print("Error")
    print(e)
