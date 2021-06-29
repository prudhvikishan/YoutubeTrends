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


def valueswap(str):
	if str == "00":
		return "12:00am"
	if str == "01":
		return "1:00am"
	if str == "02":
		return "2:00am"
	if str == "03": 
		return "3:00am"
	if str == "04": 
		return "4:00am"
	if str == "05": 
		return "5:00am"
	if str == "06": 
		return "6:00am"
	if str == "07": 
		return "7:00am"
	if str == "08": 
		return "8:00am"
	if str == "09": 
		return "9:00am"
	if str == "10": 
		return "10:00am"
	if str == "11": 
		return "11:00am"
	if str == "12": 
		return "12:00pm"
	if str == "13": 
		return "1:00pm"
	if str == "14": 
		return "2:00pm"
	if str == "15": 
		return "3:00pm"
	if str == "16": 
		return "4:00pm"
	if str == "17": 
		return "5:00pm"
	if str == "18": 
		return "6:00pm"
	if str == "19": 
		return "7:00pm"
	if str == "20": 
		return "8:00pm"
	if str == "21": 
		return "9:00pm"
	if str == "22": 
		return "10:00pm"
	if str == "23": 
		return "11:00pm"
	

def topkeywords(number, session):

    holder = []

    rows = session.execute('SELECT keyval, videoids, count, score FROM averages')
    for values in rows:
        if "time: " in values.keyval:
            score = int(values.score)
            count = int(values.count)
            average = 0
            if count > 0:
                average = score / count
            tag = values.keyval.replace('time: ', '')
            holder.append([tag, average])
    holder.sort(key=operator.itemgetter(1))
    while len(holder) > number:
        holder.pop(0)
    return holder


topwords = topkeywords(10, cqlsession)
fixedresults = reverse(topwords)

result = {}
counter = 0

for row in fixedresults:
	row[0] = valueswap(row[0])

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
