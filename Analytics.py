#!/usr/bin/python
# -*- coding: utf-8 -*-

from pprint import pprint
import json
import os
import datetime
import operator
import cassandra
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider


# pass an int for the id of the video that will be scored
# returns an int with that score
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


# pass a string with the name of the channel
# that will be scored. returns an int with that
# channel's score
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


# pass the number of videos to be in the list as an
# int. returns the top X records
def topvideos(number, session):

    arr = []
    lowest: int = 0
    count: int = 0
    rows = session.execute('SELECT id, commentcount, dislikecount, likecount, viewcount FROM statistics')
    print("Got data")
    for user_row in rows:
        comments = user_row.commentcount
        views = user_row.viewcount
        likes = user_row.likecount
        dislikes = user_row.dislikecount
        score = (int(comments) * 10) + int(views) + (int(likes) * 2) + int(dislikes)
        if count < number:
            arr.append([user_row.id, score])
            count += 1
            if lowest < score:
                lowest = score
            arr.sort(key=operator.itemgetter(1))
        elif lowest < score:
            del arr[0]
            lowest = score
            arr.append([user_row.id, score])
            arr.sort(key=operator.itemgetter(1))
    return arr


# pass the number of videos to be in the list as an
# int. returns the top X records
def topvideonames(number, session):

    arr = []
    lowest: int = 0
    count: int = 0
    rows = session.execute('SELECT id, commentcount, dislikecount, likecount, viewcount FROM statistics')
    nameresults = session.execute('SELECT id, title FROM localized')
    for user_row in rows:
        comments = user_row.commentcount
        views = user_row.viewcount
        likes = user_row.likecount
        dislikes = user_row.dislikecount
        score = (int(comments) * 10) + int(views) + (int(likes) * 2) + int(dislikes)
        if count < number:
            arr.append([user_row.id, score])
            count += 1
            if lowest < score:
                lowest = score
            arr.sort(key=operator.itemgetter(1))
        elif lowest < score:
            del arr[0]
            lowest = score
            arr.append([user_row.id, score])
            arr.sort(key=operator.itemgetter(1))
    for records in nameresults:
        for item in arr:
            if item[0] == records.id:
                item[0] = records.title
    return arr


# pass the number of channels to be in the list.
# as an int. returns the top X records
def topchannels(number, session):

    arr = []
    lowest: int = 0
    count: int = 0
    rows = session.execute('SELECT channeltitle FROM snippets')
    # rows2 = session.execute('SELECT id, commentcount, dislikecount, likecount, viewcount FROM statistics')
    for user_row in rows:
        score = channelengagement(user_row.channeltitle, session)
        if count < number:
            arr.append([user_row.channeltitle, score])
            count += 1
            if lowest < score:
                lowest = score
            arr.sort(key=operator.itemgetter(1))
        elif lowest < score:
            del arr[0]
            lowest = score
            arr.append([user_row.channeltitle, score])
            arr.sort(key=operator.itemgetter(1))
    return arr


def searchforvideobylist(listofterms, session):

    results = []
    nameresults = session.execute('SELECT id, title FROM localized')
    for value in nameresults:
        flag = True
        for term in listofterms:
            if value.title.find(term) < 0:
                flag = False
        if flag == True:
            results.append([value.title, value.id])
    return results

vidsearched = False
channelsearched = False
topvidresults = []
topchannelresults = []
cloud_config = {
    'secure_connect_bundle': 'secure-connect-teaminferno.zip'
}
auth_provider = PlainTextAuthProvider('PKulaMpxCDcyZsxHoLeorxdE',
                                      'R1KL7l1u,awPgafa0-G3Xjt5QAjk,gTtz.qgmQSrsstUIdQnOoq_jgI,77nPA9upDOOYj2+ZefBMXudz+dFfF7IYPMGo56gz7xD337Nrcaufv3KKh,kzaS,0_xuCflNI')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
cqlsession = cluster.connect('yvideos')
while True:
    print("Choose an option:")
    print("1) Display the top ten videos")
    print("2) Display the top ten channels")
    print("3) Display the engagement score of a video")
    print("4) Display the engagement score of a channel")
    print("5) Search video titles for a term")
    print("6) Quit")
    input1 = input()
    if input1 == "1":
        if vidsearched == False:
            topvidresults = topvideonames(10, cqlsession)
            vidsearched = True
        print(*topvidresults, sep="\n")
        print("Press enter to continue")
        input2 = input()
    elif input1 == "2":
        if channelsearched == False:
            topchannelresults = topchannels(10, cqlsession)
            channelsearched = True
        print(*topchannelresults, sep="\n")
        print("Press enter to continue")
        input2 = input()
    elif input1 == "3":
        print("Enter the id of a video:")
        input2 = input()
        input3 = int(input2)
        result = videoengagement(input3, cqlsession)
        print(result)
        print("Press enter to continue")
        input2 = input()
    elif input1 == "4":
        print("Enter the name of the channel")
        input2 = input()
        result = channelengagement(input2, cqlsession)
        print(result)
        print("Press enter to continue")
        input2 = input()
    elif input1 == "5":
        print("Enter the search terms")
        input2 = input()
        inputlist = []
        stringbuilder = ""
        for char in input2:
            if char != " " and char != "\n":
                stringbuilder += char
            else:
                inputlist.append(stringbuilder)
                stringbuilder = ""
        inputlist.append(stringbuilder)
        result = searchforvideobylist(inputlist, cqlsession)
        print(*result, sep="\n")
        input2 = input("Press enter to continue")
    elif input1 == "6":
        exit()
