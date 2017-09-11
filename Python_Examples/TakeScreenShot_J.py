'''from MySQLdb import *
import MySQLdb'''
import selenium
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

def database_connection_read():
    # Open database connection
    db = pymysql.connect(host="Proprietary Info",user="Proprietary Info",password="Proprietary Info",db="Proprietary Info")
    #db = pymysql.connect(host="127.0.0.1",user="root",password="",db="qaseleniumdb")
    return db
	
"""[function name: fetching_pid_data]
[return: urls]
[description: getting pid data from database]
"""
def fetching_pid_data(sql):
    pid = ""
    # prepare a cursor object using cursor() method
    db = database_connection_read()
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        pid = row[0]
    db.close()
    return pid

def login_func_yeti(driver):
	email = driver.find_element_by_id("email")
	password = driver.find_element_by_id("password")
	submit = driver.find_element_by_css_selector("button[class*='btn btn-success btn-block']")
	email.send_keys("Proprietary Info.com")
	password.send_keys("Proprietary Info")
	submit.click()
	time.sleep(5)
	if (driver.find_element_by_css_selector("div[class*='overlay vertical-center']")):
		driver.find_element_by_css_selector("span[class*='fa fa-remove'").click()
	return driver 

def take_screenshot(driver, date_string):
	some = driver.find_element_by_css_selector("div[class*='col-xs-12 row']")
	driver.execute_script("document.body.style.zoom='75%'")
	driver.execute_script("return arguments[0].scrollIntoView();", some)
	driver.get_screenshot_as_file('C:\\Users\\Rabin.David\\Desktop\\yetigraph' + date_string + '.jpeg') 
	return 0

def setup_chrome():
	driverPath = "C:\\Users\\Rabin.David\\AppData\\Local\\Programs\\Python\\Python35\\driver\\chromedriver.exe"
	driver = driver = webdriver.Chrome(driverPath)
	return driver 
	
def pID_URL(PId, driver):
	print(PId)
	driver.get("https://www.Proprietary Info.us/yeti-partner-dashboard?p_id="+str(PId))
	time.sleep(3)
	
	
def main():
	#driver = webdriver.Firefox()
	sql = "select p_id from partner_synapsys where p_domain = 'politico.com';"
	pid = fetching_pid_data(sql)
	date_string = time.strftime("%m-%d-%H-%M-%S")
	print(date_string)
	print(datetime.now())
	driver = setup_chrome()
	driver.set_window_size(1900, 800)
	driver.maximize_window()
	driver.get("https://www.Proprietary Info.us/yeti-dashboard")
	driver1 = login_func_yeti(driver)
	pID_URL(pid, driver)
	take_screenshot(driver1, date_string)
	time.sleep(4)
	driver.quit()
	slack_client.api_call('files.upload', channels="@rabindavid", filename='yetigraph.jpeg', file=open('C:\\Users\\Rabin.David\\Desktop\\yetigraph' + date_string + '.jpeg', 'rb'))
	os.remove('C:\\Users\\Rabin.David\\Desktop\\yetigraph' + date_string + '.jpeg')
	return 0
main()
	
