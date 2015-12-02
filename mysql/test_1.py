#!/usr/bin/python  
#-*-coding:utf-8-*-


import mysql.connector
import os
import sys
import time

appcrawler_user = ''
appcrawler_password = ''
appcrawler_host = ''

ostore_user = ''
ostore_password = ''
ostore_host = ''

class Db_sync:

    url_list = [];

    app_limit = 100
    app_offset = 0
    total = 0

    def __init__(self):

        self.run();

    def run(self):
        self.connect_mysql()
        self.total = self.app_total[0][0]
        print self.total
        while self.app_offset < self.total:
            self.query_appcrawler()
            for app_tuple in self.app_select_list:
                self.query_os_app(app_tuple[0], app_tuple[1], app_tuple[2])   ####  package_name,  download_url,  signature
##                break
            self.app_offset += self.app_limit
##            break

        print 'done!!'

    def connect_mysql(self):
        try:
            self.conn_appcrawler = mysql.connector.connect(user=appcrawler_user,password=appcrawler_password,host=appcrawler_host,database='appcrawler')
            self.cur_appcrawler = self.conn_appcrawler.cursor()
            self.cur_appcrawler.execute('select count(*) from app where public_key is not null')
            self.app_total = self.cur_appcrawler.fetchall()
            
            self.conn_ostore = mysql.connector.connect(user=ostore_user,password=ostore_password,host=ostore_host,database='ostore')
            self.cur_ostore = self.conn_ostore.cursor()
        
        except Exception,ex:
            print "line = 43 mysql error %s"%ex

    def query_appcrawler(self):
        try:
            self.cur_appcrawler.execute('select package_name, download_url, file_md5 from app where public_key is not NULL limit %d offset %d'%(self.app_limit, self.app_offset))
            self.app_select_list= self.cur_appcrawler.fetchall()

            ##print self.url_list

        except Exception,ex:
            print "line = 53 mysql error %s"%ex

    def query_os_app(self, package_name, download_url, signature):
        try:
            self.cur_ostore.execute('update os_app set apk_public_key = \'%s\' where app_package = \'%s\' and download_url = \'%s\' '%(str(signature), package_name, download_url))
            self.conn_ostore.commit()

##########################################  for  test 
##            self.cur_ostore.execute('update os_app set apk_public_key = NULL , download_url = \'%s\' where app_package = \'%s\' '%(download_url, package_name))
##            self.conn_ostore.commit()

###############################################         

        except Exception,ex:
            print "line = 68 mysql error %s"%ex
            print 'update os_app set apk_public_key = %s where app_package = %s and download_url = %s'%(signature, package_name, download_url)


if __name__ == '__main__':

    db_sync = Db_sync();





    

    



    
