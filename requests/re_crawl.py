#!/usr/bin/python
#-*-coding:utf-8-*-


import os
import sys
import time
import string
import requests




class DbTest:

    file_path = './app_size_0.txt'
    url_list = [];
    url = 'http://appcrawler.tclclouds.com:8080/appcrawler/seed/immediatelyCrawler.json?id='


    def __init__(self):
        self.run();

    def run(self):

        total_cnt = 0;
        err_cnt = 0
        file = open(self.file_path)
        while 1:
            line = file.readline()
            if not line:
                break;
            ##print line
            
            a = line.split('|')
##            print self.url + a[3].strip()
##            break
##            print '%s---%s---%s'%(a[1], a[2], a[3])  ##a[3]  seed_id
            url_temp = str(self.url + a[3].strip())
            print url_temp
            
            r = requests.get(url_temp, timeout = 10)
                
            if(r.status_code != 200):
                print "------" + url_temp
                err_cnt = err_cnt + 1

            total_cnt = total_cnt + 1

           
             
            

        print 'done!!'
        print 'total: %d---err:%d'%(self.total_cnt, self.err_cnt)

       



if __name__ == '__main__':

    dbTest = DbTest();
