#!/usr/bin/python
# -*-coding:utf-8-*-


import mysql.connector
import os
import sys
import time

user = ''
password = ''
host = '172.16.16.12'
port = '3306'



class Db_sync:
    pcs_dict = {}
    area_dict = {}
    area_pcs_dict= {}
    pcs_area_dict = {}

    limit = 100
    offset = 0
    total = 0

    def __init__(self):

        self.run()

    def run(self):
        self.score_total = 0
        self.connect_mysql()
        self.get_area_dict()
        self.get_pcs_dict()

        # print("line = 36 area_dict = {}\n".format(self.area_dict))
        # print("line = 37 pcs_dict = {}\n".format(self.pcs_dict))
        # print("line = 38 area_pcs_dict = {} \n".format(self.area_pcs_dict))
        # print("line = 39 pcs_area_dict = {} \n".format(self.pcs_area_dict))
        offset = 0
        limit = 10
        while offset < self.score_total:
            res_list = self.get_score_by_page(offset, limit)
            # print(res_list)

            break;

            offset += limit



        self.cur.close()
        self.conn.close()
        print('done!!')

    def connect_mysql(self):
        try:
            self.conn = mysql.connector.connect(user=user, password=password, host=host, port=port, database='dqjc')
            self.cur = self.conn.cursor()

            self.cur.execute("select count(*) from t_phone_info_credit")
            self.score_total = self.cur.fetchone()[0]


        except mysql.connector.Error as e:
            print('connect error! {}'.format(e))

    def get_area_dict(self):
        try:
            self.cur.execute('select dictCode, dictName from t_sys_dict '\
                             'where dictTypeName = %s AND id != %s', ('重庆市区域名称', '39'))
            for dictCode, dictName in self.cur:
                # print("dictCode = \t", dictCode, "dictName = \t", dictName)
                self.area_dict[dictCode] = dictName
        except mysql.connector.Error as e:
            print('line = 51\nquery error!{}'.format(e))


    def get_pcs_dict(self):
        try:
            self.cur.execute('select pcsName, pcsCode, areaCode, areaName from t_police_substation_info')
            for pcsName, pcsCode, areaCode, areaName in self.cur:
                # print("pcsName = {}, pcsCode = {}, areaCode = {}, areaName = {}".format(pcsName, pcsCode, areaCode, areaName))
                self.pcs_dict[pcsCode] = pcsName
                self.pcs_area_dict[pcsCode] = areaCode
                if self.area_pcs_dict.get(areaCode) is None:
                    self.area_pcs_dict[areaCode] = []
                if pcsCode not in self.area_pcs_dict[areaCode]:
                    self.area_pcs_dict[areaCode].append(pcsCode)

        except mysql.connector.Error as e:
            print('query error!{}'.format(e))

    def get_score_by_page(self, limt, offset):
        try:
            self.cur.execute('select id from t_phone_info_credit')
            res_list = []
            for id in self.cur:
                # print("pcsName = {}, pcsCode = {}, areaCode = {}, areaName = {}".format(pcsName, pcsCode, areaCode, areaName))
                res_list.append(id)
            return res_list
        except mysql.connector.Error as e:
            print('query error!{}'.format(e))

    def batch_update(self, idList):
        id = data['id']
        if data['areaCode'] not in self.area_dict:
            return id
        if data['controlStationId'] not in self.pcs_dict:
            return id
        ##if data[]



if __name__ == '__main__':
    db_sync = Db_sync()

