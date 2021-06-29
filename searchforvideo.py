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

chanelname = sys.argv[1]

cloud_config = {
    'secure_connect_bundle': 'secure-connect-teaminferno.zip'
}
auth_provider = PlainTextAuthProvider('PKulaMpxCDcyZsxHoLeorxdE',
                                      'R1KL7l1u,awPgafa0-G3Xjt5QAjk,gTtz.qgmQSrsstUIdQnOoq_jgI,77nPA9upDOOYj2+ZefBMXudz+dFfF7IYPMGo56gz7xD337Nrcaufv3KKh,kzaS,0_xuCflNI')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
cqlsession = cluster.connect('yvideos')


def searchforvideobylist(listofterms, session):

    results = {}
    nameresults = session.execute('SELECT id, title FROM localized')
    counter = 1
    results[0] = [0]
    for value in nameresults:
        flag = True
        for term in listofterms:
            if value.title.find(term) < 1:
                flag = False
        if flag == True:
            results[counter] = [value.title, value.id]
            counter += 1
    counter -= 1
    results[0] = counter
    return results


searchterms = sys.argv
searchterms.pop(0)
result = searchforvideobylist(searchterms, cqlsession)
print(json.dumps(result))