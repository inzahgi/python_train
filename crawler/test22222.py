#coding:utf-8

import random
import socket
import urllib.request
#import cookielib
import http.cookiejar
from html.parser import HTMLParser
import re

pattern = re.compile(r'http://heart.39.net/*?')

ERROR = {
        '0':'Can not open the url,checck you net',
        '1':'Creat download dir error',
        '2':'The image links is empty',
        '3':'Download faild',
        '4':'Build soup error,the html is empty',
        '5':'Can not save the image to your disk',
    }
######################################################################################################
######################################################################################################
class MyHTMLParser(HTMLParser):
    text_str = ''
    title_str = ''

    a_title = False
    a_start = False
    a_txt =False

    web_list = []
    total = 0
    def handle_starttag(self, tag, attrs):
        if tag == 'title':
            self.a_txt = True
            self.a_title = True
            print("Encountered tittle start tag:", tag)
            
        if tag == 'div': 
           for name1,value1 in attrs:
               if ((name1 == 'id')and(value1 == 'contentText')):
                    self.a_start = True
                    print("Encountered text start tag:", tag)
               if ((name1 == 'class') and (value1 == 'implant_box')):
                    self.a_start = False
                    print("Encountered text end tag:", tag)

        if tag=='a':
            for name, value in attrs:
                if(name == 'href'):
                     match = pattern.match(value)
                     if(match):
                         if value in  self.web_list:
                             return
                         else:
                            self.total=self.total+1
                            self.web_list.append(value)
        if tag == 'p':
            self.a_txt = True
                    
                    
    def handle_endtag(self, tag):
        if tag == 'title':
            self.a_txt = False
            self.a_title = False
            print("Encountered tittle end tag :", tag)

        if tag == 'p':
            self.a_txt = False

        ##if tag == 'div':
            ##if self.a_txt:
            ##self.a_txt = False
                ##print("Encountered an end tag :", tag)
                
    def handle_data(self, data):
        if self.a_txt and self.a_title:
            self.title_str += data
            print("Encountered some data  :", data)
        if self.a_txt and self.a_start:
            self.text_str += data
            print("Encountered some data  :", data)

#######################################################################################################
#######################################################################################################
class BrowserBase(object): 

    def __init__(self):
        socket.setdefaulttimeout(20)

    def speak(self,name,content):
        print ('[%s]%s' %(name,content))

    def openurl(self,url):
        """
        打开网页
        """
        cookie_support= urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar())
        self.opener = urllib.request.build_opener(cookie_support,urllib.request.HTTPHandler)
        urllib.request.install_opener(self.opener)
        user_agents = [
                    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
                    'Opera/9.25 (Windows NT 5.1; U; en)',
                    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
                    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
                    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
                    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
                    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
                    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 ",

                    ] 
       
        agent = random.choice(user_agents)
        self.opener.addheaders = [("User-agent",agent),("Accept","*/*"),('Referer','http://www.google.com')]
        try:
            res = self.opener.open(url)
            ##print (res.info())
            ##print (res.read())
        except Exception as e:
            self.speak(str(e)+url)
            raise Exception
        else:
            return res

if __name__=='__main__':
    ##url = 'http://heart.39.net/a/130601/4180911.html'
    ##url = 'http://ek.39.net/a/140130/4326212.html'
    url = 'http://heart.39.net/gxy/'
    splider=BrowserBase()
    fp = splider.openurl(url)
    mybytes = fp.read()
    ##mystr = mybytes.decode('gb2312','ignore')
    mystr = mybytes.decode('gb2312','ignore')
    fp.close()
    ##print (mystr)

    parser = MyHTMLParser(strict=False)
    parser.feed(mystr)
    print (parser.title_str)
    print (parser.text_str)

    print("总数：", parser.total)
    for i in range(len(parser.web_list)):
        print(parser.web_list[i])
    print("结束")
