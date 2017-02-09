#!/usr/bin/python
#-*-coding:utf-8-*-

import os
import sys
import time
import string
import requests

if __name__ == '__main__':

    ##url='http://localhost:8080/search?q=QQ&page=2'
    ##url='http://apps-test.tclclouds.com/api/search?q=test&page=5'
    ##url='http://apps.tclclouds.com/api/search?q=test&page=1&per_page=10'

    website = 'http://apps-test.tclclouds.com'
    ##website = 'http://localhost:8080'
## 1_url  469.134ms    145.392  69.194
## 2_url  259.241ms    55    24.382

    timeout_url_list = []
    input_file_path = 'D:/api_log/1_url.txt'


    input_file = open(input_file_path, 'r')

    time_total = 0
    cnt = 0
    for line in input_file:
        url = website + line
 
        r = requests.get(url)
        if(r.status_code == 200):
            respone = r.text.encode('utf-8')
            time_cur = r.elapsed.microseconds/1000%1000
            time_total += time_cur
            cnt += 1
            print time_cur

            if time_cur > 100 :
                timeout_url_list.append(line)

        time.sleep(1)
        
        

    print "\n\nthe avg time is %d.%d\n\n"%(time_total/cnt, time_total%cnt)
    print "done!!"

    for x in timeout_url_list:
        print x
    
