#!/usr/bin/python
#-*-coding:utf-8-*-


import os
import sys
import time
import string
import requests
from HTMLParser import HTMLParser


class myHTMLParser(HTMLParser):

    category_list = []
    category_url_dict = {}
    
    url_temp = ''
    category_name = ''

    is_w_popular_keyword = False
    is_a_href = False
 
    def handle_starttag(self, tag, attrs):
##        print 'Encounter the beginning of a %s tag  %s' % (tag, attrs)
        if tag == 'div' and attrs[0][0] == 'class' and attrs[0][1] == 'w-popular-keyword' :
            self.is_w_popular_keyword = True
            return

        if self.is_w_popular_keyword and tag == 'a' :
            self.is_a_href = True
            self.url_temp = attrs[0][1]

        
    def handle_endtag(self, tag):
        if self.is_w_popular_keyword :
            if tag == 'a' :
                self.is_a_href = False
                
                self.category_url_dict[self.category_name] = self.url_temp
                self.category_list.append(self.category_name)
                
                self.category_name = ''
                self.url_temp = ''
                return
                
            if tag == 'div' :
                self.is_w_popular_keyword = False
                return

            
    def handle_data(self, data):
        if self.is_w_popular_keyword and self.is_a_href :
            ##print '-----' + data
            self.category_name += data




class CrawlerTest:

    url_list = [];
    ##url = 'http://www.mobogenie.com/download-iquran-lite-2443498.html'
    url = 'http://www.mobogenie.com/apps/categories-0-downloads_1'
    ##url = 'http://www.mobogenie.com/games/categories-0-downloads_1'


    def __init__(self):
        self.m = myHTMLParser()
        self.run();

    def run(self):
        r = requests.get(self.url)
        if(r.status_code == 200):
            html = r.text.encode('utf-8')
            print len(html)

            self.m.feed(html)

            self.printf(self.m)
            
            self.m.close()
        
             
            

        print 'done!!'
    def printf(self, m):

        for category in m.category_list :
            print category

        print '\n\n'

        for key, value in m.category_url_dict.items() :
            print '--- %s ---  %s'%(key, value)
        
      



if __name__ == '__main__':
##    a = '<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">\
##    <html><head><!--insert javaScript here!--><title>test</title><body><a href="http: //www.163.com">链接到163</a></body></html>'

##    print a
##    m = myHTMLParser()
##    m.feed(a)
##    m.close()

    crawlerTest = CrawlerTest();
