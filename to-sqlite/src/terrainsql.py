
import os
import glob as glob
import sys
from pathlib import Path
import sqlite3
from sqlite3 import Error
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-d", "--tile_directory", help="Specify the directory of terrain files.")
parser.add_argument("-o", "--outfilename", help="Specify name and location of sqlite database.")
args = parser.parse_args()
if args.tile_directory == None:
    print('Terrain tile directory does not exist or is incorrect.')
    sys.exit()

if args.outfilename == None:
    print('Outfilename not specified.')
    sys.exit()

sql_create__table = """ CREATE TABLE IF NOT EXISTS data3D (
z integer NOT NULL, x integer NOT NULL, y integer NOT NULL,
image BLOB NOT NULL); """

def table_create(conn, entersql):
    try:
        c = conn.cursor()
        c.execute(entersql)
    except Error as e:
        print(e)

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        table_create(conn,sql_create__table)
    except Error as e:
        print(e)
    finally:
        conn.close()

if __name__ == '__main__':
    sql = ''' INSERT INTO data3D ( z, x, y, image) VALUES(?,?,?,?) '''
    
    print("...Started...")
    dbname = args.outfilename
    tilefolder = args.tile_directory
    create_connection(dbname)
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cn = 0
    pathlist = list(Path(tilefolder).glob('**/*.terrain'))
    path_len = len(pathlist)
    path_len = 100/path_len
    for foldname in pathlist:
        foldlist = str(foldname).replace('.terrain', '').split('/')
        cn = cn + 1
        with open(foldname, 'rb') as input_file:
            ablob = input_file.read()
            if cn % 10000 == 0:
                print("Progress: {:0.0%}".format((path_len * cn)/100), end="\r")
                conn.commit()
            t_len = len(foldlist) - 1 
            a_tile = (foldlist[t_len - 2],foldlist[t_len - 1],foldlist[t_len], ablob)
            cur.execute(sql, a_tile)
    cur.execute('CREATE INDEX  xyz on  data3D(z, x, y)')
    conn.commit()
    conn.close()
    print("...Complete...")

   