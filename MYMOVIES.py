import sqlite3
connection = sqlite3.connect("Films.db")
cursor = connection.cursor()
sql_command=""" CREATE TABLE MyMovies(Name VARCHAR(25),
Actor VARCHAR(50),
Actress VARCHAR(50),
Director VARCHAR(50),
Year_of_release INTEGER);"""
cursor.execute(sql_command)
sql_command="""INSERT INTO MyMovies(Name,Actor,Actress,Director,Year_of_release)VALUES("Viswasam","Ajith Kumar","Nayanthara","Siva",2019);"""
cursor.execute(sql_command)
sql_command="""INSERT INTO MyMovies(Name,Actor,Actress,Director,Year_of_release)VALUES("Ayan","Suriya","Tamannaah","K.V.Anand",1193);"""
cursor.execute(sql_command)
sql_command="""INSERT INTO MyMovies(Name,Actor,Actress,Director,Year_of_release)VALUES("Theri","Vijay","Samantha","Atlee Kumar",2016);"""
cursor.execute(sql_command)
connection.commit()
cursor.execute("SELECT * FROM MyMovies")
print("fetchall:")
result=cursor.fetchall()
for r in result:
    print(r)
