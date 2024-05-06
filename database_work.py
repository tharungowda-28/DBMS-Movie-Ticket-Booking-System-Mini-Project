import pymysql as ps

def create_database(dbname):
  con=ps.connect(host="localhost", user="root", password="Tharun@22")
  cur=con.cursor()
  cur.execute("show databases")
  dbs=cur.fetchall()
  for db in dbs:
      #print(db[0])
      if db[0]==dbname:
          return True
        
  cur.execute("CREATE DATABASE "+dbname)
  return True

#create_database("cinema")

def create_tables():
    if create_database("cinema"):
        con=ps.connect(host="localhost", user="root", password="Tharun@22",db="cinema")
        cur=con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS MOVIE(MID VARCHAR(20) PRIMARY KEY, MOVIENAME VARCHAR(300), RELEASE_DATE DATE, RATING FLOAT)")
        cur.execute("CREATE TABLE IF NOT EXISTS SHOWS(SID INT PRIMARY KEY AUTO_INCREMENT,MID VARCHAR(20),SDATE DATE, TIMINGS VARCHAR(200),NSHOWS INT)")
        cur.execute("CREATE TABLE IF NOT EXISTS TICKETS(TID INT PRIMARY KEY AUTO_INCREMENT,SID INT,SHOWNO INT,TOTALSEATS INT,SEATLIST VARCHAR(100),BOOKINGTIME TIMESTAMP)")
    
def show_tables():
  con=ps.connect(host="localhost", user="root", password="Tharun@22",db="cinema")
  cur=con.cursor()
  cur.execute("show tables")
  tables=cur.fetchall()
  for tb in tables:
      print(tb[0])
      cur.execute("desc " +tb[0])
      ds=cur.fetchall()
      for row in ds:
          print(row)


create_tables()
show_tables()
