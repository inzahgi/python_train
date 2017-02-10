#!/usr/bin/python
#-*-coding:utf-8-*-

import sqlite3
import os
import sys
import time
import string

    
class SqliteTest:

    table_name_list = ['description_data']

    def __init__(self):
        self.run()
        

    def run(self):
        print 'start'
        self.connect()
        self.check_table_exist()
        
        ##self.test()


        ##self.cu.close()
        ##self.conn.close()
        

    def connect(self):
        self.conn = sqlite3.connect(":memory:")
        ##self.conn = sqlite3.connect("mobogenie.db")
        self.cu = self.conn.cursor()
        
    def close(self):
        self.cu.close()
        self.conn.close()

    def check_table_exist(self):
        self.cu.execute('select name from sqlite_master where type = \'table\' ')
        query_res = self.cu.fetchall()

        exist_table = set()
        for i in range(len(query_res)) :
            exist_table.add(query_res[i][0])
        
        for table in self.table_name_list :
            if table not in exist_table :
                print 'not found %s! create it'%table
                self.create_table(table)

    def create_table(self, table_name):
        sql = ''
        if(table_name == 'description_data') :
            sql = '''create table description_data (\'id\' integer PRIMARY KEY autoincrement, \'app_id\' integer, 
                    \'category\' varchar(100), \'app_game\' varchar(100), \'data\' varchar(10000),
                    \'is_english\' integer, \'stem_data\' varchar(10000), \'tag\' varchar(1000))'''
        else:
            print 'table name is wrong'
            return
        
        self.cu.execute(sql)

    def insert_data(self, app_id, category, app_game, data):
##        sql = 'insert into description (\'app_id\', \'category\', \'app_game\', \'data\', \'is_english\', \'stem_data\', \'tag\')\
##                values (%d, \'%s\', \'%s\', \'%s\', %d, \'%s\', \'%s\' )'%(category, app_game, data, is_english, stem_data, tag)
        sql = 'insert into description (\'app_id\', \'category\', \'app_name\', \'data\') values (%d, %s, %s, %s)'
        self.cu.execute(sql)
        self.conn.commit()

    def update_category_key_word(self, table_name, category_english, key_word):

        sql = 'update %s set key_word = \'%s\' where category_english == \'%s\' '%(table_name, key_word, category_english)
        print sql
        self.cu.execute(sql)
        self.conn.commit()
        
    def print_test(self, table):
        sql = 'select * from %s'%table
        self.cu.execute(sql)
        a = self.cu.fetchall()
        print a
        
        
    def test(self):
        self.insert_category('一二', 'aaaaa', 'www.baidu.com')
        self.insert_category('三四', 'bbbbb', 'www.cctv.com')
'''
        self.insert_url('www.baidu.com', 'key_word')
        self.insert_url('www.taobao.com', 'two piece')

        self.insert_app('weixin', 'com.tencent.weixin', 'communication', 'aaaaaaaaaaaa')
        self.insert_app('QQ', 'com.tencent.qq', 'communication', 'bbbbbbbbbb')

        self.print_test('category_list')
        self.print_test('url_list')
        self.print_test('app_list')
'''        




if __name__ == '__main__':

    sqliteTest = SqliteTest();

