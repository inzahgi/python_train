#!/usr/bin/python
#-*-coding:utf-8-*-

import sqlite3
import os
import sys
import time
import string
import stem_word_root


    
class SqliteTest:

    input_path = './2_4.txt'
##    save_path = '/home/inzahgi/nlp/stem_data/'
    action_category_path = './action/'

    def __init__(self):
        self.run()

    def run(self):
##        self.connect_db()
##        self.test()
        
        filter_list = []
        filter_set = set()
        filter_dict = dict()
        self.p = stem_word_root.PorterStemmer()
        
        input_dir = os.listdir(self.action_category_path)
        for line in input_dir :
##            print line
            file_path = self.action_category_path + line
##            print file_path

            boost_name = line.strip().lstrip().rstrip('.txt')
            tmp_list = []
            tmp_set = set()
            
            tmp_file_path = open(file_path, 'r')
            for x in tmp_file_path:
                str_tmp = x.strip().lstrip().rstrip()
                output = ''
                output += self.p.stem(str_tmp, 0, len(str_tmp) - 1 )

                if output != '' and output not in tmp_set:
                    tmp_list.append(output)
                    tmp_set.add(output)

            tmp_file_path.close()

            filter_list.append(tmp_list)
            filter_dict[boost_name] = tmp_set


##        self.print_list(filter_list)
        self.print_dict(filter_dict)
            
               
        self.print_category(filter_dict)
                
                
            
            

        print 'done!!'

##        self.cx.close()


    def connect_db(self):
        self.cx = sqlite3.connect(':memory:')
        self.cu = self.cx.cursor()


    def test(self):
        self.cu.execute("create table action (item varchar(255), word_root varchar(4000), word_root_next varchar(4000) )")
        a_list = [("shot", "shot gun", ""),
                  ("combat", "combat action attack target", "")]
        for t in a_list:
            self.cu.execute("insert into action values (?,?,?)", t)
        self.cx.commit()

        res = self.cu.execute("select * from  action")
        for x in res.fetchall() :
            print '%s----%s---%s'%(x[0],x[1],x[2])

    def print_list(self, input_list):
        for line in input_list:
            print line

    def print_dict(self, input_dict):
        for line in input_dict:
            print line
            print input_dict[line]


    def print_category(self, input_dict):

        no_category_cnt = 0
        has_category_cnt = 0

        no_category_list = []
        
        input_file = open(self.input_path,'r')
        for line in input_file:
            tmp_list = []
            tmp_res_dict = dict()
            line_list = line.split()
            mysql_id = line_list[0]
            for x in line_list:
##                tmp_list = self.filter_dict(x, input_dict)
                tmp_res_dict = self.filter_dict(x, input_dict, tmp_res_dict)

            if len(tmp_res_dict) == 0:
##                print '%s---%s'%(mysql_id, tmp_res_dict)
                ##print line
                no_category_cnt += 1
                no_category_list.append(line)
            ##break
            else:
                has_category_cnt += 1
        print 'the total no category %s-----has category %s'%(no_category_cnt, has_category_cnt)
        input_file.close()
        
        output_file = open("./no_category.txt","w")
        for line in no_category_list:
            output_file.write(line)

        output_file.close()
                


    def filter_dict(self, word, input_dict, res_dict):
##        print 'line 111 -----%s'%word
        output = ''
        output += self.p.stem(word, 0, len(word) - 1 )
        for key in input_dict:
##            print 'line 115  output  %s -------key %s ----- dict %s'%(output, key, input_dict[key])
            if output in input_dict[key]:
##                print 'line 122 -- output %s --------input_dict[%s] %s '%(output, key, input_dict[key])
                if key not in res_dict:
                    res_dict[key] = 1
                else:
##                    print 'line 125--output %s--- res_ dict %s'%(output, res_dict)
##                    print key
##                    print res_dict[key]
                    res_dict[key] += 1
                
        
        return res_dict
        


if __name__ == '__main__':

    sqliteTest = SqliteTest();
