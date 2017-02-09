#!/usr/bin/python
#-*-coding:utf-8-*-


import os
import sys
import time
import string
import requests
from HTMLParser import HTMLParser


class myHTMLParser(HTMLParser):
    is_r_content = False
    is_r_app_detail_shadow = False
    is_r_app_details_info = False
    is_description_c_6 = False
    is_f18_title_c_3 = False
    is_info = False
    
    is_r_app_unfold_r_app_up = False
    is_mobo_apk_info = False

 

    

    def handle_starttag(self, tag, attrs):
##        print 'Encounter the beginning of a %s tag  %s' % (tag, attrs)
        if tag == 'div' and attrs[0][0] == 'class' and attrs[0][1] == 'r-content':
            self.is_r_content = True
            return

        print '------ tag %s  attrs %s'%(tag, attrs)
        
        if tag == 'div' and attrs[0][0] == 'class' and attrs[0][1] == 'r-app-detail shadow':
            self.is_r_app_detail_shadow = True
            return
        
        if tag == 'div' and attrs[0][0] == 'class' and attrs[0][1] == 'r-app-details-info':
            self.is_r_app_details_info == True
            return
        
        if tag == 'div' and attrs[0][0] == 'class' and attrs[0][1] == 'description c-6':
            self.is_description_c_6 = True
            return
        
        if tag == 'h3' and attrs[0][0] == 'class' and attrs[0][1] == 'f18 title c-3':
            self.is_f18_title_c_3 = True
            return
        
        if tag == 'div' and attrs[0][0] == 'class' and attrs[0][1] == 'info':
            self.is_info = True
            return

        if self.is_info == True:
            print '------ tag %s  attrs %s'%(tag, attrs)
            if tag == 'a' and attrs[0][0] == 'class' and attrs[1][1] == 'r-app-unfold':
                self.is_r_app_unfold_r_app_up = True
                return

            if tag == 'div' and attrs[0][0] == 'class' and attrs[0][1] == 'mobo-apk-info':
                self.is_mobo_apk_info = True
                return
        
    def handle_endtag(self, tag):

        return
##        print 'Encounter the end of a %s tag' % tag
    
            
    def handle_data(self, data):

        if self.is_r_app_unfold_r_app_up and self.is_mobo_apk_info and self.is_r_content :
            return
        
        if self.is_r_app_detail_shadow and self.is_r_app_details_info and self.is_description_c_6 :
            if self.is_f18_title_c_3 :
                print 'Encounter head title:' + data

            if self.is_info :
                print '------' + data



class CrawlerTest:

    url_list = [];
    url = 'http://www.mobogenie.com/download-iquran-lite-2443498.html'


    def __init__(self):
        self.m = myHTMLParser()
        self.run();

    def run(self):
        r = requests.get(self.url)
        if(r.status_code == 200):
            html = r.text.encode('utf-8')
            print len(html)

            self.m.feed(html)
            self.m.close()
        
             
            

        print 'done!!'
        
      



if __name__ == '__main__':
##    a = '<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">\
##    <html><head><!--insert javaScript here!--><title>test</title><body><a href="http: //www.163.com">链接到163</a></body></html>'

##    print a
##    m = myHTMLParser()
##    m.feed(a)
##    m.close()

    crawlerTest = CrawlerTest();
