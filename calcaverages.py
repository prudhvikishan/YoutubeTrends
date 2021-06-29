#!/usr/bin/python
# -*- coding: utf-8 -*-

from pprint import pprint
import json
import os
import datetime
import operator
import sys
import getopt
import cassandra
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config = {
    'secure_connect_bundle': 'secure-connect-teaminferno.zip'
}
auth_provider = PlainTextAuthProvider('PKulaMpxCDcyZsxHoLeorxdE',
                                      'R1KL7l1u,awPgafa0-G3Xjt5QAjk,gTtz.qgmQSrsstUIdQnOoq_jgI,77nPA9upDOOYj2+ZefBMXudz+dFfF7IYPMGo56gz7xD337Nrcaufv3KKh,kzaS,0_xuCflNI')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect('yvideos')

averagerows = session.execute('select keyval, count, score, videoids from averages')
scorerows = session.execute('SELECT id, commentcount, dislikecount, likecount, viewcount FROM statistics')

scorelist = []
for row in scorerows:
    score = (int(row.commentcount) * 10) + int(row.viewcount) + (int(row.likecount) * 2) + int(row.dislikecount)
    scorelist.append([str(row.id), score])
averagelist = []
for row in averagerows:
    ids = row.videoids.replace(',','')
    averagelist.append([row.keyval, ids, 0])

for row in averagelist:
    for value in scorelist:
        littleid = value[0]
        bigid = row[1]
        if littleid in bigid:
            row[2] += value[1]
for row in averagelist:
    strscore = row[2]
    tags = row[0]
    tags = tags.replace("'", "''")
    query = "update averages set score = " + str(strscore) + " where keyval = '" + tags + "';"
    session.execute(query)













# idlist = []
# holder = ''
# for vals in averagerows:
#     if "time: " in vals.keyval:
#         holder = vals.videoids.lstrip(' ')
#         holder = holder.lstrip(',')
#         holder = holder.lstrip(' ')
#         if len(holder) > 2:
#             holder += ";"
#         idlist.append([vals.keyval, holder])
# for values in idlist:
#     query = "update averages set videoids = '" + values[1] + "' where keyval = '" + values[0] + "';"
#     session.execute(query)
#
#
