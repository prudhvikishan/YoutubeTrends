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


session.execute("""truncate table records;""")
session.execute("""truncate table snippets;""")
session.execute("""truncate table localized;""")
session.execute("""truncate table contentdetails;""")
session.execute("""truncate table statistics;""")


record_id = 1
snippet_id = 1
localized_id = 1
contentDetails_id = 1
statistics_id = 1
                
with open('videoinfo.json') as data_file:
    data = json.load(data_file)

    for v in data:
        keywordslist = []
        rec_etag = "'" + v['etag'] + "'"
        rec_id = "'" + v['id'] + "'"
        rec_record_id = record_id
        rec_snippet_id = snippet_id
        rec_localized_id = localized_id
        rec_contentDetails_id = contentDetails_id
        rec_statistics_id = statistics_id


        s_id = snippet_id
        s_publishedAt = "'" + v['snippet']['publishedAt'] + "'"
        s_channelId = "'" + v['snippet']['channelId'] + "'"
        s_title = "'" + v['snippet']['title'] + "'"
        s_channelTitle = "'" + v['snippet']['channelTitle'] + "'"
        s_categoryId = "'" + v['snippet']['categoryId'] + "'"
        s_liveBroadcastContent = "'" + v['snippet']['liveBroadcastContent'] + "'"
        s_defaultlanguage = "'" + v['snippet']['defaultLanguage'] + "'"
        scrubdescription = v['snippet']['description']
        scrubdescription = scrubdescription.replace("'", "''")
        scrubdescription = scrubdescription.replace("\n","  ")
        scrubdescription = scrubdescription.replace("\r", "  ")
        scrubdescription = scrubdescription.replace("\r\n", "  ")
        s_description = "'" + scrubdescription + "'"


        cont_id = contentDetails_id
        cont_duration = "'" + v['snippet']['duration'] + "'"
        cont_definition = "'" + v['snippet']['definition'] + "'"
        cont_caption = "'" + v['snippet']['caption'] + "'"


        stat_id = statistics_id
        stat_viewcount = "'" + v['snippet']['viewCount'] + "'"
        stat_likecount = "'" + v['snippet']['likeCount'] + "'"
        stat_dislikecount = "'" + v['snippet']['dislikeCount'] + "'"
        stat_commentcount = "'" + v['snippet']['commentCount'] + "'"


        l_id = localized_id
        l_title = "'" + v['snippet']['title'] + "'"

        record_id += 1
        snippet_id += 1
        contentDetails_id += 1
        statistics_id += 1
        localized_id += 1

        query = 'insert into records (id,videoid,etag) values ('
        query += str(rec_record_id) + ', '
        query += str(rec_id) + ', '
        query += rec_etag + ')'
        #query += str(rec_snippet_id)

        prepared_stmt = session.prepare(query)
        session.execute(prepared_stmt)

        query = \
            'insert into snippets (id,publishedAt,channelId,title,channelTitle,categoryid,liveBroadcastContent,defeaultlanguage,description) values ('
        query += str(s_id) + ', '
        query += s_publishedAt + ', '
        query += s_channelId + ', '
        query += s_title + ', '
        query += s_channelTitle + ', '
        query += s_categoryId + ', '
        query += s_liveBroadcastContent + ', '
        query += s_defaultlanguage + ', '
        query += s_description + ')'
        #query += str(s_channelTitle_id) + ', '
        #query += str(s_localized_id) + ')'

        prepared_stmt = session.prepare(query)
        session.execute(prepared_stmt)

        query = \
            'insert into localized (id,title) values ('
        query += str(l_id) + ', '
        query += l_title + ')'

        prepared_stmt = session.prepare(query)
        session.execute(prepared_stmt)

        query = 'insert into contentdetails(id,duration,definition,caption) values ('
        query += str(cont_id) + ', '
        query += cont_duration + ', '
        query += cont_definition + ', '
        query += cont_caption + ')'

        prepared_stmt = session.prepare(query)
        session.execute(prepared_stmt)

        query = 'insert into statistics(id,viewcount,likecount,dislikecount,commentcount) values ('
        query += str(stat_id) + ', '
        query += stat_viewcount + ', '
        query += stat_likecount + ', '
        query += stat_dislikecount + ', '
        query += stat_commentcount + ')'

        prepared_stmt = session.prepare(query)
        session.execute(prepared_stmt)

        checker = "tags" in v['snippet']
        if checker:
            datalist = v['snippet']['tags']
            for value in datalist:
                value = value.translate(str.maketrans({"'": "''"}))
                keywordslist.append(value)

            query = ' '
            for value in keywordslist:
                query = "select keyval, count, videoids from averages where keyval = "
                query += "'tag: " + value + "';"

                myrows = session.execute(query)
                for resultparse in myrows:
                    ids = "'" + str(resultparse.videoids) + ", " + str(snippet_id) + "'"
                    counter = resultparse.count + 1

                mycount = str(counter)
                print(mycount)
                query = "update averages set count = " + mycount + ", videoids = " + ids + " where keyval = "
                query += "'tag: " + value + "';"
                print(query)
                prepared_stmt = session.prepare(query)
                session.execute(prepared_stmt)


        timevalue = s_publishedAt[12: 14]
        print("timevalue = " + timevalue)
        query = "select count, videoids from averages where keyval = "
        query += "'time: " + timevalue + "';"
        print(query)
        rows = session.execute(query)
        ids = ''
        counter = 0
        for resultparse in rows:
            ids = "'" + str(resultparse.videoids) + ", " + str(snippet_id) + "'"
            counter = resultparse.count + 1
        query = "update averages set count = " + str(counter) + ", videoids = " + ids + " where keyval = "
        query += "'time: " + timevalue + "';"
        print(query)
        prepared_stmt = session.prepare(query)
        session.execute(prepared_stmt)
