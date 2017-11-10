#To watch video please visit: https://youtu.be/S5O3HLHzlUg

# Libraiers needed
import time
import sys
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from datetime import datetime
from selenium.webdriver.common.keys import Keys
import win32com.client as win32
import selenium
import logging

def setUp_Chrome(system):                                   #setting up chrome driver
    options = webdriver.ChromeOptions()
    d = DesiredCapabilities.CHROME
    d['loggingPrefs'] = { 'browser':'ALL' }
    options.add_argument("--window-size=1900,800")
    options.add_argument("--screen-resolution=1920x1200")
    #options.add_argument('--disk-cache-size=1')
    #options.add_argument('--media-cache-size=1')
    options.add_argument('--ignore-certificate-errors')
    #options.add_experimental_option("prefs", {"profile.default_content_settings.cookies": 2})
    #options.add_experimental_option("prefs", {"profile.block_third_party_cookies": True})
    driverPath = "C:\\Users\\Rabin.David\\AppData\\Local\\Programs\\Python\\Python35\\driver\\chromedriver.exe"  #location of Chrome Driver
    driver = webdriver.Chrome(driverPath, chrome_options=options, desired_capabilities=d)
    driver.maximize_window()
    print ("\nTesting In CHROME " + system)
    logging.info("Chrome Driver was Successfully Setup")
    return driver

def login_func(driver):    #Logging in to Memember account
    email = driver.find_element_by_id("email")              #Finding email field
    password = driver.find_element_by_id("password")        #Finding password field
    submit = driver.find_element_by_css_selector("button[class*='btn btn-primary btn-lg btn-block semi-bold']")    #Finding SignIn button
    email.send_keys("rabincool_rocking@yahoo.co.in")            #Entering email address
    print("PASS: Email Address Entered")
    password.send_keys("ProprietaryInfo")                           #Entering password
    print("PASS: Password Entered")
    submit.click()                                              #Clicking on SignIn button
    print("PASS: Logged In")
    logging.info("Logged in to Memeber Account")
    time.sleep(9)                                               #Sleeping to wait for page to load
    #wait = WebDriverWait(driver, 7)
    #wait.until(EC.title_contains("https://watch.sling.com/browse/dynamic/on-now"))
    #print ("Done Waiting")

def take_screenshot(driver, date_string):   #function to take screenshot
    try:
        driver.get_screenshot_as_file('C:\\Users\\Rabin.David\\Desktop\\Sling' + date_string + '.png')  #Taking SS and saving the directory
        logging.info("Screenshot Captured")
        print("PASS: Screenshot Captured")
    except Exception as e:
        logging.error("Screenshot Capture Failed")
        print("FAIL: Screenshot Failed")
        print(e)

def os_check():     #Function to check current system
    OS = ""
    from sys import platform
    if platform == "darwin":
        OS = 'Mac'
    elif platform == "win32":
        OS = 'PC'
    return OS

def LoggingSetup(): #setting up Log file
    logging.basicConfig(format='%(asctime)-2s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',filename="C:\\Users\\Rabin.David\\Desktop\\Sling_Log.log", filemode='w', level=0)

def main():
    LoggingSetup()                          #setting up Log file
    logging.info("Test Started")
    system = os_check()                     #Checking current system
    print("Testing on: " + system)
    driver = setUp_Chrome(system)           #setting up chrome drive
    t0 = datetime.now()                     # Create timer for test duration
    driver.get("https://www.sling.com/")
    if (len(driver.find_elements_by_css_selector("li[class^='user-login signIn hidden-on-load']")) > 0):  #Finding the Memeber Login button
        print("PASS: Login Button Found")
        driver.find_element_by_css_selector("li[class^='user-login signIn hidden-on-load']").click()   #clicking login button
        login_func(driver)
        date_string = time.strftime("%m-%d-%H-%M-%S")
        take_screenshot(driver, date_string)
    else:
        print("FAIL: Login Button not found")
    time.sleep(15)
    t1 = datetime.now()
    duration = t1-t0
    print("Test Duration: " + str(duration))
    logging.info("Test Duration: " + str(duration))
    logging.info("Test Finished")
    driver.quit()                           #quitting driver session
main()
