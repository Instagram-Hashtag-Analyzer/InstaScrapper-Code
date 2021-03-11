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
		
def insert_tag_like(cursor, tag_name, total_like_count): 
	add_tag = ("INSERT INTO tag_like "
						"(tagname, numLike) "
						"VALUES (%(name)s, %(numLike)s)")
	
	# data set for test only, DONE: data feeder implementation
	data_tag = {
		'name':       tag_name,
		'numLike':    total_like_count,
	}
	try:
		cursor.execute(add_tag, data_tag)
		
	except mysql.connector.IntegrityError:
		pass