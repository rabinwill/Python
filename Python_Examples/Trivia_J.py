# Pass-fail marker - DONE
# Traverse through list and compare to actual list
# Data validation test
# Embed

import time
import threading
import sys
from selenium import webdriver
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import queue
from datetime import datetime
from random import randint

#-----------------------------------------------
# View the list of sites in the test
#-----------------------------------------------
def view(): # View the list of sites in the test
    for x in range(len(sites)):
        print(sites[x])

#-----------------------------------------------
# Add new sites to the list of sites
#-----------------------------------------------
def push():
    new_site = raw_input("Please type the URL you wish to add to the list: ")
    sites.append(new_site)

#-----------------------------------------------
# Set test incognito-mode
#-----------------------------------------------
def setUp_chrome():
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
    driverPath = "C:\\Users\\Rabin.David\\AppData\\Local\\Programs\\Python\\Python35\\driver\\chromedriver.exe"
    driver = webdriver.Chrome(driverPath, chrome_options=options, desired_capabilities=d)
    driver.maximize_window()
    print ("\nTesting on Chrome")
    return driver

def setUp_Edge():
    driverE = webdriver.Edge("C:\\Users\\Rabin.David\\AppData\\Local\\Programs\\Python\\Python35\\driver\\MicrosoftWebDriver.exe");
    driverE.implicitly_wait(10)
    driverE.maximize_window()
    print ("\nTesting on Edge")
    return driverE

def setUp_IE():
    driver_path_ie = ("C:\\Users\\Rabin.David\\AppData\\Local\\Programs\\Python\\Python35\\driver\\IEDriverServer.exe")
    random_port =  randint(1,10000)
    ie_capabilities = DesiredCapabilities.INTERNETEXPLORER
    ie_capabilities['webdriver.ie.ensureCleanSession'] = True
    driverIE = webdriver.Ie(executable_path=driver_path_ie, capabilities=ie_capabilities, port=random_port)
    driverIE.maximize_window()
    print ("\nTesting on IE")
    return driverIE

def setUp_Firefox():
    port =  randint(1,10000)
    print("PROCESS PORT = "+str(port))
    profile = webdriver.FirefoxProfile()
    #profile.set_preference("general.useragent.override", bot)
    profile.set_preference("browser.cache.disk.enable", False)
    profile.set_preference("browser.cache.memory.enable", False)
    profile.set_preference("browser.cache.offline.enable", False)
    profile.set_preference("network.http.use-cache", False)
    profile.set_preference("webdriver.firefox.port", port)
    profile.set_preference("capability.policy.default.Window.QueryInterface","allAccess")
    profile.set_preference("capability.policy.default.Window.frameElement.get","allAccess")
    profile.set_preference("http.response.timeout", 0)
    profile.set_preference("dom.max_script_run_time", 0)
    driverFF = webdriver.Firefox(profile)
    print ("\nTesting on Firefox")
    return driverFF

#-----------------------------------------------
# Begin test
# 1. Create a new instance of the Chrome driver
# 2. Pull up sites in database to test
# 3. Run tests
# 4. Print test duration
#-----------------------------------------------
def test():
    t0 = datetime.now() # Create timer for test duration
    driver = setUp_Firefox()
    driver.set_page_load_timeout(60)
    #driver.maximize_window()
    status = False
    test_status = 'Fail'
    window_home = ''



    for x in range(len(sites)): # Open sites in browser
        try:
            driver.get(sites[x])
            time.sleep(10)
        except Exception:
            print("\nLOADING TIME OUT -> START TESTING")
            driver.execute_script("window.stop();")
            window_home = driver.window_handles[0] # Set window_home as first window handle
        try:
            time.sleep(10)
            iframes = locate_iframe(driver)
            status = locate_widget(iframes,driver,window_home)
        except Exception as e:
            print(e)
            driver.quit()
        t1 = datetime.now()
        print("Test duration: ", t1-t0) # Print test duration
        if(status == False):
            test_status = 'Fail'
        elif (status == True):
            test_status = 'Pass'
        print ("Test results: ", test_status)

    driver.quit()

def inject_debugger(driver):
    driver.execute_script("igloo.toggleDebug();")


#-----------------------------------------------
# Locate igloo on page
#-----------------------------------------------
def find_igloo(url,driver,window_home, iframes): # Locate igloo in test

    status = False
    #changed iframe for Comet. Should find Widget_zone
    if (len(driver.find_elements_by_css_selector("div[class^='widget_zone']"))>0):
        driver.find_element_by_css_selector("div[class^='widget_zone']")
        print("=============== START OF TEST===================")
        print("Date/Time: " + str(datetime.now()))
        print("URL: " + str(url))
        print("")
        print("INITIAL CHECK:")
        print("PASS: Igloo was found")
        #inject_debugger(driver)
        #iframes = locate_iframe(driver)
        status = locate_widget(iframes,driver,window_home)
        print("=============== END OF TEST ====================")

    else:
        print("=============== START OF TEST ==================")
        print("Date/Time: " + str(datetime.now()))
        print("URL: " + str(url))
        print("")
        print("INITIAL CHECK:")
        print("ERROR: Igloo was not found")
        print("=============== END OF TEST ====================")
    return status

#-----------------------------------------------
# Locate igloo iframe on page
#-----------------------------------------------
def locate_iframe(driver):
    iframes = []
    if (len(driver.find_elements_by_css_selector('iframe[src^="/app/ads/widget1.html"]')) > 0):
        iframes = driver.find_elements_by_css_selector('iframe[src^="/app/ads/widget1.html"]')
        print(iframes)
        #iframes = driver.find_elements_by_css_selector('iframe[id^="div_pfwidget"]')
    else:
        print("ERROR: Can't locate iframe")
        print("=============== END OF TEST ====================")
    return iframes

def remove_header(driver):
    if (len(driver.find_elements_by_css_selector("div[class^='header']"))>0):
        header = driver.find_element_by_css_selector("div[class^='header']")
        driver.execute_script("""
        var header = arguments[0];
        header.parentNode.removeChild(header);
        """, header)
        print ("Header Removed")
    else:
        print("Page Does not have a HEADER")

def remove_skin(driver):
    if (len(driver.find_elements_by_css_selector("div[id='skin']"))>0):
        header = driver.find_element_by_css_selector("div[id='skin']")
        driver.execute_script("""
        var header = arguments[0];
        header.parentNode.removeChild(header);
        """, header)
        print ("Skin Removed")
    else:
        print ("Page Does not have SKIN")
#-----------------------------------------------
# Switch in - locate widget on page
#-----------------------------------------------
def locate_widget(iframes, driver,window_home):
    time.sleep(5)

    status = False
    status3 = False
    status4 = False
    status5 = False
    status6 = False
    status8 = False
    status9 = False
    facebook = ''
    twitter = ''
    image = ''
    title = ''
    left_nav = ''
    right_nav = ''
    full_list = ''
    next_list = ''

    # Locate iFRAME ID
    for iframe in iframes:
        #wide_iframe = iframe.get_attribute("class")
        print("PASS: Trivia Widget iframe was found")
        driver.execute_script("return arguments[0].scrollIntoView();", iframe) #scroll to view
        driver.execute_script("window.scrollBy(0,-100)")
        print (iframe)
        driver.switch_to.frame(iframe)
        print("")
        print("VISUAL CHECK:")

        twiframe = driver.find_element_by_css_selector('iframe[class^="twiframe"]')
        driver.switch_to.frame(twiframe)
        # Locate IMAGE ID
        if (len(driver.find_elements_by_css_selector("div[class^='trivia_image_container']")) > 0):
            tests = driver.find_elements_by_css_selector("div[id^='pixelateContainer']")
            for test in tests:
                print("PASS: 'Trivia BG Image' found (" + str(test.get_attribute("style")) + ")")
            status3 = True
        else:
            print("ERROR: 'Profile Image' not found")

        listpage_items = []



        # Locate Trivia Question Options
        if (len(driver.find_elements_by_css_selector("div[class^='trivia_options_container']")) > 0):
            tests = driver.find_elements_by_css_selector("div[class^='trivia_options_container']")
            print("PASS: 'Trivia Options' found")
            status4 = True
            list_item = []
            i=1
            for x in range(10):
                # Locate Trivia Question
                if (len(driver.find_elements_by_css_selector("div[class^='trivia_question']")) > 0):
                    tests = driver.find_elements_by_css_selector("div[class^='trivia_question']")
                    for test in tests:
                        print("PASS: 'Trivia Question #"+str(x)+"' found (" +str(test.text) + ")")
                    status4 = True
                else:
                    print("ERROR: 'Trivia Question' not found")
                if (len(driver.find_elements_by_css_selector("li[class^='button']")) > 0):
                    items = driver.find_elements_by_css_selector("li[class^='button']")
                    status5 = True
                    for item in items:
                        string = item.text
                        item_list = string.split("\n")
                        validation2 = (" OPTION "+str(i)+": "+ item_list[0] + " ")
                        list_item.append(validation2)
                        i += 1
                    print(list_item)
                    print("")
                    list_item = []
                    i=1
                l = items[randint(0, len(items)-1)]
                l.click()
                nextbutton = driver.find_element_by_css_selector("div[id^='next_question']")
                nextbutton.click()
                time.sleep(2)
                items = driver.find_elements_by_css_selector("li[class^='button']")
        else:
            print("ERROR: 'Options' not found")

        #Locate Total Score
        if(len(driver.find_elements_by_css_selector("div[class^='score_container']"))>0):
            scores = driver.find_element_by_css_selector("div[class^='score_container']")
            status6 = True
            string = str(scores.text)
            string = string.replace("\n"," ")
            print("PASS: 'Trivia Scores' found (" +string + ")")

        #Locate Try Again
        if(len(driver.find_elements_by_css_selector("span[class^='try_again']"))>0):
            tryagain = driver.find_elements_by_css_selector("span[class^='try_again']")
            status7 = True
            for z in tryagain:
                string = z.text
                print("PASS: '" +string+ "' found")
        else:
            print("ERROR: 'Try Again' not found")

        #Find other Trivia Options
        if (len(driver.find_elements_by_css_selector("ul[class^='other_content_options_container']"))>0):
            triviaoption = driver.find_elements_by_css_selector("ul[class^='other_content_options_container']")
            status8 = True
            for r in triviaoption:
                string = str(r.text)
                opts = string.replace("\n"," ")
                print("PASS: 'Trivia Options' found (" +opts + ")")
            triviaoption = driver.find_elements_by_css_selector("div[class^='animation_container']")
            l = triviaoption[randint(0, len(triviaoption)-1)]
            l.click()
            if (len(driver.find_elements_by_css_selector("div[class^='trivia_question']")) > 0):
                status9 = True
                print("PASS:  Clicked on 'New Trvia Option'")
                time.sleep(2)
                tests = driver.find_elements_by_css_selector("div[class^='trivia_question']")
                for test in tests:
                    print("PASS:  New 'Trivia Question' found (" +str(test.text) + ")")
            else:
                print("ERROR: Could not Click on 'Trivia Options'")
        else:
            print("ERROR: 'Trivia Options' not found")


    if(status3 == True and status4 == True and status5 == True and status6 == True and status8 == True and status9 == True):
        status = True

        return status
        driver.switch_to.default_content()

# =======================================================
# Here is the start of the actual Snowflake Implementation Test
# =======================================================
sites = ['ProprietaryInfo.com']


# while True:

print("")
print("SNOWFLAKE IMPLEMENTATION MENU: ")
print("================================================")
print("1. View list of sites")
print("2. Add site to list")
print("3. Begin test")
print("4. Exit")
print("================================================")
user_input = int(input("Please enter your menu choice: "))
print ("")

if user_input == 1:
    view()
if user_input == 2:
    push()
if user_input == 3:
    test()
if user_input == 4:
    quit()
