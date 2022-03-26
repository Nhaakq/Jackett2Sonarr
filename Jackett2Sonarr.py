import sqlite3, json
import os.path
import sys
from os import listdir
from os.path import isfile, join
from sqlite3 import Error

def insert_datas(database, task):
    try:
        conn = sqlite3.connect(database,timeout=10)
    except Error as e:
        print(e)

    sql = ''' INSERT OR IGNORE INTO Indexers (Name,"Implementation",Settings,ConfigContract,EnableRss,EnableAutomaticSearch,EnableInteractiveSearch,Priority,Tags,DownloadClientId)
             VALUES (?,?,?,?,?,?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()

def update_datas(database, sql_update):
    try:
        conn = sqlite3.connect(database,timeout=10)
    except Error as e:
        print(e)

    cur = conn.cursor()
    cur.execute(sql_update)
    conn.commit()

def check_names(database, sql_update):
    try:
        conn = sqlite3.connect(database,timeout=10)
    except Error as e:
        print(e)

    cur = conn.cursor()
    cur.execute(sql_update)
    export_line = cur.fetchall()
    conn.commit()
    return export_line

def main():
    av_files = []
    user_indexers = []  
    path_sonarr = input('Sonnar.db path ? :') or '/data/Dockers/Sonarr/sonarr.db'
    path_jackett = input('Jackett configuration path ? :') or '/data/Dockers/Jackett/Jackett'
    path_indexers = join(path_jackett,'Indexers')
    choice_all = input('Do you want to import all Indexers ? (y/n)') or 'n'

    f = open ((path_jackett+'/ServerConfig.json'), "r")
    data = json.loads(f.read())
    url_jackett = data['BaseUrlOverride']
    api_key = data['APIKey']
    f.close()

    try:
        conn = sqlite3.connect(path_sonarr,timeout=10)
    except Error as e:
        print(e)

    onlyfiles = [f for f in listdir(path_indexers) if (isfile(join(path_indexers, f)) and (f.endswith('.json')))]

    compteur = 0
    for file in onlyfiles:
        file = file.split('.json')
        av_files.append(file[0])
        print(compteur, '-', file[0])
        compteur += 1
    
    if choice_all in 'yY':
        for index_name in av_files:
            sql2 = "SELECT * FROM Indexers WHERE Name='"+index_name+"';"
            all_line = check_names(path_sonarr,sql2)
            if not all_line :
                sql_insert = (index_name,'Newznab','''{"baseUrl": "'''+url_jackett+'''/api/v2.0/indexers/'''+index_name+'''/results/torznab/","apiPath": "/api","apiKey": "'''+api_key+'''","categories": [],"animeCategories": [],"animeStandardFormatSearch": true}''','NewznabSettings',1,1,1,25,'[]',0)            
                insert_datas(path_sonarr,sql_insert)
            else:
                sql_update=('''Update Indexers set Name = "'''+index_name+'''", Settings = '{"baseUrl": "'''+url_jackett+'''/api/v2.0/indexers/'''+index_name+'''/results/torznab/","apiPath": "/api","apiKey": "'''+api_key+'''","categories": [],"animeCategories": [],"animeStandardFormatSearch": true}'  where Name = "'''+index_name+'''";''')
                update_datas(path_sonarr,sql_update)
        exit()
    
    user_indexers = [int(item) for item in input("Enter the Indexers number separate with spaces : ").split()]
    for select in user_indexers:
        index_name = av_files[select]
        sql2 = "SELECT * FROM Indexers WHERE Name='"+index_name+"';"
        all_line = check_names(path_sonarr,sql2)
        if not all_line :
            sql_insert = (index_name,'Newznab','''{"baseUrl": "'''+url_jackett+'''/api/v2.0/indexers/'''+index_name+'''/results/torznab/","apiPath": "/api","apiKey": "'''+api_key+'''","categories": [],"animeCategories": [],"animeStandardFormatSearch": true}''','NewznabSettings',1,1,1,25,'[]',0)            
            #print(sql_insert)
            insert_datas(path_sonarr,sql_insert)
        else:
            sql_update=('''Update Indexers set Name = "'''+index_name+'''", Settings = '{"baseUrl": "'''+url_jackett+'''/api/v2.0/indexers/'''+index_name+'''/results/torznab/","apiPath": "/api","apiKey": "'''+api_key+'''","categories": [],"animeCategories": [],"animeStandardFormatSearch": true}'  where Name = "'''+index_name+'''";''')
            update_datas(path_sonarr,sql_update)
            #print(sql_update)

if __name__ == '__main__':
    main()


