#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import datetime

if __name__ == '__main__':
    start_time = '2015-09-22 00:00:00'
    start_date_time = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
    ##print start_date_time.ctime()
    
    delta = datetime.timedelta(hours = 1)
    tmp_time_1 = start_date_time
    
    for i in range(200):
        ##tmp_time = start_date_time + delta
        tmp_time_2 =tmp_time_1 +delta
        
        ##print tmp_time_2
        
        print 'insert into log select * from log_test where created_time >= \'%s\' and created < \'%s\' '%(tmp_time_1, tmp_time_2)
        tmp_time_1 = tmp_time_2;
