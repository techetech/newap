# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 09:57:20 2025

@author: jadon
"""

import streamlit as st
import sqlite3
from streamlit_option_menu import option_menu

def connect_db():
    con=sqlite3.connect("DCEBATCH4.db")
    return con
def create_table():
    con=connect_db()
    cur=con.cursor()
    cur.execute('create table if not exists student (roll int primary key,name text,password text,branch text)')
    con.commit()
    con.close()

def add_record(data):
    con=connect_db()
    cur=con.cursor()
    try:
        cur.execute('Insert into student(roll,name,password,branch) values(?,?,?,?)',data)
        con.commit()
        con.close()
    except sqlite3.IntegrityError:
        st.error("User Already Registered")
        con.close()
    
def view_record():
    con=connect_db()
    cur=con.cursor()
    cur.execute('Select * from student')
    result=cur.fetchall()
    con.close()
    return result

def disp():
    data=view_record()    
    st.table(data)
    
def signup():
    st.title("Registration Page")
    roll=st.number_input('enter your roll number',format='%d')
    name=st.text_input('enter your name')
    branch=st.selectbox('Branch', options=['CSE','AIML','CSIT','IOT','ME','ECE','ECS'])
    password=st.text_input('password',type='password')
    repass=st.text_input('Re type password')
    if st.button('Sign in'):
        if password!=repass:
            st.error("Wrong password")
        else:
            add_record((roll,name,password,branch))
            st.success("Student Registered")

create_table()

with st.sidebar:
    selected=option_menu('Select from here',['SignUp','Display All Record'])
    
if selected == 'SignUp':
    signup()
elif selected=='Display All Record':
    disp()
else:
    pass