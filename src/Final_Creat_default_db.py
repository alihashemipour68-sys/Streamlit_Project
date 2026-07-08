import sqlite3
import src.app_api_list0 as app_api_list0

DB_NAME = 'Movieinfo_Final_default.db'
def init_db():
    conn = sqlite3.connect(DB_NAME)
    conn.close()

# init_db()
def create_table():
    conn = sqlite3.connect(DB_NAME)
    
    query = """CREATE TABLE IF NOT EXISTS MOVIES
     (id INTEGER PRIMARY KEY AUTOINCREMENT,
      TITLE TEXT,
       imdb_rate REAL, year_build INTEGER,
         country TEXt, awards TEXT,
         genres TEXT,plot TEXT,poster TEXT
        
        )
             """
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()

create_table()

def insert_movie(title, imdb_rate,year_build,country,awards,genres,plot,poster):
    conn = sqlite3.connect(DB_NAME)
    query = "INSERT INTO MOVIES (TITLE, imdb_rate,year_build,\
        country,awards,genres,plot,poster) VALUES (?, ?,?,?,?,?,?,?)"
    cursor = conn.cursor()
    cursor.execute(query, (title, imdb_rate,year_build,country,awards,genres,plot,poster))
    conn.commit()
    conn.close()


for i in range(1,251):
    film_250_=app_api_list0.get_movei_info(i)
    insert_movie(film_250_[0] ,film_250_[1],film_250_[2]\
                 ,film_250_[3],film_250_[4],film_250_[5],film_250_[6],film_250_[7])


