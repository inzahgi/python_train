# -*- coding: utf-8 -*-
import random
import socket
import urllib.request
#import cookielib
import http.cookiejar
from html.parser import HTMLParser
import re

import threading
import time
import sys
from PyQt4 import QtCore, QtGui

###################################################

pattern = re.compile(r'http://www.99.com.cn/xxg/*?')

pattern_url = re.compile(r'http://www.99.com.cn/xxg/*?')

start_url = "http://www.99.com.cn/xxg/gxy/"
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
##-----html解析
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
           ##print("Encountered tittle start tag:", tag)
            
        if tag == 'div': 
           for name1,value1 in attrs:
               if ((name1 == 'class')and(value1 == 'detail_con')):
                    self.a_start = True
                    ##print("Encountered text start tag:", tag)
               if ((name1 == 'class') and (value1 == 'writing_ad')):
                    self.a_start = False
                    ##print("Encountered text end tag:", tag)
               if ((name1 == 'class') and (value1 == 'page_byphone cc')):
                    self.a_start = False
                    ##print("Encountered text end tag:", tag)
               if ((name1 == 'class') and (value1 == 'recom_read')):
                    self.a_start = False
                    ##print("Encountered text end tag:", tag)

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
            ##print("Encountered tittle end tag :", tag)

        if tag == 'p':
            self.a_txt = False

        ##if tag == 'div':
            ##if self.a_txt:
            ##self.a_txt = False
                ##print("Encountered an end tag :", tag)
                
    def handle_data(self, data):
        if self.a_txt and self.a_title:
            self.title_str += data
            ##print("Encountered some data  :", data)
        if self.a_txt and self.a_start:
            self.text_str += data
            ##print("Encountered some data  :", data)

#######################################################################################################
#######################################################################################################
##-------获取网页信息            

####################################################################################
################################################################################
##class crawler(threading.Thread, MyHTMLParser, BrowserBase):
##---------爬虫后台线程
class crawler(QtCore.QThread):
    thread_stop = False
    def __int__(self):
        threading.Thread.__int__(self)
        socket.setdefaulttimeout(20)

    def run(self):
        
        num=1
        ########
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
        ########

        parser = MyHTMLParser(strict=False)

        website_list = []
        remove_website_set = set()
        ##url = 'http://heart.39.net/a/130601/4180911.html'
        ##url = 'http://ek.39.net/a/140130/4326212.html'
        ##url = 'http://heart.39.net/gxy/'
        global start_url
        url = start_url
        
        while (not self.thread_stop):
            ##print ("the threading is beginning!!!")
            self.emit(QtCore.SIGNAL("update(QString)"), "开始下载网页")
            time.sleep(1)

            ##fp = splider.openurl(url)
            agent = random.choice(user_agents)
            self.opener.addheaders = [("User-agent",agent),("Accept","*/*"),('Referer','http://www.google.com')]
            try:
                fp = self.opener.open(url)
            except urllib.error.HTTPError as e:  
       
                print ('The server could not fulfill the request.')
       
                print ('Error code: ', e.code ) 
       
            except urllib.error.URLError as e:  
       
                print ('We failed to reach a server.')
       
                print ('Reason: ', e.reason ) 
       
            else:
                if fp.code == 200:
                    mybytes = fp.read()
                    mystr = mybytes.decode('gb2312','ignore')
            
                    fp.close()
    
                    ##print ("the website is %s"%url)
                    self.emit(QtCore.SIGNAL("update(QString)"), "当前网址是： %s"%url)
                    parser.feed(mystr)
                    ##print (parser.title_str)
                    ##print (parser.text_str)
            
                    if len(parser.text_str) > 10:
                
                        file_object = open(parser.title_str + ".txt",'w',encoding='utf-8')
                        file_object.write(parser.text_str)
                        file_object.close()
                        self.emit(QtCore.SIGNAL("update(QString)"), parser.title_str)
                        ##print ('print file %d'%num)
                        self.emit(QtCore.SIGNAL("update(QString)"), "目前共计： %d"%num)
                        num = num+1
                    else:
                        self.emit(QtCore.SIGNAL("update(QString)"), "没有可以获取的信息")
            
                    ##print("总数：", parser.total)
                    for i in range(len(parser.web_list)):
                        ##print(parser.web_list[i])
                        if not(parser.web_list[i] in remove_website_set):
                            remove_website_set.add(parser.web_list[i])
                            website_list.append(parser.web_list[i])
            ##print("结束")
        #######################
                        
            ##print ("总计：%d"%num)
            finally:

                parser.text_str = ''
                parser.title_str = ''

                parser.a_title = False
                parser.a_start = False
                parser.a_txt =False

                parser.web_list = []
                parser.total = 0

            if len(website_list)== 0:
                self.thread_stop = True
                ##print ("no website!!\n")
                self.emit(QtCore.SIGNAL("update(QString)"), "没有网址可供使用!!\n")
                break

            while len(website_list)>0:
                url = website_list[len(website_list)-1]
                del website_list[len(website_list)-1]
            
                match = pattern.match(url)
                if(match):
                    break
                    ##print ("match")
                    self.emit(QtCore.SIGNAL("update(QString)"), "website match")
                else:
                    continue
            self.emit(QtCore.SIGNAL("update(QString)"), "目前可用网址列表共计 %d"%len(website_list))
            if num%50 ==0:
                self.emit(QtCore.SIGNAL("update(QString)"), "开始刷新界面")
                self.emit(QtCore.SIGNAL("clean_text()"))
        self.emit(QtCore.SIGNAL("update(QString)"), "已经停止下载网页!!!")
            
                    
    def render(self):
        self.start()
        thread_stop = False

    def stop(self):
        self.thread_stop = True
        ##print ("thread  stop !!!!!!")
        self.emit(QtCore.SIGNAL("update(QString)"), "正在停止下载网页!!!")

############################################################################
###################################################################################
class Window( QtGui.QWidget ):
    def __init__( self ):

        self.thread1 = crawler()
        self.thread_live = True
        self.thread_UI_start = False
        #######################
        super( Window, self ).__init__()
        self.setWindowTitle( "99网爬虫" )
        self.resize( 500, 500 )

        gridlayout = QtGui.QGridLayout()

        self.label = QtGui.QLabel("请输入网址：http://www.99.com.cn/xxg/gxy/*？")
        gridlayout.addWidget( self.label, 0,0)

        self.text_url = QtGui.QLineEdit("http://www.99.com.cn/xxg/gxy/")
        gridlayout.addWidget( self.text_url,1, 0, 1, 30 )
        
        self.start_button = QtGui.QPushButton( "开始" )
        gridlayout.addWidget( self.start_button, 2, 0, 1, 1 )
         
        self.stop_button = QtGui.QPushButton( "停止" )
        ##button2.setFlat( True )
        gridlayout.addWidget( self.stop_button, 2, 1, 1, 10 )

        self.textEdit = QtGui.QTextEdit()
        gridlayout.addWidget(self.textEdit, 3, 0, 90, 90 )
        ##gridlayout.addWidget(  )
        
        self.setLayout( gridlayout )

        self.connect( self.start_button, QtCore.SIGNAL( 'clicked()'), self.start_thread)
        self.connect( self.stop_button, QtCore.SIGNAL( 'clicked()'), self.stop_thread)
        self.connect(self.thread1, QtCore.SIGNAL('update(QString)'), self.update_GUI_text)
        self.connect(self.thread1, QtCore.SIGNAL('clean_text()'), self.clear_GUI_text)
        
        self.textEdit.setText("开始运行爬虫程序!")
    def start_thread(self):
        print ("start-------------------")
        ##self.textEdit.textCursor().insertText("\nqwewt")
        self.textEdit.append("start")
        input_url = self.text_url.text()
        match = pattern.match(input_url)
        if not (match):
            self.textEdit.append("the input website is not match\nplease input right website")
            return 
        global start_url
        start_url = input_url   
        if not self.thread_UI_start:
            ##self.thread1 = crawler()
            self.thread1.start()
            ##self.thread1.render()
            self.thread_UI_start = True
        
    def stop_thread(self):
        ##print ("stop")
        
        print ("stop-----------!\n")
        print (self.thread_UI_start)
        if self.thread_UI_start:
            self.thread1.stop()
            self.thread_UI_start = False
            self.thread_live = False
            self.textEdit.append("stop")

    def update_GUI_text(self,message):
        self.textEdit.append(message)

    def clear_GUI_text(self):
        self.textEdit.setText("开始刷新界面")
        
        
 
app = QtGui.QApplication( sys.argv )
demo = Window()
demo.show()
app.exec_()
