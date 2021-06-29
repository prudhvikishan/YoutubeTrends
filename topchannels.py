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


def topchannels(number, session):

    arr = []
    lowest: int = 0
    count: int = 0
    rows = session.execute('SELECT id, channeltitle FROM snippets')
    rows2 = session.execute('SELECT id, commentcount, dislikecount, likecount, viewcount FROM statistics')
    channeldirectory = []
    videoscores = []

    for user_row in rows2:
        comments = user_row.commentcount
        views = user_row.viewcount
        likes = user_row.likecount
        dislikes = user_row.dislikecount
        score = (int(comments) * 10) + int(views) + (int(likes) * 2) + int(dislikes)
        videoscores.append([user_row.id, score])
    for user_row in rows:
        if user_row.channeltitle not in (channeldirectory):
            channeldirectory.append([user_row.channeltitle, user_row.id])

    for channelentry in channeldirectory:
        chanscore = 0
        for videoscore in videoscores:
            if videoscore[0] == channelentry[1]:
                chanscore += videoscore[1]

        if count < number:
            arr.append([channelentry[0], str(chanscore)])
            count += 1
            if lowest < score:
                lowest = score
            arr.sort(key=operator.itemgetter(1))
        elif lowest < chanscore:
            del arr[0]
            lowest = chanscore
            arr.append([channelentry[0], str(chanscore)])
            arr.sort(key=operator.itemgetter(1))
    return arr


topchannelresults = topchannels(10, cqlsession)
fixedresults = reverse(topchannelresults)

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

