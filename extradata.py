#!/usr/bin/python
# -*- coding: utf-8 -*-

from pprint import pprint
import json
import os
import datetime
import cassandra
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

# Connection to yvideos keyspace

cloud_config= {
    'secure_connect_bundle': 'secure-connect-teaminferno.zip'
}
auth_provider = PlainTextAuthProvider('PKulaMpxCDcyZsxHoLeorxdE', 'R1KL7l1u,awPgafa0-G3Xjt5QAjk,gTtz.qgmQSrsstUIdQnOoq_jgI,77nPA9upDOOYj2+ZefBMXudz+dFfF7IYPMGo56gz7xD337Nrcaufv3KKh,kzaS,0_xuCflNI')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect('yvideos')

record_id = 1
snippet_id = 1
localized_id = 1
contentDetails_id = 1
statistics_id = 1
keywordslist = []
with open('videoinfo.json') as data_file:
    data = json.load(data_file)
    for v in data:
        checker = "tags" in v['snippet']
        if checker:
            datalist = v['snippet']['tags']
            for value in datalist:
                value = value.translate(str.maketrans({"'": "''"}))
                if value not in keywordslist:
                    keywordslist.append(value)
    query = 'insert into averages(keyval,videoids, count, score) values ('
    for value in keywordslist:
        query = 'insert into averages(keyval,videoids, count, score) values ('
        query += "'tag: " + value + "', ' ', 0, 0)"
        prepared_stmt = session.prepare(query)
        session.execute(prepared_stmt)

    attrlist = {'2d', '3d', 'hd', 'sd', 'caption', 'nocaption'}
    daylist = {'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'}
    timelist = {'00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14',
                '15', '16', '17', '18', '19', '20', '21', '22', '23'}

    for value in attrlist:
        query = 'insert into averages(keyval,videoids, count, score) values ('
        query += "'attr: " + value + "', ' ', 0, 0)"
        prepared_stmt = session.prepare(query)
        session.execute(prepared_stmt)
    for value in daylist:
        query = 'insert into averages(keyval,videoids, count, score) values ('
        query += "'day: " + value + "', ' ', 0, 0)"
        prepared_stmt = session.prepare(query)
        session.execute(prepared_stmt)
    for value in timelist:
        query = 'insert into averages(keyval,videoids, count, score) values ('
        query += "'time: " + value + "', ' ', 0, 0)"
        prepared_stmt = session.prepare(query)
        session.execute(prepared_stmt)