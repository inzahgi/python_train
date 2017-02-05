# -*- coding: utf-8 -*-
import paramiko
import os
import string

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#client.connect('192.168.8.248', 22, username='root', password='password', timeout=4)

char_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

num_char_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

lower_char_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]

upper_char_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]

spcial_char_list = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

def write_log(ip_str,password):
	log_file = "find_pass.txt"
	file = open(log_file,'a')
	file.write(ip_str+'|'+password+os.linesep)
	file.close()

def ssh_connect(ip,username,password):
	global client
	try:
		client.connect(ip, 22, username=username, password=password, timeout=4)
		write_log(ip,password)
		print "ip: %s is login success,password is %s" % (ip,password)
	except:
		print "ip: %s login has no pass" % ip
		#client.close()

def creat_password(num, char_list):
	
											
if __name__=='__main__':
	char_list = list(string.printable)
	print char_list
	print a+b+c+d
	
##	pwd_dic = ['123456','111111','222222','888888','999999','666666']
##	if os.path.exists('ip_log.txt'):
##		for ip in open("ip_log.txt").readlines():
##			for pwd in pwd_dic:
##				ssh_connect(ip,'root',pwd)
##	else:
##		print "ip_log is not exists"
##	client.close()
