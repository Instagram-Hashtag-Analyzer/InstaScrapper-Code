# -*- coding: utf-8 -*-

#import urllib.request
#import urllib.error # get webpage by URL
#import re
#import json
import time
from datetime import datetime, date
#from bs4 import BeautifulSoup # pip install bs4 # parse web, obtain data 
import mysql.connector
from mysql.connector import errorcode
# import xlwt # excel
from webreader import get_tagpage_json
from jparser import total_like_of
from jparser import create_top9infolist
from db_operation import create_database
from db_operation import create_tables
from db_operation import insert_tag_like
from db_operation import insert_tag_toppost
from db_operation import insert_toppost_info




def start():

    print ("\t Instagram Hashtag Scrapper \n")
    tag_base_url = "https://www.instagram.com/explore/tags/"
    # post_base_url = "https://www.instagram.com/p/"

    tag_name = input("Please Enter a Hashtag: ")

    tag_url = tag_base_url + tag_name
    
    # print (tag_url) # for display only 

# 1. get webpage sources, store in variable (object)
    # function tagpage_json :: tag_url --> jsonstr 

    jsonstr = get_tagpage_json(tag_url)


# 2. parsing

    total_like_count : int = total_like_of(jsonstr) # not elegent 
    top9infolist = create_top9infolist(jsonstr)
    

# 3. save data to DB
    
    # Create Database if not exists:    `explore`
    DB_NAME = "explore"
    create_database(DB_NAME)
    
    # Use/Connect Database    
    conn = mysql.connector.connect(
        host      = "localhost",
        user      = "root",
        password  = "TIC3901", 
        database  =  DB_NAME,
        charset   = "utf8",
        collation = "utf8_general_ci"
    )
    
    cursor = conn.cursor()
    
    # Create Table 01:    `tag_like`
    create_tables(cursor)
    
    # Insert, modification of table 01: 

    insert_tag_like(cursor, tag_name, total_like_count)
    
    insert_tag_toppost(cursor, tag_name, top9infolist)
        
    insert_toppost_info(cursor, top9infolist)


    conn.commit()
    cursor.close()
    conn.close()


#`top9PostId` varchar(50) COLLATE utf8_unicode_ci,
#`createDate` datetime NOT NULL DEFAULT current_timestamp()

## Function Definition: 
#def create_database(DB_NAME): 



if __name__ == "__main__":
    start_time = time.time()
    start()
    print("-- execution time: %ss --" % (time.time() - start_time))





##+CAPTION: tag_
#| tagname   |    numLike | 
#|-----------+------------|
#| apple     |   35465424 |
#| love      | 2000022138 |
#| winter    |  147962789 |
#=name= should be primary key as each hashtag and the search page URL are unique.
#
##+CAPTION: tag_toppost
#| tag_name | postId        |
#|----------+---------------|
#| coding   | =CKQLGFVAo6e= |
#| coding   | =CKTPbS6A0mg= |
#| coding   | =CKPFztCDsUO= |
#| coding   | =CKRtAtvgWFO= |
#| coding   | =CKRZ13ygtuw= |
#| coding   | =CKR7KFCFD7d= |
#| coding   | =CKSs0yfAciw= |
#| coding   | =CKRLDmaAxmR= |
#| coding   | =CKSwFaNAsWr= |
#
##+CAPTION:toppost_info
#| postId        | numLike | numComment |       Date |
#|---------------+---------+------------+------------|
#| =CKQLGFVAo6e= |    8892 |         52 | 2021-01-20 |
#| =CKTPbS6A0mg= |    2799 |        223 | 2021-01-21 |
#| =CKPFztCDsUO= |    1426 |         14 | 2021-01-19 |
#
#
##+CAPTION: post_contain_tag
#| postId        | tagname       |
#|---------------+---------------|
#| =CKPFztCDsUO= | NULL          |
#| =CJ1d_NZgli1= | peoplewhocode |
#| =CJ1d_NZgli1= | 100daysofcode |
#| =CJ1d_NZgli1= | buildupdevs   |





#
#def sum (n): 
#    if n == 0: 
#        return 0
#    else: 
#        print (n)
#        return n + sum (n - 1) 
#        
#print (sum (10))
#
#
#list = ['a', 'b', 'c']
#
#for i, k in enumerate(list):
#    print ("%d: %s"%(i, k))


# 2. parsing
    
    # infolist = json.loads(jsonstr) # python dict obj 
    # #print (infolist)   # for display only 
    
    # with open('raw_all.json', 'w', encoding='utf-8') as jsonfile:
    #     json.dump(infolist, jsonfile, indent=4, ensure_ascii=False)
    
    #print(json.dumps(infolist, indent = 4, sort_keys=True)) # for display only 
    
    # edge_hashtag_to_top_posts
    
    # print(infolist["entry_data"]["TagPage"][0]["graphql"]["hashtag"]["edge_hashtag_to_media"]["count"])
    # Hard Coded ::DONE
    