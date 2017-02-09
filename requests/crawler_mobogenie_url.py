#!/usr/bin/python
#-*-coding:utf-8-*-


import os
import sys
import time
import string
import requests
from HTMLParser import HTMLParser


class myHTMLParser(HTMLParser):

    url_list = []
    
    

    is_r_app_category_cf = False
    is_hbox = False
    is_a_href = False
 
    def handle_starttag(self, tag, attrs):
##        print 'Encounter the beginning of a %s tag  %s' % (tag, attrs)
        if tag == 'ul' and attrs[0][0] == 'class' and attrs[0][1] == 'r-app-category cf' :
            self.is_r_app_category_cf = True
            return

        if self.is_r_app_category_cf and tag == 'li' and attrs[0][0] == 'class' and attrs[0][1] == 'hbox' :
            self.is_hbox = True
            return

        if self.is_hbox and tag == 'a' and len(attrs) >= 2 :
            if attrs[1][0] == 'class' and attrs[1][1] == 'pic' :
                self.is_a_href = True
                ##print attrs[0][1]
                self.url_list.append(attrs[0][1])


        
    def handle_endtag(self, tag):
        if self.is_a_href :
            if tag == 'a' :
                self.is_a_href = False
                self.is_h_box = False

                return
        if self.is_r_app_category_cf and tag == 'ul' :
            self.is_r_app_category_cf = False
                

            
##    def handle_data(self, data):
##        if self.is_w_popular_keyword and self.is_a_href :
            ##print '-----' + data
##            self.category_name += data




class CrawlerTest:

    url_list = [];
    ##url = 'http://www.mobogenie.com/download-iquran-lite-2443498.html'
    ##url = 'http://www.mobogenie.com/apps/categories-0-downloads_1'
    ##url = 'http://www.mobogenie.com/games/categories-0-downloads_1'

    url = 'http://www.mobogenie.com/apps/categories-0-downloads_'


    def __init__(self):
        self.m = myHTMLParser()
        self.run();

    def run(self):
        for i in range(1, 11):
            print i
            r = requests.get(self.url + str(i))
            if(r.status_code == 200):
                html = r.text.encode('utf-8')
                print len(html)

                self.m.feed(html)

                self.printf(self.m)

                self.m.url_list = []
            
        self.m.close()
        
             
            

        print 'done!!'
    def printf(self, m):

        for category in m.url_list :
            print category

        

        print '\n\n'

        
      



if __name__ == '__main__':
##    a = '<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">\
##    <html><head><!--insert javaScript here!--><title>test</title><body><a href="http: //www.163.com">链接到163</a></body></html>'

##    print a
##    m = myHTMLParser()
##    m.feed(a)
##    m.close()

    crawlerTest = CrawlerTest();
