#!/usr/bin/python
#-*-coding:utf-8-*-


import os
import sys
import time
import string
import requests
from HTMLParser import HTMLParser


class myHTMLParser(HTMLParser):

    category = ''
    app_name = ''
    description = ''
    package_name = ''
    

## for category
    is_r_content = False
    a_cnt = 0
    

## for app name
    is_info_con = False
    is_name = False
    is_te = False

## for descrption
    is_description_c_6 = False
    is_f18_title_c_3 = False
    is_info = False
    
##    is_r_app_unfold_r_app_up = False
##    is_mobo_apk_info = False


## for package name
    is_mobo_apk_block = False
    is_mobo_apk_title = False


    

    def handle_starttag(self, tag, attrs):
##        print 'Encounter the beginning of a %s tag  %s' % (tag, attrs)
        if tag == 'div' and attrs[0][0] == 'class' and attrs[0][1] == 'r-content' :
            self.is_r_content = True
            ##print '   self.is_r_content ' + str(self.is_r_content)
            return 

        if self.is_r_content and tag == 'a' :
            self.a_cnt += 1


        if tag == 'div' and attrs[0][0] == 'class' and attrs[0][1] == 'info-con' :
            self.is_info_con = True
            return

        if self.is_info_con and tag == 'p' and len(attrs) != 0 :
            if attrs[0][0] == 'class' and attrs[0][1] == 'name':
                self.is_name = True
                return

        if self.is_name and tag == 'a' and attrs[1][0] == 'class' and attrs[1][1] == 'te' :
            self.is_te = True
            return
        
        if tag == 'div' and attrs[0][0] == 'class' and attrs[0][1] == 'description c-6':
            
##            print 'Encounter the beginning of a %s tag  %s' % (tag, attrs)
            self.is_description_c_6 = True
            return
        
        
        if tag == 'div' and attrs[0][0] == 'class' and attrs[0][1] == 'info':
            self.is_info = True
            return

        if tag == 'div' and attrs[0][0] == 'class' and attrs[0][1] == 'mobo-apk-block' :
            self.is_mobo_apk_block = True
            print 'mobo_apk_block ' + str(self.is_mobo_apk_block)
            return

        if self.is_mobo_apk_block :
##            print '    %s   %s'%(tag, attrs)
            if tag == 'p' and len(attrs) != 0 :
                if attrs[0][0] == 'class' and attrs[0][1] == 'mobo-apk-title' :
                    self.is_mobo_apk_title = True
                    ##print 'mobo_apk_title ' + str(self.is_mobo_apk_title)
                    return


        
    def handle_endtag(self, tag):
               
##        print 'Encounter the end of a %s tag' % tag

        if self.a_cnt == 3 and tag == 'a':
            self.is_r_content = False

        if self.is_te and tag == 'a':
            self.is_te = False
            self.is_name = False
            self.is_info_con = False
        
        if  self.is_description_c_6 and tag == 'div' :
            self.is_description_c_6 = False

        if  self.is_mobo_apk_block and self.is_mobo_apk_title and tag == 'span' :
            self.is_mobo_apk_title = False
            self.is_mobo_apk_block = False
            
    def handle_data(self, data):

        if self.is_r_content and self.a_cnt == 3:
            ##print '    category :' + data
            self.category += data
            return
            
        if self.is_te and self.is_name and self.is_info_con :
            ##print '    app name :' + data
            self.app_name  += data
            return

        if self.is_description_c_6 :
            if self.is_info :
                ##print '------ data :' + data
                self.description += data
                return
                
        
        if self.is_mobo_apk_block and self.is_mobo_apk_title :
            if data != 'Package Name':
                ##print '------ package Name :' + data
                self.package_name += data


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

            print 'category: %s\napp_name: %s\ndescription: %s\npackage_name: %s\n'%( \
                self.m.category, self.m.app_name, self.m.description, self.m.package_name)
            
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
