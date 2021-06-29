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


def searchfortag(listofterms, session):
    results = {}
    title = 'tag: '
    for word in listofterms:
        title += word
    query = "SELECT count, score FROM averages where keyval = '" + title + "'"
    nameresults = session.execute(query)

    score = 0
    count = 0
    flag = True
    if nameresults is not None:
        for val in nameresults:
            for number in val:
                if flag:
                    holder = val[0]
                    count = int(holder)
                    flag = False
                else:
                    hold = val[1]
                    score = int(hold)
        average = 0
        if score > 0:
            average = score / count
        return average
    badsearch = -1
    return badsearch

searchterms = sys.argv
searchterms.pop(0)
result = searchfortag(searchterms, cqlsession)
print(result)