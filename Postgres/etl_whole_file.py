import os
import glob
import psycopg2
import pandas as pd
from etl import *


def process_song_file(cur, filepath):
    # open song file
    df = pd.read_json(filepath, lines=True)

    # insert artist record
    artist_data = df.loc[(df['artist_id'].notnull() & df['artist_name'].notnull()),
                        ['artist_id', 'artist_name', 'artist_location', 'artist_latitude',
                        'artist_longitude']].values[0].tolist()
    cur.execute(artist_table_insert, artist_data)



def process_log_file(cur, filepath):
    #open log file
    df = pd.read_json(filepath, lines=True)

    #load user table
    user_df = df.loc[(df['userId'].notnull() & df['gender'].notnull()
                    & df['level'].notnull() & df['ts'].notnull()),
                    ['userId', 'firstName', 'lastName', 'gender', 'level', 'ts']]


def process_data(cur, conn, filepath, func):
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files, in os.walk(filepath):
        files = glob.glob(os.path.join(root, '*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))



def main():
    conn = psycopg2.connect("host=192.168.178.22 dbname=test user=postgres password=Dudko010914")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data', func=process_song_file)

    conn.close()

if __name__ == "__main__":
    main()
