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

def channelengagement(cname, session):

    query1 = 'SELECT id, channeltitle FROM snippets'
    rows = session.execute(query1)
    vidnumbers = []
    for result in rows:
        if result.channeltitle == cname:
            vidnumbers.append(result.id)
    score = 0
    for idnum in vidnumbers:
        idval = str(idnum)
        score += videoengagement(idval, session)
    return score


def videoengagement(idnum, session):

    idval = str(idnum)
    query = 'SELECT id, commentcount, dislikecount, likecount, viewcount FROM statistics WHERE id = ' + idval
    rows = session.execute(query)
    for user_row in rows:
        comments = user_row.commentcount
        views = user_row.viewcount
        likes = user_row.likecount
        dislikes = user_row.dislikecount
        score = (int(comments) * 10) + int(views) + (int(likes) * 2) + int(dislikes)
    return score


result = channelengagement(chanelname, cqlsession)
print(result)
# exit(result)