import os
import glob
import mysql
import pandas as pd


try:
    conn = mysql.connector.connect(host='192.168.178.22',
                                        database='test',
                                        user='aldudko2',
                                        password='Dudko010914')
    print("1. Woooorks")
except Error as e:
    print("Error while connection to mysql", e)


try:
    cur = conn.cursor()
    print("2. cursor ok")
except Error as e:
    print("Error: Could not get curser to the Database")
    print(e)

conn.autocommit=True

"""
def get_files(filepath):
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, '*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    return all_files
"""
conn.close()
