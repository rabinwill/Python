'''from MySQLdb import *
import MySQLdb'''
import selenium
import schedule
from selenium import webdriver
from datetime import datetime, time
import time
from slackclient import SlackClient
import sys
import pymysql
import os

token = "Proprietary Info"
slack_client = SlackClient(token)
BOT_NAME = 'snowflake-bot'

def yeti_databse_connection_read():
	db = pymysql.connect(host="Proprietary Info", port=3306, db="Proprietary Info", user="Proprietary Info", password="Proprietary Info", read_timeout = 60)
	return db


def fetching_pid_data(sql):
	pid = []
	# prepare a cursor object using cursor() method
	db = yeti_databse_connection_read()
	cursor = db.cursor()
	cursor.execute(sql)
	data = cursor.fetchall()
	if(data):
		for row in data:
			pid.append(row[0])
	db.close()
	return pid

def main():
	#driver = webdriver.Firefox()
	name = "inline_ad"
	pid = []
	sql = "select widget_type, url, data_date from yeti_ingest_widgets WHERE url LIKE '%Proprietary Info%' and widget_type like '"+"%"+name+"%"+"' and data_date >=DATE_SUB(NOW(), INTERVAL 60 MINUTE) GROUP BY data_date ORDER BY data_date DESC LIMIT 100;"
	print(sql)
	try:
		pid = fetching_pid_data(sql)
	except pymysql.err.OperationalError as e:
		print("Active User: No data for first query")

	if(len(pid) > 20):
		slack_client.api_call("chat.postMessage", channel="@rabindavid", text="Found Inline Ad on majorleaguegaming" + str(pid), as_user=True)
		slack_client.api_call("chat.postMessage", channel="@Proprietary Info", text="Found Inline Ad on majorleaguegaming" + str(pid), as_user=True)
	else:
		print("no data")
# main()

schedule.every(1).minutes.do(main)
while True:
	schedule.run_pending()
	time.sleep(1)
