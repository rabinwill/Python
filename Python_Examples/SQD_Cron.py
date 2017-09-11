# Author: Rabin W David
# Date: 05/09/2016
# SQD Script Test
# Python Version Used: 2.7.5 in a RHEL 7.1 environment.
#



#importing the packages/libraries needed
#!/usr/bin/env python
from crontab import CronTab, CronItem
from datetime import datetime, timedelta
import subprocess;
import string;
import time;
import re;

#Getting Access to crontab
system_cron = CronTab()
system_cron1=CronItem()
user_cron = CronTab('root')
file_cron = CronTab()
mem_cron = CronTab(tab="""
  * * * * * command
""")

#Taking user input
fileloc = (raw_input("Please Enter the File Location and the file Name \n(ex: /root/touchfile.txt):"))
times = int (raw_input("Specify the number of times cron will touch the file \n(ex: 2 minutes):"))
nfile = (raw_input("Please enter the the renamed file location and prefix \n (ex: /root/rotate/pythontest):"))
runtime1 = int(raw_input("Please Specify how long would you like the program to run \n (0 for forever until interrupt):"))
runtime = time.time() + 60 * runtime1							#Setting the run time in seconds
start_time = time.time()

addtouch = "touch" + " " + fileloc							#adding touch to command
today = datetime.now()
t7 = today - timedelta(seconds=420)							#The last 7 minutes
todayd = today.day
month  = time.strftime("%b")
mondate = month +"  "+ str(todayd)
count  = 0
touch1 = 0
x  = 1

def WriteToFileLogic():
	global fileloc, nfile, count, touch1, x, addtouch, todayd, month
	with open("/var/log/cron","r") as infile:					#Opening Cron log for reading
		searchlines = infile.readlines()
		for line in searchlines:
			if ("touch" in line):
				touch1 += 1
				match = re.search("/(\w+):(\w+):(\w+)/", line)          #Regular expression for hour, minute and second
				if match:
					logDate = datetime(today.year, today.month, today.day, match[0], match[1], match[2])
					if (logDate >= t7):                             #If times is greater or equal to t-7minutes
                            			count += 1
						writedata = month+" "+str(todayd)+" "+ str(touch1)+ " times"
                                		f.write(writedata)			#Write number of touches with date
                                		f.close()

                        	if (count == 15):					#If touched 15 times
			                f = open(fileloc, 'a')
					writedata = month+" "+str(todayd)+" "+ str(touch1)+ " times"
					print(writedata)
		                        f.write(writedata)
		                        f.close()
		                        nfile1 = nfile+"."+str(x)			#Incrementing touched file name
					fileloc = nfile1
		                        x+=1
					count = 0
					touch1 = 0

			if ("Error" or "Warning" in line):				#If error or warning exists in cron log
                                f = open(fileloc, 'a')
                                f.write(line)
                                f.close()





job = system_cron.new(command=addtouch)							#Creating a new cron job
job.minute.every(times)									#Adding minute slice
system_cron.write(user='root')								#Writing to crontab

if (runtime1 == 0):									#If run forever
	while True:
		try:
			WriteToFileLogic()
		except KeyboardInterrupt:						#Handling keyboard interrupt
			print(" \nExit due to user keyboard interrupt.\n")
			break

else:
	while (time.time() < runtime): 							#Loop to run for certain seconds
		WriteToFileLogic()
	print("\nSuccess\n")
