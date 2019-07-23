import psycopg2
from flask import Flask, render_template, json, request, redirect, url_for, flash, jsonify

app = Flask(__name__)

try:
    conn = psycopg2.connect("host=127.0.0.1 dbname=dwh user=postgres password=Dudko$010914")
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



ARN='arn:aws:iam::004051775499:role/dwhadmin'

AMA_EXPORT_DATA='17083935421018098.txt'
LOG_JSONPATH='s3://udacity-dend/log_json_path.json'
SONG_DATA='s3://udacity-dend/song_data'


staging_ama_order_export = ("""
                            COPY ama_Order_export2 FROM '/data/17083935421018098.txt';
                            """)


try:
    cur.execute(staging_ama_order_export)
except psycopg2.Error as e:
    print("Error")
    print(e)
