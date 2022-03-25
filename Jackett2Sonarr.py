import sqlite3
import os.path
import sys
from os import listdir
from os.path import isfile, join
from sqlite3 import Error

def insert_datas(database, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """
    #database = r"C:/Users/Nathan/Documents/Scripts/Python/SUTOM/dictionnaire.db"
    try:
        conn = sqlite3.connect(database)
    except Error as e:
        print(e)

    sql = ''' INSERT OR IGNORE INTO Indexers (Name,"Implementation",Settings,ConfigContract,EnableRss,EnableAutomaticSearch,EnableInteractiveSearch,Priority,Tags,DownloadClientId)
             VALUES (?,?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()


def main():
    av_files = []
    path_sonarr = input('Sonnar.db path ? :') or 'scripts/Jackett2Sonarr/sonarr.db'
    path_jackett = input('Jackett configuration path ? :') or 'scripts/Jackett2Sonarr/Jackett/'
    path_indexers = join(path_jackett,'Indexers')
    choice_all = input('Do you want to import all Indexers ? (y/n)') or 'n'

    try:
        conn = sqlite3.connect(path_sonarr)
    except Error as e:
        print(e)
      
    #print(path_sonarr)
    #print(path_jackett)

    onlyfiles = [f for f in listdir(path_indexers) if (isfile(join(path_indexers, f)) and (f.endswith('.json')))]

    compteur = 0
    for file in onlyfiles:
        file = file.split('.json')
        av_files.append(file[0])
        print(compteur, '-', file[0])
        compteur += 1
    
    if choice_all in 'yY':
        print('IMPORT ALL')
        exit()
    #print(onlyfiles[2])
    lst1 = []    
    lst1 = [int(item) for item in input("Enter the Indexers number separate with spaces : ").split()]

    for select in lst1:
        index_name = av_files[select]
        sql2 = "SELECT * FROM Indexers WHERE Name='"+index_name+"';"
        cur = conn.cursor()
        cur.execute(sql2)
        #conn.commit()
        all_line=cur.fetchall()
        if not all_line :
            print('c vide')
            sql_insert = (index_name,'Newznab','{
            "baseUrl": "https://jTESTTESTTEST/",
            "apiPath": "/api",
            "apiKey": "16qks88lejde3b1z2oz74zcxtdxptqud",
            "categories": [
                5000,
                5040,
                5050,
                100208
            ],
            "animeCategories": [],
            "animeStandardFormatSearch": true
            }','NewznabSettings',1,1,1,25,'[]',0))
            print(sql_insert)
            #insert_datas(path_sonarr,)



if __name__ == '__main__':
    main()


