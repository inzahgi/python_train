#!/usr/bin/python
#-*-coding:utf-8-*-


import os
import sys
import time
import string
import requests
import json


url = 'http://10.128.208.137:8080/static/easyui/jquery.min.js'
##url = 'http://localhost:8080/static/easyui/jquery.min.js'

def has_max_age_0_and_no_modified_time():
    payload = {'some':'data'}
    headers = {'Accept' : '*/*',
           'Accept-Encoding' : 'zh-CN,zh;q=0.8,en-US;a=0.5,en;q=0.3',
           'Cache-Control' : 'max-age=0',
           'Connection' : 'keep=alive',
           'Host' : 'localhost:8080' ,
           'Referer' : 'http://localhost:8080/',
           'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv42.0) Gecko/20100101 Firefox/42.0',
   
           }

    r = requests.get(url, data=json.dumps(payload), headers=headers)

    ##r.text
    ###print dir(r.text)

    head = r.headers

    print r.status_code

    for key in head:
        print '---%s--------%s'%(key, head[key])

        

def has_max_age_0_and_modeified_time():
##    payload = {'some':'data'}
    headers = {
        
        'Accept' : '*/*',
        'Accept-Encoding' : 'gzip, deflate',
        'Accept-Language' : 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Cache-Control' : 'max-age=0',
        'Connection' : 'keep-alive',
        'Host' : '10.128.208.137:8080',
        'If-Modified-Since' : 'Tue, 08 Dec 2015 10:44:17 GMT',
        'If-None-Match' : 'W/"95790-1449571457212"',
        'Referer' : 'http://10.128.208.137:8080/',
        'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0'
           }

    ##r = requests.get(url, data=json.dumps(payload), headers=headers)
    r = requests.get(url, headers=headers)

    ##r.text
    ###print dir(r.text)

    head = r.headers

    print r.status_code

    for key in head:
        print '---%s--------%s'%(key, head[key])



def has_max_age_0_and_modeified_time():
    payload = {'some':'data'}
    headers = {
        'Accept' : '*/*',
        'Accept-Encoding' : 'gzip, deflate',
        'Accept-Language' : 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Cache-Control' : 'max-age=0',
        'Connection' : 'keep-alive',
        'Host' : '10.128.208.137:8080',
        'If-Modified-Since' : 'Tue, 08 Dec 2015 10:44:17 GMT',
        'If-None-Match' : 'W/"95790-1449571457212"',
##        'If-None-Match' : 'W/"95790-1449571457211"',  ## etag has change
        'Referer' : 'http://10.128.208.137:8080/',
        'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0'
           }

    r = requests.get(url,  headers=headers)

    ##r.text
    ###print dir(r.text)

    head = r.headers

    print r.status_code

    for key in head:
        print '---%s--------%s'%(key, head[key])


if __name__ == '__main__':

    has_max_age_0_and_no_modified_time();
    has_max_age_0_and_modeified_time();
    
    
        
