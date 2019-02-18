#!/usr/bin/python
# -*-coding:utf-8-*-


import mysql.connector
import os
import sys
import time
import random

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

        self.area_list = list(self.area_dict.keys())
        self.pcs_list = list(self.pcs_dict.keys())

        # print("line = 36 area_dict = {}\n".format(self.area_dict))
        # print("line = 37 pcs_dict = {}\n".format(self.pcs_dict))
        # print("line = 38 area_pcs_dict = {} \n".format(self.area_pcs_dict))
        # print("line = 39 pcs_area_dict = {} \n".format(self.pcs_area_dict))
        offset = 0
        limit = 10000
        while offset < self.score_total:
            res_list = self.get_score_by_page(offset, limit)
            # print(res_list)
            self.batch_update(res_list)
            ##break
            print("offset = {}".format(offset))
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
                self.pcs_dict[pcsCode] = pcsName
                self.pcs_area_dict[pcsCode] = areaCode
                if self.area_pcs_dict.get(areaCode) is None:
                    self.area_pcs_dict[areaCode] = []
                if pcsCode not in self.area_pcs_dict[areaCode]:
                    self.area_pcs_dict[areaCode].append(pcsCode)

        except mysql.connector.Error as e:
            print('query error!{}'.format(e))

    def get_score_by_page(self, offset, limit):
        try:
            self.cur.execute('select id, areaCode, controlStationId, subStationId from t_phone_info_credit limit %s offset %s', (limit, offset))
            res_list = []
            for id, areaCode, controlStationId, subStationId in self.cur:
                tmp = {}
                tmp['id'] = id
                tmp['areaCode'] = areaCode
                tmp['controlStationId'] = controlStationId
                tmp['subStationId'] = subStationId
                res_list.append(tmp)
            return res_list
        except mysql.connector.Error as e:
            print('query error!{}'.format(e))

    def batch_update(self, list):
        try:
            for d in list:
                flag = False
                id = d['id']
                areaCode = d['areaCode']
                if self.area_dict.get(areaCode) is None:
                    flag = True
                controlStationId = d['controlStationId']
                if self.pcs_dict.get(controlStationId) is None:
                    flag = True
                subStationId = d['subStationId']
                if self.pcs_dict.get(subStationId) is None:
                    flag = True
                if flag:
                    areaCode = self.area_list[random.randint(0,len(self.area_list) -1)]
                    controlStationId = self.pcs_list[random.randint(0, len(self.pcs_list) -1)]
                    subStationId = self.pcs_list[random.randint(0, len(self.pcs_list) -1)]

                    self.cur.execute('update t_phone_info_credit set areaCode = %s , controlStationId = %s, '
                             'subStationId = %s where id = %s', (areaCode, controlStationId, subStationId, id))

        except mysql.connector.Error as e:
            print('query error!{}'.format(e))




if __name__ == '__main__':
    db_sync = Db_sync()

