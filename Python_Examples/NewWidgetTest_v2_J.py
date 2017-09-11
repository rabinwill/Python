# Pass-fail marker - DONE
# Traverse through list and compare to actual list
# Embed

import time
import threading
import sys
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import queue
from datetime import datetime
from random import randint
from selenium.webdriver.common.keys import Keys
import IglooFinder as finder
import win32com.client as win32


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
def setUp_Chrome():
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
    print ("\nTesting In CHROME")
    return driver

def setUp_Edge():
    driverE = webdriver.Edge("C:\\Users\\Rabin.David\\AppData\\Local\\Programs\\Python\\Python35\\driver\\MicrosoftWebDriver.exe");
    driverE.implicitly_wait(10)
    driverE.maximize_window()
    print ("\nTesting In EDGE")
    return driverE

def setUp_IE():
    #driver_path_ie = ("C:\\Users\\Rabin.David\\AppData\\Local\\Programs\\Python\\Python35\\driver\\IEDriverServer.exe")
    # random_port =  randint(1,10000)
    # ie_capabilities = DesiredCapabilities.INTERNETEXPLORER
    # ie_capabilities['webdriver.ie.ensureCleanSession'] = True
    # driverIE = webdriver.Ie(executable_path=driver_path_ie, capabilities=ie_capabilities, port=random_port)
    # driverIE.maximize_window()
    driverIE = webdriver.Ie("C:\\Users\\Rabin.David\\AppData\\Local\\Programs\\Python\\Python35\\driver\\IEDriverServer.exe")
    driverIE.implicitly_wait(10)
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
    print ("\nTesting In FIREFOX")
    return driverFF

def setUp_Safari():
    driver = webdriver.Safari()
    driver.maximize_window()
    return driver

def os_check():
    OS = ""
    from sys import platform
    if platform == "darwin":
        OS = 'Mac'
    elif platform == "win32":
        OS = 'PC'
    return OS
#-----------------------------------------------
# Begin test
# 1. Create a new instance of the Chrome driver
# 2. Pull up sites in database to test
# 3. Run tests
# 4. Print test duration
#-----------------------------------------------
def test(sites,p_codes,product_list,deal):
    driver = ''
    embed = ''
    system = ''
    p = 0
    s = 0
    embedcode = ""
    mailtext = ""
    finalbody = ""
    system = os_check()
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = 'sample.example@example.com; sample1.example1@example.com'
    mail.Subject = ('QA Results for ' + deal)
    if (system == 'PC'):
        browsers = ["Firefox"]
    elif (system == 'Mac'):
        browsers = ['Firefox']
    for each in browsers:
        if(each == 'Firefox'):
            driver = setUp_Firefox()
        elif(each == 'Safari'):
            driver = setUp_Safari()
        elif(each == 'Chrome'):
            driver = setUp_Chrome()
        elif(each == 'Edge'):
            driver = setUp_Edge()
        elif(each == "IE"):
            time.sleep(5)
            driver = setUp_IE()
        t0 = datetime.now() # Create timer for test duration
        status = False
        test_status = 'Fail'
        window_home = ''

        for x in range(len(sites)): # Open sites in browser
            try:
                driver.get(sites[x])
                mailtext = (mailtext + "\nSite: " + sites[x])
                time.sleep(4)
                #driver.set_page_load_timeout(60)
                # remove_header(driver)
                # remove_popup(driver)
                # remove_subheader(driver)
                # remove_overlay(driver)
            except Exception:
                print("\nLOADING TIME OUT -> START TESTING")
                driver.execute_script("window.stop();")
                time.sleep(40)
                window_home = driver.window_handles[0]      # Set window_home as first window handle
            for product in product_list:
                try:
                    if (each == "IE" or each == "Edge" ):
                        driver.execute_script("document.getElementsByTagName('body')[0].innerHTML = '';")
                        print("Deleted Body")
                    embed = inject_embed(driver,p_codes[x],product)
                    time.sleep(20)
                    status = find_igloo(sites[x],driver,window_home,each,system,embed,product)
                    driver.switch_to.default_content()
                    finder.monitor_igloo(driver)
                    if (product.endswith('_wide')):
                        driver.set_window_size(975, 800)
                        time.sleep(15)
                        print("Wide widget in 975 View")
                        driver.set_window_size(660, 800)
                        print("Wide widget in 650 View")
                        time.sleep(15)
                        #driver.maximize_window()
                        driver.set_window_size(1500, 800)
                    driver.refresh()
                    driver.set_page_load_timeout(60)
                    time.sleep(4)
                    t1 = datetime.now()
                    print("Test duration: ", t1-t0)             # Print test duration

                except Exception as e:
                    print(e)
                    driver.quit()
                if(status == False):
                    test_status = 'Fail'
                elif (status == True):
                    test_status = 'Pass'
                print ("Test results: ", test_status)
                print ("{code}")
                embedcode = embedcode + "\n" + product + ": " + embed
            s = s+1
            finalbody = finalbody + mailtext + embedcode #
            embedcode = ""
            mailtext = ""
        driver.quit()
        print("Sleeping for 10")
        time.sleep(10)
        print("Quiting")
        print(finalbody)

        if ((s==len(sites)) and (each == 'Firefox')):
            finalbody = "QA has successfully tested the below product(s) on: \n" + finalbody + "\n\nIf you have any questions/concerns please feel free to reach out.\n\nThanks,\nRabin"
            print(finalbody)
            print("Sending Email")
            mail.Body = finalbody
            mail.Send()
        s=0

def remove_header(driver):
    # Remove header
    header = driver.find_element_by_css_selector("div[id^='header']")
    driver.execute_script("""
    var header = arguments[0];
    header.parentNode.removeChild(header);
    """, header)

def remove_subheader(driver):
    header = driver.find_element_by_css_selector("div[class='header_subheader']")
    driver.execute_script("""
    var header = arguments[0];
    header.parentNode.removeChild(header);
    """, header)

def remove_popup(driver):
    header = driver.find_element_by_css_selector("div[id='simplemodal-custom-container']")
    driver.execute_script("""
    var header = arguments[0];
    header.parentNode.removeChild(header);
    """, header)

def overlay(driver):
    header = driver.find_element_by_css_selector("div[class='simplemodal-overlay']")
    driver.execute_script("""
    var header = arguments[0];
    header.parentNode.removeChild(header);
    """, header)

#-----------------------------------------------
# Inject embed
#-----------------------------------------------
def inject_embed(driver,p_codes,product):
    p_code = p_codes
    testing_product = product

    # Dynamic Group Widgets (Entertainment, Weather, Money, Sports)
    if (product == 'dynamic_group_entertainment' or product == 'dynamic_group_weather' or product == 'dynamic_group_money' or product == 'dynamic_group_sports'):
        embed = ('''
        Proprietary Info ''')
        driver.execute_script(embed)
        script = '''Proprietary Info''' + p_code + '''&Proprietary Info=''' + product + '''Proprietary Info'''
        return script

    # Standard Inline (300x250)
    elif(product == 'inline_ad'):
        embed = ('''
        Proprietary Info ''')
        driver.execute_script(embed)
        script = '''Proprietary Info''' + p_code + '''&Proprietary Info=''' + product + '''Proprietary Info'''
        return script

    # Brick Ad (728x90)
    elif(product == 'inline_728x90'):
        embed = ('''
        Proprietary Info ''')
        driver.execute_script(embed)
        script = '''Proprietary Info''' + p_code + '''&Proprietary Info=''' + product + '''Proprietary Info'''
        return script

    elif(product == 'inline_300x600'):
        embed = ('''
        Proprietary Info ''')
        driver.execute_script(embed)
        script = '''Proprietary Info''' + p_code + '''&Proprietary Info=''' + product + '''Proprietary Info'''
        return script

    #Skyscraper (160x600)
    elif(product == 'inline_160x600'):
        embed = ('''
        Proprietary Info ''')
        driver.execute_script(embed)
        script = '''Proprietary Info''' + p_code + '''&Proprietary Info=''' + product + '''Proprietary Info'''
        return script

    #Wide Dynamic Unlinked
    elif (product == 'dynamic_group_entertainment_wide' or product == 'dynamic_group_weather_wide' or product == 'dynamic_group_money_wide' or product == 'dynamic_group_sports_wide'):
        embed = ('''
        Proprietary Info ''')
        driver.execute_script(embed)
        script = '''Proprietary Info''' + p_code + '''&Proprietary Info=''' + product + '''Proprietary Info'''
        return script

    elif (product == 'dodgy_drone'):
        embed = ('''
        Proprietary Info ''')
        driver.execute_script(embed)
        script = '''Proprietary Info''' + p_code + '''&Proprietary Info=''' + product + '''Proprietary Info'''
        return script
#-----------------------------------------------
# Inject debugger
#-----------------------------------------------
def inject_debugger(driver):
    driver.execute_script("Proprietary Info;")


#-----------------------------------------------
# Locate igloo on page
#-----------------------------------------------
def find_igloo(url,driver,window_home,each,system,embed,product): # Locate igloo in test

    status = False
    if (len(driver.find_elements_by_css_selector("div[class^='widget_zone']"))>0):
        driver.find_element_by_css_selector("div[class^='widget_zone']")
        print("{code:java}")
        print("=============== START OF TEST===================")
        print("Date/Time: " + str(datetime.now()))
        print("URL: " + str(url))
        print("Browser: " + system + " " + each)
        print("Embed Tested: " + embed)
        print("")
        print("INITIAL CHECK:")
        print("PASS: Igloo was found")
        inject_debugger(driver)
        if (product.startswith('dynamic_group')):
            iframes = locate_iframe(driver)
            status = locate_widget(iframes,driver,window_home,each)
        elif(product == 'inline_ad' or product == 'inline_728x90' or product == 'inline_160x600' or product =='inline_300x600' or product =='dodgy_drone'):
            print("N/A: Sidekick Test not required for this product")
            status = True
        print("=============== END OF TEST ====================")

    else:
        print("=============== START OF TEST ==================")
        print("Date/Time: " + str(datetime.now()))
        print("URL: " + str(url))
        print("Browser: " + each)
        print("Embed Tested: " + system + " " + embed)
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
    if (len(driver.find_elements_by_css_selector('iframe[class^="dwunlinkIframe"]')) > 0):
        iframes = driver.find_elements_by_css_selector('iframe[class^="dwunlinkIframe"]')
    else:
        print("ERROR: Can't locate iframe")
        print("=============== END OF TEST ====================")
    return iframes

#-----------------------------------------------
# Switch in - locate widget on page
#-----------------------------------------------
def locate_widget(iframes, driver,window_home,each):
    time.sleep(5)

    status = False
    status3 = False
    status4 = False
    status5 = False
    status6 = False
    status8 = False
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
        wide_iframe = iframe.get_attribute("class")
        print("PASS: iframe was found (" + str(wide_iframe) + ")")
        driver.execute_script("return arguments[0].scrollIntoView();", iframe) #scroll to view
        driver.execute_script("window.scrollBy(0,-100)")
        driver.switch_to.frame(iframe)

        print("")
        print("VISUAL CHECK:")


        # Locate IMAGE ID
        if (len(driver.find_elements_by_css_selector("div[id^='mainimg']")) > 0):
            tests = driver.find_elements_by_css_selector("div[id^='mainimg']")
            for test in tests:
                test_id = test.get_attribute("id")
                print("PASS: 'Profile Image' found (" + str(test.get_attribute("style")) + ")")
                # Click Profile Image
            status3 = True
        else:
            print("ERROR: 'Profile Image' not found")

        listpage_items = []
        # Locate WIDGET TITLE
        if (len(driver.find_elements_by_css_selector("div[id^='profile-title']")) > 0):
            tests = driver.find_elements_by_css_selector("div[id^='profile-title']")
            for test in tests:
                print("PASS: 'Widget Title' found (" +str(test.text) + ")")
            status4 = True
        else:
            print("ERROR: 'Widget Title' not found")


        # Locate NAVIGATION ARROWS
        if (len(driver.find_elements_by_css_selector("button[class^='cta_button-next']")) > 0):
            tests = driver.find_elements_by_css_selector("button[class^='cta_button-next']")
            print("PASS: 'Right Navigation' found")

            status5 = True

            list_item = []
            # Click right-navigation bar x10
            for i in range(10):
                #Locate CONTENT
                if (len(driver.find_elements_by_css_selector("div[class^='block-data']")) > 0):
                    items = driver.find_elements_by_css_selector("div[class^='block-data']")
                    for item in items:
                        string = item.text
                        if (each == 'Safari'):
                            string = ' '.join(string.split())
                            validation2 = ("CONTENT = "+ string)
                            list_item.append(validation2)
                        else:
                            item_list = string.split("\n")
                            try:
                                validation2 = ("CONTENT = "+ item_list[0] + " " + item_list[1] + " " + item_list[2] + " " + item_list[3])
                            except IndexError:
                                validation2 = ("CONTENT = "+ item_list[0] + " " + item_list[1] + " " + item_list[2])
                            list_item.append(validation2)
                        if (each == 'Safari'):
                            driver.find_element_by_css_selector("button[class^='cta_button-next']").send_keys(Keys.RETURN)
                        else:
                            driver.find_element_by_css_selector("button[class^='cta_button-next']").click()
                    right_nav = str("PASS: 'Right Navigation' works appropriately")
                else:
                    print("ERROR: 'Right Navigation' not found")


        if (len(driver.find_elements_by_css_selector("button[class^='cta_button-previous']")) > 0):
            tests = driver.find_elements_by_css_selector("button[class^='cta_button-previous']")
            print("PASS: 'Left Navigation' found")

            # Click left-navigation bar x10
            for i in range(len(list_item)):
                driver.find_element_by_css_selector("button[class^='cta_button-previous']").click()
                left_nav = str("PASS: 'Left Navigation' works appropriately")

            status6 = True
        else:
            print("ERROR: 'Left Navigation' not found")



        # Locate NEXT LIST
        if (len(driver.find_elements_by_css_selector("button[class^='cta_button-list leftTransform atomic_border atomic_bg']")) > 0):
            tests = driver.find_elements_by_css_selector("button[class^='cta_button-list leftTransform atomic_border atomic_bg']")
            print("PASS: 'Next List' button found")
            status8 = True

            #Click 'Next List'
            driver.find_element_by_css_selector("button[class^='cta_button-list leftTransform atomic_border atomic_bg']").click()
            next_list = str("PASS: 'Next List' button works appropriately")
        else:
            print("ERROR: 'Next List' button not found")

        time.sleep(5) # Allow for pages to fully load

        print ("")
        print("FUNCTIONALITY CHECK:")
        print(left_nav)
        print(right_nav)
        print(next_list)

        print("")
        print("WIDGET CONTENT: ")
        print(list_item)



        if(status3 == True and status4 == True and status5 == True and status6 == True and status8 == True):
            status = True

        return status
        driver.switch_to.default_content()
