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