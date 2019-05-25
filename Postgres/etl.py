import os
import glob
import psycopg2
import pandas as pd


try:
    conn = psycopg2.connect("host=192.168.178.22 dbname=test user=postgres password=Dudko010914")
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



def get_files(filepath):
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, '*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))
    return all_files

song_files = get_files('data')
print(song_files[0])


conn.close()
