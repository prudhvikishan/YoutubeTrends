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
cqlsession = cluster.connect('yvideos')


def reverse(lst):
    return[ele for ele in reversed(lst)]


def topkeywords(number, session):
    holder = []
    rows = session.execute('SELECT keyval, videoids, count, score FROM averages')
    for values in rows:
        if "tag: " in values.keyval:
            score = int(values.score)
            count = int(values.count)
            average = score / count
            tag = values.keyval.replace('tag: ', '')
            holder.append([tag, average])
    holder.sort(key=operator.itemgetter(1))
    while len(holder) > number:
        holder.pop(0)
    return holder


topwords = topkeywords(20, cqlsession)
fixedresults = reverse(topwords)

result = {}
counter = 0

if len(sys.argv) == 1:
    for ele in fixedresults:
        del ele[1]
    for ele in fixedresults:
        result[counter] = ele
        counter += 1
else:
    for ele in fixedresults:
        del ele[0]
    for ele in fixedresults:
        result[counter] = ele
        counter += 1

print(json.dumps(result))
