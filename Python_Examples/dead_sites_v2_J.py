import selenium
import schedule
from selenium import webdriver
from datetime import datetime, time, timedelta
import time
from slackclient import SlackClient
import sys
import pymysql
import os
import prettytable

token = "Proprietary Info"
slack_client = SlackClient(token)
BOT_NAME = 'snowflake-bot'

def yeti_databse_connection_read():
    db = pymysql.connect(host="Proprietary Info", port=3306, db="Proprietary Info", user="Proprietary Info", password="Proprietary Info", read_timeout = 60)
    return db

def fetching_sql_data(sql):
    pid = []
    p_name = []
    newlist = []
    db = yeti_databse_connection_read()
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    x = prettytable.PrettyTable(["PID", "Domain"])
    x.align = "l"
    # x.set_field_align("PID","l") #Left align
    x.padding_width = 10 # One space between column edges and contents (default)
    for row in data:
        x.add_row(row)
    return x

def main():
    time = datetime.now() + timedelta(hours=5)
    sql = '''select 	a.partner_id,
		                b.p_name
                FROM 	yeti_hourly_synapsys a
                		INNER JOIN partner b
                			ON a.partner_id = b.p_id
                WHERE 	a.partner_id != 0
                		AND a.mobile=0
                		AND a.pageviews =0
                		AND a.data_date >= now() - interval 60 minute'''
    try:
        pid = fetching_sql_data(sql)
    except pymysql.err.OperationalError as e:
        print("ERROR: Connection error to the database")
    slack_client.api_call("chat.postMessage", channel="@Proprietary Info", text="The following sites are indicating 0 pageviews in the last hour: \n" + "```" + str(pid) + "```", as_user=True)
    slack_client.api_call("chat.postMessage", channel="@rabindavid", text="The following sites are indicating 0 pageviews in the last hour: \n" + "```" + str(pid) + "```", as_user=True)

print("-------------------------------------------------------")
print("DEAD_SITES NOTIFIER HAS BEEN ACTIVATED")
print("ONLY ACTIVE BETWEEN 7 AM to 10 PM DAILY.")
print("-------------------------------------------------------")
if (datetime.now().hour > 7 or datetime.now().hour < 22):
    schedule.every(60).minutes.do(main)
while True:
    schedule.run_pending()
    time.sleep(1)
