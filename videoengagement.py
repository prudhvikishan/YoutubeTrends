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

idnum = sys.argv[1]

cloud_config = {
    'secure_connect_bundle': 'secure-connect-teaminferno.zip'
}
auth_provider = PlainTextAuthProvider('PKulaMpxCDcyZsxHoLeorxdE',
                                      'R1KL7l1u,awPgafa0-G3Xjt5QAjk,gTtz.qgmQSrsstUIdQnOoq_jgI,77nPA9upDOOYj2+ZefBMXudz+dFfF7IYPMGo56gz7xD337Nrcaufv3KKh,kzaS,0_xuCflNI')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect('yvideos')

idval = str(idnum)
query = 'SELECT id, commentcount, dislikecount, likecount, viewcount FROM statistics WHERE id = ' + idval

rows = session.execute(query)
for user_row in rows:
    comments = user_row.commentcount
    views = user_row.viewcount
    likes = user_row.likecount
    dislikes = user_row.dislikecount
    score = (int(comments) * 10) + int(views) + (int(likes) * 2) + int(dislikes)

print(score)