#!/usr/bin/python
#-*-coding:utf-8-*-

import os
import sys
import time
import string
import requests
import base64
from urllib import urlencode



if __name__ == '__main__':

    ##url='http://localhost:8080/api/search?q=%E4%B8%80&page=1'
    ##url='http://apps.tclclouds.com/api/search?q=baidu&page=1'
    ##url='http://apps.tclclouds.com/api/search?q=%E5%86%9C%E6%9D%91%E7%A6%BB%E5%A9%9A%E7%9B%B8%E4%BA%B2&page=1'

    data = {'q' : '测试'}


    ##url='http://localhost:8080/api/search?%s&page=1'%(urlencode(data))
    ##url='http://localhost:8080/search?%s&page=1'%(urlencode(data))


    ##url='http://apps.tclclouds.com/api/search?%s&page=1'%(urlencode(data))
    url='http://apps-test.tclclouds.com/api/search?%s&page=1'%(urlencode(data))
    ##url='http://10.128.208.195:8086/api/search?%s&page=1'%(urlencode(data))
    print url
    
    ##url='http://apps.tclclouds.com/api/search?q=test&page=1&per_page=10'
    r = requests.get(url)
    if(r.status_code == 200):
        respone = r.text.encode('utf-8')

        ##res_list = respone.split(":")

        res_base64 = eval(respone)["result"]

        
        app_search_dict = eval(base64.decodestring(res_base64))

        app_list = app_search_dict["items"]

        i = 1
        for x in app_list :
            print "i = %d id = %d------ name = %s"%(i, x["id"], x["name"].decode('utf-8'))
            i += 1

    print "done!!"
    
