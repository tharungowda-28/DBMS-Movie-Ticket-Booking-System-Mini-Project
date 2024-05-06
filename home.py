import os
import pymysql as ps
import re

def welcome():
  print("="*70)
  print("\n"*4)
  print(" "*20,"+","="*30,"+", sep="")
  print(" "*20,"|","PVR CINEMA".center (30),"|",sep="")
  print(" "*20,"|", "Movie Ticket Booking System".center (30),"|",sep="")
  print(" "*20,"|", "Year 2023".center (30), "|", sep="")
  print(" "*20,"|", "DBMS Mini Project".center (30),"|",sep="")
  print(" "*20, "+","="*30,"+",sep="")
  print("\n"*4)
  print("="*70)
  input("Continue...(Press Enter) ")
  os.system("cls")

def connection():
    return ps.connect(host="localhost", user="root", password="Tharun@22",db="cinema")

def getMovie(MID):
    con=connection()
    cur=con.cursor()
    cur.execute("SELECT * FROM MOVIE WHERE MID='%s'"%(MID))
    return cur.fetchone()


def getShow(sid):
    con=connection()
    cur=con.cursor()
    cur.execute("SELECT * FROM SHOWS WHERE SID= %s"%(sid))
    return cur.fetchone()
  
def add_movie():
  os.system("cls")
  print("="*70)
  print("\n"*4)
  print(" "*20,"+","="*30,"+", sep="")
  print(" "*20,"|", "PVR CINEMA".center (30), "|", sep="")
  print(" "*20,"|", "Movie Ticket Booking System".center (30), "|", sep="")
  print(" "*20,"|", "Movie ID : ", sep="",end="")
  mid=input()
  if mid=="":
    print(" "*20,"|", "Don't Leave Blank ", sep="",end="")
    input()
    return
  if getMovie(mid):
    print(" "*20,"|", "Already Exists ", sep="",end="")
    input()
    return
  print(" "*20,"|", "Movie Name : ", sep="",end="")
  mname=input ()
  print(" "*20,"|", "Release Date : ", sep="",end="")
  rdate=input()
  print(" "*20,"|", "Rating : ", sep="",end="")
  rating=input()
  con=connection()
  cur=con.cursor()
  cur.execute("INSERT INTO MOVIE VALUES('%s','%s','%s',%s)"%(mid,mname,rdate,rating))
  con.commit()
  print("Add Movie Successfully")
  input()
  

def add_shows():
  os.system("cls")
  print("="*70)
  print("\n"*4)
  print(" "*20,"+","="*30,"+", sep="")
  print(" "*20,"|", "PVR CINEMA".center (30), "|", sep="")
  print(" "*20,"|", "Movie Ticket Booking System".center (30), "|", sep="")
  print(" "*20,"|", "Movie ID : ", sep="",end="")
  mid=input()
  if getMovie(mid):
      print(" "*20,"|", "Show Date : ", sep="",end="")
      sdate=input()
      print(" "*20,"|", "Number of Shows : ", sep="",end="")
      nshows=int(input())
      timings=[]
      print(" "*20,"|", "Timings : ", sep="")
      for x in range(nshows):
          print(" "*20,"|", "Show Number %d : "%(x+1), sep="",end="")
          timings.append(input())
      tm="|".join(timings)
      con=connection()
      cur=con.cursor()
      cur.execute("INSERT INTO SHOWS VALUES(0,'%s','%s','%s',%s)"%(mid,sdate,tm,nshows))
      con.commit()
      print("Add Show Successfully")
      input()

#add_shows()

def edit_movie():
  os.system("cls")
  print("="*70)
  print("\n"*4)
  print(" "*20,"+","="*30,"+", sep="")
  print(" "*20,"|", "PVR CINEMA".center (30), "|", sep="")
  print(" "*20,"|", "Movie Ticket Booking System".center (30), "|", sep="")
  print(" "*20,"|", "Movie ID : ", sep="",end="")
  mid=input()
  mv=getMovie(mid)
  if mv:
      print(" "*20,"|", "1. Movie Name : %s"%(mv[1]), sep="")
      print(" "*20,"|", "2. Release Date : %s"%(mv[2]), sep="")
      print(" "*20,"|", "3. Rating : %s"%(mv[3]), sep="")
      print(" "*20,"+","-"*30,"+",sep="")
      print(" "*20,"|", "Enter Choice (What Edit?):", sep="",end="")
      ch=int(input())
      V=["MID","MOVIENAME","RELEASE_DATE","RATING"]
      if ch>=1 and ch<len(V):
          print(" "*20,"|", "%s : "%(V[ch]), sep="",end="")
          nvalue=input()
          con=connection()
          cur=con.cursor()
          cur.execute("UPDATE MOVIE SET %s='%s' WHERE MID='%s'"%(V[ch],nvalue,mid))
          con.commit()
      else:
          print(" "*19,"|","Enter Correct Choice.. ")
  else:
      print(" "*19,"|","Enter Correct Movie Id")



def edit_shows():
  os.system("cls")
  print("="*70)
  print("\n"*4)
  print(" "*20,"+","="*30,"+", sep="")
  print(" "*20,"|", "PVR CINEMA".center (30), "|", sep="")
  print(" "*20,"|", "Movie Ticket Booking System".center (30), "|", sep="")
  print(" "*20,"|", "Show Number : ", sep="",end="")
  sno=input()
  if sno=="":
    print(" "*20,"|","Don't Leave Blank",sep="")
    input()
    return
  sh=getShow(sno)
  if sh:
      print(" "*20,"|", "1. Movie ID : %s"%(sh[1]), sep="")
      print(" "*20,"|", "2. Show Date : %s"%(sh[2]), sep="")
      print(" "*20,"|", "3. Add New Show ", sep="")
      print(" "*20,"|", "4. Remove New Show ", sep="")
      print(" "*20,"+","-"*30,"+",sep="")
      print(" "*20,"|", "Enter Choice (What Edit?):", sep="",end="")
      ch=int(input())
      con=connection()
      cur=con.cursor()
      if ch==1:
        print(" "*20,"|", "New Movie ID : ", sep="",end="")
        mid=input()
        cur.execute("UPDATE SHOWS SET MID='%s' WHERE SID='%s'"%(mid,sno))
        con.commit()
      elif ch==2:
        print(" "*20,"|", "Show Date : ", sep="",end="")
        SDATE=input()
        cur.execute("UPDATE SHOWS SET SDATE='%s' WHERE SID='%s'"%(SDATE,sno))
        con.commit()
      elif ch==3:
        print(" "*20,"|","Timing : ",sep="")
        print(" "*20,"|","Show NO %s : "%(int(sh[4])+1),sep="",end="")
        TIMING=input()
        cur.execute("UPDATE SHOWS SET TIMINGS='%s', NSHOWS=NSHOWS+1 WHERE SID='%s'"%(sh[3]+"|"+TIMING,sno))
        con.commit()
      elif ch==4:
        S=sh[3].split("|")
        for i in range(len(S)):
          print(" "*20,"|","Show %d : %s"%(i+1,S[i]),sep="")
        print(" "*20,"|","Show NO ? : ",sep="",end="")
        SN=int(input())
        if SN>0 and SN<=len(S):
          del S[SN-1]
        cur.execute("UPDATE SHOWS SET TIMINGS='%s',NSHOWS=NSHOWS-1 WHERE SID='%s'"%("|".join(S),sno))
        con.commit()
  else:
      print(" "*19,"|","Enter Correct Show Number")

#edit_shows()



def movie_list():
  os.system("cls")
  print("="*70)
  print("MOVIE LIST".center(60))
  con=connection()
  cur=con.cursor()
  cur.execute("SELECT * FROM MOVIE")
  data=cur.fetchall()
  print("-"*60)
  print("|%-5s|%-30s|%-12s|%-7s|"%("ID","NAME","DATE","RATING"))
  print("-"*60)
  for m in data:
    print("|%-5s|%-30s|%-12s|%-7s|"%(m))
  print("-"*60)



def shows_list():
  os.system("cls")
  print("="*70)
  print("SHOWS LIST".center(60))
  con=connection()
  cur=con.cursor()
  cur.execute("SELECT * FROM SHOWS ORDER BY SDATE DESC")
  data=cur.fetchall()
  print("-"*70)
  print("|%-2s|%-4s|%-12s|%-42s|%-3s|"%("SN","NAME","DATE","TIMING","NO"))
  print("-"*70)
  for m in data:
    m=list(m)
    m[3]=m[3].replace("|",",")
    if len(m[3])>35:
      m[3]=m[3][:36]+" ..."
    print("|%-2s|%-4s|%-12s|%-42s|%-3s|"%tuple(m))
  print("-"*70)


#shows_list()

def search_shows():
  os.system("cls")
  print("="*70)
  print("\n"*4)
  print(" "*20,"+","="*30,"+", sep="")
  print(" "*20,"|", "PVR CINEMA".center (30), "|", sep="")
  print(" "*20,"|", "Movie Ticket Booking System".center (30), "|", sep="")
  print(" "*20,"|", "Movie ID : ", sep="",end="")
  MID=input()
  con=connection()
  cur=con.cursor()
  cur.execute("SELECT * FROM SHOWS WHERE MID='%s'"%(MID))
  data=cur.fetchall()
  if len(data)==0:
    print(" "*20,"|", "Movie ID NOT FOUND ",sep="",end="")
  else:
    mv=getMovie(MID)
    print(" "*20,"|", "Movie Name : %s"%(mv[1]),sep="")
    print(" "*20,"|", "Release Date : %s"%(mv[2]),sep="")
    print(" "*20,"|", "Rating : %s"%(mv[3]), sep="")
    print(" "*20,"|", "Show Date: ", sep="")
    print(" "*20,"|", "(YYYY-MM-DD)? : ", sep="",end="")
    SDATE=input()
    if re.search("^\d{4}-\d{2}-\d{2}$",SDATE)==None:
      print(" "*20,"|","DATE PATTERN NOT MATCHED ", sep="")
      return
    
    cur.execute("SELECT * FROM SHOWS WHERE MID='%s' AND SDATE='%s'"%(MID,SDATE))
    data=cur.fetchone()
    if data:
      S=data[3].split("|")
      for i in range(len(S)):
        print(" "*20,"|", "Show %d : %s"%(i+1,S[i]), sep="")
      print("-"*70)
    else:
      print(" "*20,"|", "Show Not Available ", sep="")

        

def mov_maintainance():
  input("Continue...")
  os.system("cls")
  print("="*70)
  print("\n"*4)
  print(" "*20,"+","="*30,"+", sep="")
  print(" "*20,"|", "PVR CINEMA".center(30), "|", sep="")
  print(" "*20,"|", "Movie Ticket Booking System".center(30),"|",sep="")
  print(" "*20,"+","-"*30,"+",sep="")
  print(" "*20,"|","MOVIE MAINTAINANCE MENU".center (30),"|",sep="")
  print(" "*20,"+","-"*30,"+",sep="")
  print(" "*20,"|","%-30s"%("1. Add New Movie"),"|",sep="")
  print(" "*20,"|","%-30s"%("2. Add Shows"),"|", sep="")
  print(" "*20,"|","%-30s"%("3. Edit Movie"),"|", sep="")
  print(" "*20,"|","%-30s"%("4. Edit Shows"),"|",sep="")
  print(" "*20,"|","%-30s"%("5. Movies List"),"|", sep="")
  print(" "*20,"|","%-30s"%("6. Shows List"),"|", sep="")
  print(" "*20,"|","%-30s"%("0. Back"),"|", sep="")
  print(" "*20, "+","="*30,"+", sep="")
  print("\n"*4)
  print("="*70)
  choice=input("Enter your choice : ")
  if choice=="":
    print(" "*20,"|","Don't Leave Blank",sep="")
    input()
    mov_maintainance()
    return
  if not choice.isdigit():
    print(" "*20,"|","Text Not Allowed",sep="")
    input()
    mov_maintainance()
    return
  choice=int(choice)
  if choice==0:
      return
  elif choice==1:
      add_movie()
  elif choice==2:
      add_shows()
  elif choice==3:
      edit_movie()
  elif choice==4:
      edit_shows()
  elif choice==5:
      movie_list()
  elif choice==6:
      shows_list()

  mov_maintainance()


def total_booked_seats(SH):
  D=[]
  con=connection()
  cur=con.cursor()
  cur.execute("SELECT * FROM TICKETS WHERE SID={0} AND SHOWNO={1}".format(SH["SID"],SH["SN"]))
  data=cur.fetchall()
  for d in data:
    D.extend(d[4].split("|"))
  return D


def book_ticket(SH):
  print("Select Seats (how many)? : ")
  ts=input()
  if ts=="":
    print(" "*20,"|"," Don't Leave Blank ", sep="")
  elif not ts.isdigit():
    print(" "*20,"|","Text Not Allowed",sep="")
  elif int(ts)<1 or int(ts)>10:
    print(" "*20,"|"," 1 to 10 seats allowed at a time",sep="")
  else:
    SeatList=[]
    x=0
    TS=total_booked_seats(SH)
    while x < int(ts):
      print("Seat Number %d"%(x+1))
      rows=[chr(i) for i in range(65,75)]
      print("Select Row : ", sep="",end="")
      row=input()
      if row not in rows:
        print("Enter correct Row")
        input()
        continue
      seats=["%02d"%(i) for i in range(1,16)]
      print("Seat Number : ", sep="",end="")
      seatno=input()
      if seatno not in seats:
        print("Enter correct Seat")
        input()
        continue
      if row+seatno in SeatList:
        print("Seat Already Selected")
        input()
        continue
      if row+seatno in TS:
        print("Seat Already Booked")
        input()
        continue
      SeatList+=[row+seatno]
      print(SeatList)
      x+=1
    con=connection()
    cur=con.cursor()
    cur.execute("INSERT INTO TICKETS VALUES(0,%s,%s,%s,'%s',now())"%(SH["SID"],SH["SN"],ts,"|".join(SeatList)))   
    con.commit()
  print("Ticket Booked Successfully ")
  input()


def is_booked(SH,seat ):
  con=connection()
  cur=con.cursor()
  cur.execute("SELECT * FROM TICKETS WHERE SID={0} AND SHOWNO={1} AND SEATLIST like '%{2}%'".format(SH["SID"],SH["SN"],seat))
  data=cur.fetchone()
  return data!=None

  
def available_seats(SH):
  TS=total_booked_seats(SH)
  print("  ",end="")
  for j in range(1,16):
      print("[%02d] "%(j),end="")
  print()
  for i in range(10):
    print("%c "%(chr(65+i)),end="")
    for j in range(15):
      st=chr(65+i)+"%02d"%(j+1)
      if st in TS:
        print("[##] ",end="")
      else:
        print("[  ] ",end="")
    print()

  print("="*70)
  print("Do You Want To Book Any Seat ? (Y/N) : ")
  choice=input()
  if choice in "Yy":
    book_ticket(SH)

#available_seats({"SID":4,"SN":0})



def checking_tickets():
  os.system("cls")
  print("="*70)
  print("\n"*4)
  print(" "*20,"+","="*30,"+", sep="")
  print(" "*20,"|", "PVR CINEMA".center (30), "|", sep="")
  print(" "*20,"|", "Movie Ticket Booking System".center (30), "|", sep="")
  print(" "*20,"|", "Show Date: ", sep="")
  print(" "*20,"|", "(YYYY-MM-DD)? : ", sep="",end="")
  SDATE=input()
  if re.search("^\d{4}-\d{2}-\d{2}$",SDATE)==None:
    print(" "*20,"|","DATE PATTERN NOT MATCHED ", sep="")
    return
  con=connection()
  cur=con.cursor()
  cur.execute("SELECT * FROM SHOWS WHERE SDATE='%s'"%(SDATE))
  data=cur.fetchall()
  if len(data)==0:
    print(" "*20,"|"," Show Not Available ", sep="")
    input()
  else:
    i=1
    SH=[]
    for d in data:
      S=d[3].split("|")
      for j in range(len(S)):
        print(" "*19,"|","Show %d : "%(i),d[1],S[j])
        SH+=[{"SID":d[0],"SN":j}]
        i+=1
    print(" "*20,"|"," Show NO ? ", sep="",end="")
    sno=input()
    if sno=="":
      print(" "*20,"|"," Don't Leave Blank ", sep="")
    elif not sno.isdigit():
      print(" "*20,"|","Text Not Allowed",sep="")
    elif int(sno)<1 or int(sno)>i-1:
      print(" "*20,"|","Total Shows = "+str(i-1),sep="")
      input()
    else:
      available_seats(SH[int(sno)-1])
      


def menu():
  os.system("cls")
  print("="*70)
  print("\n"*4)
  print(" "*20,"+","="*30,"+", sep="")
  print(" "*20,"|", "PVR CINEMA".center(30), "|", sep="")
  print(" "*20,"|", "Movie Ticket Booking System".center(30),"|",sep="")
  print(" "*20,"+","-"*30,"+",sep="")
  print(" "*20,"|","MAIN MENU".center (30),"|",sep="")
  print(" "*20,"+","-"*30,"+",sep="")
  print(" "*20,"|","%-30s"%("1. Movie Maintainance Menu"),"|",sep="")
  print(" "*20,"|","%-30s"%("2. Book Tickets"),"|", sep="")
  print(" "*20,"|","%-30s"%("0. EXIT"),"|", sep="")
  print(" "*20, "+","="*30,"+", sep="")
  print("\n"*4)
  print("="*70)
  choice=input("Enter your choice : ")
  if choice=="":
    print(" "*20,"|","Don't Leave Blank",sep="")
    input()
    menu()
    return
  if not choice.isdigit():
    print(" "*20,"|","Text Not Allowed",sep="")
    input()
    menu()
    return
  choice=int(choice)
  if choice==0:
    print(" "*20,"|","%-30s"%("THANK YOU"),"|",sep="")
    return
  if choice==1:
      mov_maintainance()
  elif choice==2:
      checking_tickets()
      
  menu()
      


def login():
  print("="*70)
  print("\n"*4)
  print(" "*20,"+","="*30,"+", sep="")
  print(" "*20,"|", "PVR CINEMA".center (30), "|", sep="")
  print(" "*20,"|", "Movie Ticket Booking System".center (30), "|", sep="")
  print(" "*20,"|", "User Name :", sep="",end="")
  username=input ()
  print(" "*20,"|", "Password :", sep="",end="")
  password=input()
  if username=="RAKSHA" and password=="1234":  #admin id
      menu()
  else:
      print("Failed")
  input()

def main():
    welcome()
    login()

main()
