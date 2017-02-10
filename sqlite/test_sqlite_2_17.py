#!/usr/bin/python
#-*-coding:utf-8-*-

import sqlite3
import os
import sys
import time
import string
import stem_word_root


    
class SqliteTest:

    def __init__(self):
        self.run()

    def run(self):
        print 'start'

    def connect(self):
        conn = sqlite3.connect(":memory:")
        self.cu = conn.cursor()

    def create_table(self) :
        sql_create_category = 'create table category_list (\'id\' integer PRIMARY KEY autoincrement, \'is_game\' bool, \'key_word\' varchar(30) )'
        self.cu.execute(sql_create_category)

        sql_create_url = 'create table url_list ( \'id\' integer PRIMARY KEY autoincrement, \'url\' varchar(100), \'category\' varchar(30) )'
        self.cu.execute(sql_create_url)

        sql_create_app = 'create table  app_list ( \'id\' integer PRIMARY KEY autoincrement, \' app_name\' varchar(50), package_name varchar(100), \'category\' varchar(50),  \'description\' varchar(2000) )'
        self.cu.execute(sql_create_app)

    def test(self):

        sql = 'insert'
        


if __name__ == '__main__':

##    sqliteTest = SqliteTest();
    conn = sqlite3.connect(":memory:")
    cu = conn.cursor()

    sql = 'create table category_list (\'id\' integer PRIMARY KEY autoincrement, \'is_game\' bool, \'key_word\' varchar(30) )'
    cu.execute(sql)

    sql = 'create table url_list (\'id\' integer PRIMARY KEY autoincrement, \'url\' varchar(100) , \'category\' varchar(30) ) '
    cu.execute(sql)

    sql = 'create table app_list (\'id\' integer PRIMARY KEY autoincrement, \'app_name\' varchar(50), package_name varchar(100), \'category\' varchar(50), \'description\' varchar(2000) )'
    cu.execute(sql)


    cu.execute('select name from sqlite_master where type = \'table\' ')
    a = cu.fetchall()
    print a


    
