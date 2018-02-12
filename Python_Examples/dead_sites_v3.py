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
global sql_old
global counter

token = "proprietaryInfo"
slack_client = SlackClient(token)
BOT_NAME = 'snowflake-bot'

def connectDatabase(query):
    query_pid = []
    db = pymysql.connect(host="proprietaryInfo", port=3306, db="proprietaryInfo", user="proprietaryInfo", password="proprietaryInfo", read_timeout = 60)
    cursor = db.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    return data

def main():
    sql =  '''select a.partner_id, c.p_name, a.pageviews as current_pageviews, b.pageviews as last_hour_pageviews, d.2nd_pageviews as same_hour_yesterday_pageviews
                FROM yeti_hourly_synapsys a
                INNER JOIN yeti_hourly_synapsys b
                    ON a.partner_id = b.partner_id
                INNER JOIN partner c
                    ON a.partner_id = c.p_id,
                (
                    select partner_id, pageviews as 2nd_pageviews, data_date as 2nd_date from yeti_hourly_synapsys where mobile = 0
                ) as d
                WHERE   a.partner_id != 0
                        AND a.mobile=0
                        AND a.data_date >= now() - interval 1 hour
                        AND b.mobile=0
                        AND b.partner_id !=0
                        AND b.data_date >= now() - interval 2 hour
                        AND b.data_date <= now() - interval 1 hour
                        AND c.p_lineage not like('%/1806/%')
                        AND c.p_lineage not like('%/1749/%')
                        AND c.p_lineage not like('%/1874/%')
                        AND d.2nd_date = (from_unixtime(unix_timestamp(a.data_date) - 86400))
                        AND d.partner_id = a.partner_id;
    '''

    x = prettytable.PrettyTable(["PID","Domain","Percent Drop"])
    x.align = "l"
    x.padding_width = 5
    query_database = connectDatabase(sql)
    counter = 0
    for row in query_database:
        sameHour_yesterday = row[4]
        lastHour = row[3]
        currentHour = row[2]
        if (sameHour_yesterday != 0 and lastHour != 0):
            percent_drop_today = (currentHour - lastHour)/lastHour * 100
            percent_drop_yesterday = (currentHour - sameHour_yesterday)/sameHour_yesterday * 100
            if lastHour > 50:
                if(percent_drop_today <= -30 and percent_drop_yesterday <=-90):
                    x.add_row([row[0],row[1],int(percent_drop_today)])
                    counter += 1
    if(counter > 0):
        slack_client.api_call("chat.postMessage", channel="@proprietaryInfo", text="The following sites show significant drop in pageviews in the last hour: \n" + "```" + str(x) + "```", as_user=True)
        slack_client.api_call("chat.postMessage", channel="@rabindavid", text="The following sites show significant drop in pageviews in the last hour: \n" + "```" + str(x) + "```", as_user=True)
        slack_client.api_call("chat.postMessage", channel="p17_sites", text="The following sites show significant drop in pageviews in the last hour: \n" + "```" + str(x) + "```", as_user=True)
        print(str(datetime.now()) + ' ' + str(counter) + ' accounts returned on slack')
    else:
        print (str(datetime.now()) + " No reported accounts this hour")
print("-------------------------------------------------------")
print("DEAD_SITES: VERSION 3.0 | LAST EDITED: 11/13/17")
print("")
print("DEAD_SITES NOTIFIER HAS BEEN ACTIVATED")
print("ONLY ACTIVE BETWEEN 7 AM to 10 PM DAILY.")
print("-------------------------------------------------------")

schedule.every(60).minutes.do(main)

while True:
    if (int(datetime.now().hour) > 7 and int(datetime.now().hour) < 22):
        if (int(datetime.now().hour) == 8):
                time.sleep(3000) #58 minute of the hour
        schedule.run_pending()
    time.sleep(1)
