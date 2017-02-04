# -*- coding: utf-8 -*-
import struct
import sys

import os
import sqlite3


def read_buf(num):
    return buf[(num*0x1000):((num+1)*0x1000)]

def find_address(): ##找到聊天记录的标志位   #/x06/x02(/x01)/x08/x00
    b=len(temp)
    a=0
    while a<(b-10):
        if temp[a] != 0x06 :
            a=a+1
            continue
        if temp[a+1] != 0x01 :
            if temp[a+1] != 0x02:
                if temp[a+1] != 0x03:
                    a=a+2
                    continue
        if temp[a+2] != 0x01 :
            if temp[a+2] !=0x08 :
                a=a+3
                continue
        if temp[a+3] != 0x00 :
            a=a+4
            continue
        if temp[a+4] >= 0x40 :
            a=a+5
            print(5)
            continue
        msg_find_address.append(a)
        a=a+1

def check_address(): ##找到信息的首位地址
    i=1
    if x>100: ##不会超出上边界
        while i<6:  ##/x06/x02(/x01)/x08/x00 前面有10个 0 判断地址是否正确
            if temp[x-i-1] == 0x0:
                i=i+1;
                continue
            break
        
        ##print ('line 39  i= %d'%i)
    if i==6:
        ##print ('find it')

        cnt = x+4    ##从/x06开始 过4个字节 就是 QQ号码
        while True:
            ##print ('循环1--------------------------------------')
        
            if temp[cnt] < 0x40 and temp[cnt] >0x29:
              ##  print (hex(temp[cnt]))
                cnt=cnt+1
                continue
            break
        return cnt+4 ##QQ 号码之后的4个字节表示时间
    else :
        return 0

def analysis_end(len_addr): ##目前只考虑一个字节
    ##print ('len_addr = %x '%(temp[len_addr]))
    if temp[len_addr]%2 ==0:
        return (temp[len_addr]-12)//2  
    else:
        return (temp[len_addr]-13)//2
        
    

def find_msg_end(addr):  ##msg address 

    addr_temp1=analysis_end(x-31)+addr ## x is 06020800 address
    ##print ('addr_temp1 = %d  addr = %d'%(addr_temp1,addr))
    

    while True:
        ##print (addr)
        if addr >4090:
            break
        if temp[addr]==0x01:
            if temp[addr+1]==0x00:
                if temp[addr+2]==0x00 :
                    break

        if temp[addr]==0x03:
            if temp[addr+1]==0x01:
                if temp[addr+2]==0x00 :
                    break


        ##print ('>>>>>>>%x<<<<<<<<'%temp[addr])
        addr=addr+1
        continue
    addr_temp2=addr
    if addr_temp1 < addr_temp2:
        return addr_temp1
    else :
        return addr_temp2
    
def find_send_or_receive():  
    i=0
    while temp[x-35-i] != 0x04:  ## x is /x06/x02/x08/x00  中/x06的地址
        ##print ('line = 78 -------time flag is %s'%hex(temp[x-35-i]))
        i = i+1
        if i>5:
            break
    ##print ('line = 78 time flag is %s'%hex(temp[x-35-i]))
     
    ##print ('line 84  send_flag is  %s  i = %d x= %s'%(hex(temp[x-33-i]),i,hex(x)))
    if temp[x-33-i] == 0x09:
        return 1        ##  send
    elif temp[x-33-i] == 0x08:
        return 0       ## receive 
    else :
        return 2   ## 表示 找到的状态 有问题

##def display(qq_n,qq_m,msg_n,msg_m):
##    msg=temp[msg_n:msg_m]
##    msg_print= msg.decode('utf-8','ignore')
##    qq_num= temp[qq_start:qq_end].decode('utf-8','ignore')
##    send_time= struct.unpack('>I',temp[qq_end:qq_end+4])
##    print ('msg_print is')
##    print ('\n-----------------\n')
##    print  ('QQ:\t%s'%qq_num)
##    print  ('time:\t%s'%send_time)
##    print ('msg:\t%s'%msg_print)
##    print ('flag:\t%d'%send_or_receive)
##    print ('\n-----------------\n')

##    cursor.execute("""
##insert into c2cmsg(QQ, time, text, flag)
##values (qq_num, send_time, msg_print, flag)
##""")

def display1(number,time, msg, flag):
    print ('\n----------------------------\n')
    print ('QQ:\t%s'%number)
    print ('time:\t%s'%time)
    print ('msg:\t%s'%msg)
    print ('flag:\t%d'%flag)
    print ('\n----------------------------\n')
        


if __name__ == '__main__':
    
    db_name = input('input database: ')
    if db_name == 'db_rebulit.db':
        print ('you can\'t input this name \nPlease change the file name!')
        input('')
        exit()
        
    if db_name == 'recover_database.db':
        print ('you can\'t input this name \nPlease change the file name!')
        input('')
        exit()
        
    os.system('sqlite3.exe %s<1.txt'%db_name) ## 导出SQL语句
    ##os.system('del db_rebuilt.db')
    os.system('sqlite3.exe db_rebuilt.db<2.txt')  ##生成一个精简的DB 文件 
    
    
    conn=sqlite3.connect('recover_database.db')
    cursor=conn.cursor()

    cursor.execute("""DROP TABLE IF EXISTS c2cmsg_recover""") ## 删除表
    
    cursor.execute("""create table c2cmsg_recover
(QQ char(12), time double, text varchar, flag int)
""")

    cursor.execute("""DROP TABLE IF EXISTS c2cmsg""") ## 删除表
    
    cursor.execute("""create table c2cmsg
(QQ char(12), time double, text varchar, flag int)
""")
    
    print ('please wait.......programe is runing')

    db_cnt = 0
    while True:
        if db_cnt ==0:
            file=open('%s'%db_name,'rb')   ##  QQ_hou.db   QQYCF.db   QQ.db
        else :
            file=open('db_rebuilt.db','rb')
            
        try:
            buf=file.read()
        finally:
            file.close()
        loop_time = 0
        i=0
        while True:
            temp=read_buf(loop_time) ##读出一页的字节  也就是 当前页号
            msg_find_address=[]   

            find_address()   ##/x06/x02/x08(/x01/x00)中 06的地址
            if len(msg_find_address)!=0:
                print (msg_find_address) ##显示找到的地址  

            for x in msg_find_address:
                qq_start = x+4
                ##print ('qq_start = %s'%(hex(temp[qq_start])))
                start=check_address()   ##找到信息的首位地址
                qq_end = start-4
                ##print ('qq_end = %s'%(hex(temp[qq_end])))
                ##print  (temp[qq_start:qq_end])
            
                if start !=0:    ##  /x06前面 有10个0  可以开始恢复聊天纪录
                    last =find_msg_end(start)
                    ##print ('start = %d  last = %d'%(start,last))
                    ##print ('line = 125 start = %s start+1 = %s'%(hex(temp[start]),hex(temp[start +1]) )  )
##------------------------------------------------------------------------------------------
                    qq_num= temp[qq_start:qq_end].decode('utf-8','ignore')
                                
                    send_time= '%s'%(struct.unpack('>I',temp[qq_end:qq_end+4]))
                    send_or_receive = find_send_or_receive()
                    msg=temp[start:last]
                    msg_print= '%s'%(msg.decode('utf-8','ignore'))
                
                
                

##-----------------------------------------------------------------------------------------
                    if db_cnt == 0:
                        sql_insert = 'insert into c2cmsg_recover(QQ, time, text, flag) values(%s, %s, \'%s\', %d)'%(qq_num, send_time, msg_print, send_or_receive)
                    else :
                        sql_insert = 'insert into c2cmsg(QQ, time, text, flag) values(%s, %s, \'%s\', %d)'%(qq_num, send_time, msg_print, send_or_receive)
                    try:
                        cursor.execute(sql_insert)
                    except sqlite3.OperationalError:
                        pass
                
##-------------------------------------------------------------------------------------------                
                 ## SQL 语句需要全局变量 函数局部变量不行
                ##display1(qq_num, send_time, msg_print, send_or_receive)
                i=i+1
            
               

            ##print (loop_time) ##打印循环次数
            if loop_time >= (len(buf)/0x1000):
                break
            else:
                loop_time=loop_time+1
                continue
        ##print ('total  %d'%i)
        db_cnt = db_cnt+1
        if db_cnt>=2:
            break


    cursor.execute("""DROP TABLE IF EXISTS recover""") ## 删除表
    
    cursor.execute("""create table recover
(QQ char(12), time double, text varchar, flag int)
""")
    
    sql_choice = """insert into recover
select *
from c2cmsg_recover t1 
where not exists ( select * 
from  c2cmsg tt2
where t1.QQ = tt2.QQ
and t1.time = tt2.time
and t1.text = tt2.text )"""
    cursor.execute(sql_choice)
    conn.commit()
    cursor.close()
    conn.close()
    os.system('del db_rebuilt.db')
    
