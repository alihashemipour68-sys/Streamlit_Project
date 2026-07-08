import sqlite3
import shutil
import os

DB_NAME = 'Movieinfo_Final.db'
SOURCE_DB = 'Movieinfo_Final_default.db'

#------------------------------------------------------------
def Restore_Default():
        conn = sqlite3.connect(DB_NAME)
        conn.close()
        
        if os.path.exists(DB_NAME):
            os.remove(DB_NAME)
        
        if os.path.exists(SOURCE_DB):
            shutil.copy2(SOURCE_DB, DB_NAME)
            return True
        else:
            return False

#----------------------------------------------------------
def select_all_records():
    query='SELECT * FROM MOVIES'
    conn=sqlite3.connect(DB_NAME)
    cursor=conn.cursor()
    rows=cursor.execute(query).fetchall()
    conn.close()
    return rows
#---------------------------------------------------------
def Oscar_Nominated_Rating():
    data_list = select_all_records()
    data_list_oscar_Nominated=[]
    for i in range(len(data_list)):
        if ("Oscar" in data_list[i][5]) and ("Nominated" in data_list[i][5]) :
            count=int(data_list[i][5][13:16])
            data_list_oscar_Nominated.append([count,data_list[i]])
        data_list_oscar_Nominated.sort(reverse=True)
    data_list_oscar_Nominated_new=[]
    for i in range(len(data_list_oscar_Nominated)):
            data_list_oscar_Nominated[i].pop(0)
            data_list_oscar_Nominated_new.append(data_list_oscar_Nominated[i][0])

    return data_list_oscar_Nominated_new
# print(Oscar_Nominated_Rating())
#-------------------------------------------------------
def Oscar_Won_Rating():
    data_list = select_all_records()
    data_list_oscar_Won=[]
    for i in range(len(data_list)):
        if ("Oscar" in data_list[i][5]) and ("Won" in data_list[i][5]) :
            count=int(data_list[i][5][3:6])
            data_list_oscar_Won.append([count,data_list[i]])
        data_list_oscar_Won.sort(reverse=True)
    data_list_oscar_Won_new=[]
    for i in range(len(data_list_oscar_Won)):
            data_list_oscar_Won[i].pop(0)
            data_list_oscar_Won_new.append(data_list_oscar_Won[i][0])
        
    return data_list_oscar_Won_new
#----------------------------------------------------------
def update_record_by_id(id,imdb_rate):
        query=' UPDATE MOVIES SET imdb_rate = ? WHERE id = ?'
        conn=sqlite3.connect(DB_NAME)
        cursor=conn.cursor()
        cursor.execute(query,(imdb_rate,id))
        conn.commit()
        conn.close()
#----------------------------------------------------------------
def delete_records(record):
    query='DELETE FROM MOVIES WHERE id = ?'
    conn=sqlite3.connect(DB_NAME)
    cursor=conn.cursor()
    cursor.execute(query,(record,))
    conn.commit()
    conn.close()
#-------------------------------------------------------------------
# imdb_range=float(input('Enter Minimum Of IMDB Rating: '))
def imdb_range(min_imdb):
    min_imdb=float(min_imdb)
    data_list = select_all_records()
    data_list_imdb=[]
    for i in range(len(data_list)):
        if data_list[i][2]>=min_imdb:
            data_list_imdb.append(data_list[i])
    return data_list_imdb

#-------------------------------------------------------------------
# Year_build_range=float(input('Enter Minimum Of Year Build: '))
def year_range(min_year):
    min_year=int(min_year)
    data_list = select_all_records()
    data_list_year=[]
    for i in range(len(data_list)):
        if data_list[i][3]>=min_year:
            data_list_year.append(data_list[i])
    return data_list_year

# print(data_list_year)
#-----------------------------------------------------------------
# film_name=input('Enter Filme Name:')
def film_Search_Name(film_name):
    data_list = select_all_records()
    data_list_name=[]
    for i in range(len(data_list)):
        if film_name.lower() in data_list[i][1].lower():
            data_list_name.append(data_list[i])
    return data_list_name
# print(film_Search_Name(film_name))    
#------------------------------------------------------------------
def list_country(country_name):
    data_list = select_all_records()
    data_list_country_name=[]
    for i in range(len(data_list)):
        if country_name in data_list[i][4]:
            data_list_country_name.append(data_list[i])
    return data_list_country_name

# print(f'USA: {data_list_USA}')
#--------------------------------------------------------------------
