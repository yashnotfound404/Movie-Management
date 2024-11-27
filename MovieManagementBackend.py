import streamlit as st

st.title("BACKEND FOR MANAGEMENT")
st.subheader("")



import mysql.connector as sql1
import random
from getpass import getpass
b='<your password here>'
db = sql1.connect(host='localhost', user="root",passwd=b)
cur = db.cursor()
cur.execute("Show Databases")
dbs = []

#Connection/Creation of Databse

for x in cur:
    dbs += x
if ('movi' not in dbs):
    # st.write('\n The Database is missing. \n', '〰️'*15)
    # st.write('Creating Database...')
    cur.execute("CREATE DATABASE movi")
    cur.execute("Show Databases")
    dbs = []
    for x in cur:
        dbs += x
    if 'movi' in dbs:
        st.write('Database created successfully!...')
    else:
        st.write("Unable to create Database...")
# else:
#     st.write('Database Found...')

cur.execute("use movi")
if db.is_connected():
    st.write('Connected to Database...')
else:
    st.write('Couldn\'t connect to database...')



#Table Named movie is created


cur.execute("Show tables")
tbs = []
for x in cur:
    tbs += x
if 'movie' not in tbs:
    # st.write('\n Table is missing. \n', '〰️'*13)
    # st.write('Creating Table...')
    cur.execute('create table movie(naam varchar(15), phno bigint(11), tic int(2), fnam varchar(20), lnam varchar(20), pswd varchar(20), usrid varchar(10));')
    cur.execute("Show tables")
    tbs = []
    for x in cur:
        tbs += x
        if 'movie' not in tbs:
            st.write('unable to create table...')
        # else:
        #     st.write('MySQL Table Created!')
# else:
    # st.write("table found....")

#Front Row Table

if 'frow' not in tbs:
    # st.write('\n A Table is missing. \n', '〰️'*13)
    # st.write('Creating Table...')
    cur.execute('create table frow(naam varchar(15), phno bigint(11), tic int(2), fnam varchar(20), lnam varchar(20), pswd varchar(20), usrid varchar(10));')
    cur.execute("Show tables")
    tbs = []
    for x in cur:
        tbs += x
    if 'frow' not in tbs:
        st.write('unable to create table...')
    # else:
    #     st.write('Table Created!')
# else:
#     st.write("table found...")


#Upper Row Table

if 'upcb' not in tbs:
    # st.write('\n A Table is missing. \n', '〰️'*13)
    # st.write('Creating Table...')
    cur.execute('create table upcb(naam varchar(15), phno bigint(11), tic int(2),fnam varchar(20), pswd varchar(20), usrid varchar(10));')
    cur.execute("Show tables")
    tbs = []
    for x in cur:
        tbs += x
    if 'upcb' not in tbs:
       st.write('unable to create table...')
    # else:
    #     st.write('Table Created!')
# else:
#     st.write("table found...")


#PRINTING STARTS


st.write('''

Welcome to Movie Management system by Yash Mishra

''')
st.write('\n'*20)


#Functioning


def sup():

    naam = st.text_input("Enter the movie name :")
    phno = st.number_input("Enter phone number :")
    fnam = st.text_input("Enter your first name :")
    lnam = st.text_input("Enter your last name :")
    tic = st.number_input("Enter total tickets :")
    pswd = st.text_input("Enter your passwd :")
    idd = [0]
    usrid = 0
    cur.execute('select usrid from movie')
    if st.button("Submit"):
        st.write(f"Movie Name: {naam}, Phone: {phno}, Ticket: {tic}")
        for x in cur:
            idd += x
        iddd = 0
        while iddd in idd:
            iddd = random.randint(1000, 3000)
            usrid = iddd
        st.write("User ID is: ", {usrid})
        v_ins = "insert into movie values( '{}','{}','{}','{}','{}','{}','{}');".format(naam, phno, tic, fnam, lnam, pswd, usrid)
        cur.execute(v_ins)
        db.commit()
        st.write(" General Ticket Booked \n\n")


def frt():
    st.write("Front Row Booking")
    aa = st.text_input("Enter your movie name : ")
    bb = st.text_input("Enter your first name : ")
    ee = st.text_input("Enter your last name: ")
    cc = st.number_input("Enter total tickets : ")
    dd = st.number_input("Enter your ph_no : ")
    pswd = st.text_input("Enter the password : ")
    idd = [0]
    usrid = 0
    cur.execute('select usrid from frow')
    for x in cur:
        idd += x
        iddd = 0
    while iddd in idd:
        iddd = random.randint(1, 1000)
        usrid = iddd
    else:
        st.write("User ID is: ", {usrid})
    v_ins = "insert into frow values( '{}','{}','{}','{}','{}','{}','{}')".format(
    aa, dd, cc, bb, ee, pswd, usrid)
    cur.execute(v_ins)
    db.commit()
    st.write(" **TICKET BOOKED** \n\n")
def upcb():
    st.write("Upper Circle booking")
    a = st.text_input("Enter your name : ")
    b = st.text_input("Enter your movie name : ")
    c = st.number_input("Enter your ph_no : ")
    d = st.number_input("Enter total tickets : ")
    pswd = st.text_input("Enter the password : ")
    idd = [0]
    usrid = 0
    cur.execute('select usrid from upcb')
    for x in cur:
        idd += x
    iddd = 0
    while iddd in idd:
        iddd = random.randint(3000, 9999)
        usrid = iddd
    else:
        st.write("User ID is: ", usrid)
    v_ins = "insert into upcb values( '{}','{}','{}','{}','{}','{}')".format(
    b, c, d, a, pswd, usrid)
    cur.execute(v_ins)
    db.commit()
    st.write(" ENJOY THE MOVIE AND HAVE FUN \n\n")
def delt():
    d = st.text_input('''What ticket is to be deleted:\n
    1. General ticket\n
    2. Front row ticket\n
    3. Upper circle ticket\n
    0. Abort
    [1/2/3] : ''')
    t = ''
    e = st.number_input("Enter the User ID: ")
    l = st.text_input("Enter Password : ")
    if st.button("Submit"):
        if d == 'General ticket' or 'general ticket':      
            t = 'movie'
        elif d == 'Front row ticket' or 'front row ticket':
            t = 'frow'
        elif d == 'Upper circle ticket' or 'upper circle ticket':
            t = 'upcb'
        else:
            st.write('Invalid Input\n')
        cur.execute("delete from {t} where usrid=\'{e}\' and pswd=\'{l}\'".format(t=t, e=e, l=l))
        st.write("Cancelled Ticket Successfully")
        db.commit()
def com():
    co = input('''
 ______________________________
 WARNING 
 You may end up loosing data if
 wrong command is entered
 *
 do not terminate your commands
 ______________________________
: ''')
    cur.execute(co)
    om = cur.fetchall()
    for x in om:
        st.write({x})
    st.write("\n\n\n")


def mnu():
    st.write("\n1. General Ticket")
    st.write("2. Front row ticket booking")
    st.write("3. Upper circle booking")
    st.write("4. see table")
    st.write("5. Cancel ticket")
    st.write("6. Enter command")
    st.write("7. Exit\n")
    ch = st.radio("Choose an option:", ["1", "2", "3","4","5","6","7"])
    if ch == '1':
        sup()
    elif ch == '2':
        frt()
    elif ch == '3':
        upcb()
    elif ch == '5':
        delt()
    elif ch == '6':
        com()
    elif ch == '7':
        st.write('''▀█▀ █░█ ▄▀█ █▄░█ █▄▀ █▄█ █▀█ █░█
                 ░█░ █▀█ █▀█ █░▀█ █░█ ░█░ █▄█ █▄█
                 █▀▀ █▀█ █▀█ █░█ █ █▀ █ ▀█▀ █ █▄░█ █▀▀ ░
                 █▀░ █▄█ █▀▄ ▀▄▀ █ ▄█ █ ░█░ █ █░▀█ █▄█ ▄''')
        quit()
    elif ch == '4':
        tbs = []
        cur.execute("Show tables")
        for x in cur:
            tbs += x
        st.write("What table you want to view ", tbs)
        a = st.text_input("Enter Table name : ")
        if a in tbs:
            cur.execute("select * from {}".format(a))
            select = cur.fetchall()
            for x in select:
                st.write('\n', {x})
            st.write("\n")
        else:
            st.write('Wrong Input\n')
    else:
        quit()


        
mnu()
