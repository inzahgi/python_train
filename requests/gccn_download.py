#!/usr/bin/python
#-*-coding:utf-8-*-


import os
import sys
import time
import string
import requests




class CrawlerTest:


    url = 'http://test.gccn.tclclouds.com/gccn-api/api/categoryinfo/'


    def __init__(self):
        self.run();

    def run(self):
        for i in range(1, 11):
            print i
            payload = {'uncompress' : '1',
                       'category_id':'13',
                       'offset': '0',
                       'imei':'0.93382115635460',
                       'imsi':'460017219804029',
                       'model':'ALCATEL+ONE+TOUCH+BROWSER',
                       'language':'en_US',
                       'screen_size':'800%23480',
                       'network':'WIFI',
                       'req_from':'0',
                       'version_code':'60',
                       'version_name':'3.1',
                       'os_version_code':'10',
                       'os_version':'4.2.2',
                       'channel':'TCL'}
            r = requests.post(self.url, params=payload)
            if(r.status_code == 200):
                ##print r.json()["data"]["apps"][0]["downloadUrl"]
                url = r.json()["data"]["apps"][0]["downloadUrl"]
                ##html = r.text.encode('utf-8')
                ##print len(html)
                ##print dir(html)

                ##print html["data"]["apps"][0]["downloadUrl"]

                cmd = 'wget -O %d.apk %s'%(i, url)
                print cmd
                ##os.system(cmd)

        
             
            

        print '\n\ndone!!'
        

        print '\n\n'

        
      



if __name__ == '__main__':
##    a = '<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">\
##    <html><head><!--insert javaScript here!--><title>test</title><body><a href="http: //www.163.com">链接到163</a></body></html>'

##    print a
##    m = myHTMLParser()
##    m.feed(a)
##    m.close()

    crawlerTest = CrawlerTest();
