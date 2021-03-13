#!/usr/bin/env python3

import mysql.connector
from mysql.connector import errorcode


def create_database(DB_NAME): 
    try: 
        newdb = mysql.connector.connect(
            host     = "localhost",
            user     = "root",
            password = "TIC3901"
        )
        
        newcursor = newdb.cursor()
        
        newcursor.execute(
            "CREATE DATABASE {};".format(DB_NAME))
        print("New Database Created!")
    except mysql.connector.Error as e: 
        if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        else: 
            print("Preparing Database...")
            pass
            
            
def insert_tag_like(cursor, tagname, total_like_count): 
    add_tag = ("INSERT INTO tag_like "
        "(tagname, numLike) "
        "VALUES (%(tagname)s, %(numLike)s)")
    
    # data set for test only, DONE: data feeder implementation
    data_tag = {
        'tagname':    tagname,
        'numLike':    total_like_count,
    }
    try:
        cursor.execute(add_tag, data_tag)
        
    except mysql.connector.IntegrityError:
        add_tag = ("UPDATE tag_like "
            "SET numLike = %(numLike)s WHERE tagname = %(tagname)s")
        data_tag = {
            'tagname':    tagname,
            'numLike':    total_like_count,
        }
        cursor.execute(add_tag, data_tag)
        
def insert_tag_toppost(cursor, tagname, list): 
    cursor.execute(
        "DELETE FROM tag_toppost WHERE tagname = %s",
         (tagname, )) 
    
    for dict in list:
        postId = dict["postId"]
        add_tag = ("INSERT INTO tag_toppost "
                        "(tagname, postId) "
                        "VALUES (%(tagname)s, %(postId)s)")
        
        # data set for test only, DONE: data feeder implementation
        data_tag = {
            'tagname':    tagname,
            'postId':     postId,
        }
        try:
            cursor.execute(add_tag, data_tag)
        except mysql.connector.IntegrityError:
            pass

def insert_toppost_info(cursor, list):
    
    for dict in list:
        postId = dict["postId"]
        numLike = dict["numLike"]
        numComment = dict["numComment"]
        pdate = dict["date"]
        
        
        add_tag = ("INSERT INTO toppost_info "
            "(postId, numLike, numComment, pdate) "
            "VALUES (%(postId)s, %(numLike)s, %(numComment)s, %(pdate)s)")
#            "ON DUPLICATE KEY UPDATE"
#            "numLike = %s,"
#            "numComment = %s,"
#            "pdate = %s")
        
        
        # data set for test only, DONE: data feeder implementation
        data_tag = {
            'postId':     postId,
            'numLike':    numLike,
            'numComment': numComment,
            'pdate':      pdate,
            'numLike':    numLike,
            'numComment': numComment,
            'pdate':      pdate
        }
        try:
            cursor.execute(add_tag, data_tag)
        except mysql.connector.IntegrityError:
            pass
            
    
def create_tables(cursor):
    try: 
        cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS `tag_like` (
            `tagname` varchar(50) COLLATE utf8_unicode_ci NOT NULL PRIMARY KEY,
            `numLike` int(12) NOT NULL
            ) 
        ''')
        
    except mysql.connector.Error as e: 
        print("Table error: ")
        print(e.msg)
        pass 
####		
    try: 
        cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS `tag_toppost` (
            `tagname` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
            `postId` char(11) NOT NULL,
             PRIMARY KEY (tagname, postId)) 
        ''')
        # `id` int IDENTITY PRIMARY KEY,
        
    except mysql.connector.Error as e: 
        print("Table error: ")
        print(e.msg)
        pass 
####		
    try: 
        cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS `toppost_info` (
            `postId` char(11) NOT NULL PRIMARY KEY,
            `numLike` int(12) NOT NULL,
            `numComment` int(12) NOT NULL,
            `pdate` date NOT NULL)
        ''')
        # `id` int IDENTITY PRIMARY KEY,
        
    except mysql.connector.Error as e: 
        print("Table error: ")
        print(e.msg)
        pass 