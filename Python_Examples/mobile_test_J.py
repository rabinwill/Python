# Mobile Test for Mobile Emuluations
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
import unittest
import IglooFinder as finder
import site_precheck as precheck
from selenium.webdriver.common.touch_actions import TouchActions

# ----------------------- INITIATING WEB-DRIVERS----------------------------
# INCLUDED:
# - ANDROID MOBILE (UNDER CONSTRUCTION)
# - ANDROID CHROME
# - IOS CHROME
# - IOS SAFARI
# ---------------------------------------------------------------------------
def setUp_AndroidMobile(): # Under Construction
    # DesiredCapabilities capabilities = new DesiredCapabilities();
    # capabilities.setCapability("deviceName", "Android");
    # capabilities.setCapability("platformName", "Android");
    # capabilities.setCapability("app", appFile.getAbsolutePath());
    # capabilities.setCapability("serial", deviceID);
    # capabilities.setCapability("newCommandTimeout", "120");
    # capabilities.setCapability("chromedriverExecutable", "Desktop/tpt/chromedriver"));
    # driver = new AndroidDriver(new URL("http://localhost:4723/wd/hub"), capabilities
    desired_capabilities = {}
    # 'xcrun simctl list' command to find all UDID
    desired_capabilities ['platformVersion'] = 'Android'
    desired_capabilities ['deviceName'] = 'Android'
    desired_capabilities ['app'] = appFile.getAbsolutePath()
    desired_capabilities ['serial'] = deviceID
    desired_capabilities ['newCommandTimeout'] = '120'
    driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_capabilities)
    return driver

def setUp_AndroidChrome():
  mobile_emulation = { "deviceName": "Samsung Galaxy S4" }
  chrome_options = webdriver.ChromeOptions()
  chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
  #driver = webdriver.Remote(desired_capabilities = chrome_options.to_capabilities())
  driver = webdriver.Chrome()
  driver.set_window_size(375,667)
  return driver

def setUp_iOSChrome():
  mobile_emulation = { "deviceName": "iPhone 6" }
  chrome_options = webdriver.ChromeOptions()
  chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
  # driver = webdriver.Remote('http://localhost:472/wd/hub',desired_capabilities = chrome_options.to_capabilities())
  driver = webdriver.Chrome()
  driver.set_window_size(375,667)
  return driver

def setUp_iOSSafari():
  desired_capabilities = {}
  # 'xcrun simctl list' command to find all UDID
  desired_capabilities['udid'] = '69842F06-973D-4F72-988C-E64A3156361F'
  desired_capabilities ['platformName'] = 'iOS'
  desired_capabilities ['platformVersion'] = '10.0'
  desired_capabilities ['browserName'] = 'Safari'
  desired_capabilities ['deviceName'] = 'iPhone Simulator'
  desired_capabilities ['automationName'] = 'XCUITest'
  driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_capabilities)
  return driver

# ----------------------- WEB-PAGE SETUP ---------------------------------

def inject_centipede(driver,p_codes,product):
  p_code = p_codes
  testing_product = product
  embed = ('''
  Proprietary Info ''')
  driver.execute_script(embed)
  script = '''Proprietary Info''' + p_code + '''&Proprietary Info=''' + product + '''Proprietary Info'''
  return script

def inject_debugger(driver):
  driver.execute_script("Proprietary Info")

def find_centipede(url,driver,window_home,each,embed,product,text_file):
  status = False
  if(product == 'default_mobile'):
    if (len(driver.find_elements_by_css_selector("div[class^='widget_zone']"))>0):
          driver.find_element_by_css_selector("div[class^='widget_zone']")
          text_file.write("=============== START OF TEST===================")
          text_file.write("\nDate/Time: " + str(datetime.now()))
          text_file.write("\nURL: " + str(url))
          text_file.write("\nMobile Emulation: " + each)
          text_file.write("\nEmbed Tested: " + embed)
          text_file.write("")
          text_file.write("\n\nINITIAL CHECK:")
          text_file.write("\nPASS: Igloo was found")
          inject_debugger(driver)
          text_file.write("\nN/A: Centipede Test not required for this product")
          text_file.write("\n=============== END OF TEST ====================")

  elif (len(driver.find_elements_by_css_selector("iframe[class^='centipedeIframe']"))>0):
      snt = driver.find_elements_by_css_selector("iframe[class^='centipedeIframe']")
      for y in snt:
          first = driver.find_element_by_css_selector("iframe[class^='centipedeIframe']")
          text_file.write("=============== START OF TEST===================")
          text_file.write("\nDate/Time: " + str(datetime.now()))
          text_file.write("\nURL: " + str(url))
          text_file.write("\nMobile Emulation: " + each)
          text_file.write("\nEmbed Tested: " + embed)
          text_file.write("")
          driver.execute_script("return arguments[0].scrollIntoView();", first)
          text_file.write("\nPASS: Centipede Found")
          inject_debugger(driver)
          driver.switch_to.frame(first)
          test_centipede(each,driver,text_file)
          text_file.write("\n=============== END OF TEST ====================")


  else:
      text_file.write("=============== START OF TEST ==================")
      text_file.write("\nDate/Time: " + str(datetime.now()))
      text_file.write("\nURL: " + str(url))
      text_file.write("\nMobile Emulation: " + each)
      text_file.write("\nEmbed Tested: " + embed)
      text_file.write("")
      text_file.write("\nINITIAL CHECK:")
      text_file.write("\nERROR: Centipede was not found")
      text_file.write("\n=============== END OF TEST ====================")
  return status

def test_centipede(each,driver,text_file):
    list_item = []
    info_list = []
    info_str_combine = ""
    if (len(driver.find_elements_by_css_selector("div[class^='helper']"))>0):
        title = driver.find_element_by_css_selector("div[class^='helper']")
        text_file.write ("\nList Title: " + str(title.text))
        time.sleep(4)
    if (len(driver.find_elements_by_css_selector("div[class^='slider_block']"))>0):
        texts = driver.find_element_by_css_selector("div[class^='slider_block']")
        if (len(driver.find_elements_by_css_selector("div[class^='info']"))>0):
            info = driver.find_elements_by_css_selector("div[class^='info']")
            for x in info:
                infostr = x.text
                info_list = infostr.replace("\n", " ")
                info_str_combine = info_str_combine +", "+info_list
            validation2 = ("CONTENT = "+info_str_combine)
            list_item.append(validation2)
            text_file.write(list_item)
            print("scrolling Right")
            if(each == 'iOSChrome' or each == 'AndroidChrome'):
              touchactions = TouchActions(driver).scroll_from_element(texts,1500,0).perform()
              touchactions = TouchActions(driver).release(1500,0)
              time.sleep(2)
            elif(each == 'iOSSafari'):
              print("scrolling right")
              time.sleep(3)
              driver.execute_script("mobile: scroll", {"direction": "right"})
              print("scrolling right")
              time.sleep(3)
              driver.execute_script("mobile: scroll", {"direction": "right"})
              print("scrolling left")
              time.sleep(3)
              driver.execute_script("mobile: scroll", {"direction": "left"})
        if (len(driver.find_elements_by_css_selector("div[class^='ad_spacer']"))>0):
            ad_spacer = driver.find_elements_by_css_selector("div[class^='ad_spacer']")
            if (len(driver.find_elements_by_css_selector("div[class^='widget_zone"))>0):
                element = driver.find_elements_by_css_selector("div[class^='widget_zone']")
                Igloo_run(element, driver)
        if (len(driver.find_elements_by_css_selector("div[class^='next_list']"))>0):
            nextarrow = driver.find_element_by_css_selector("div[class^='next_list']")
            text_file.write("\nFOUND BUTTON: Next List")
            driver.execute_script("return arguments[0].scrollIntoView();", nextarrow)
            touchactions = TouchActions(driver).tap(nextarrow)
            touchactions.perform()
            time.sleep(3)
            text_file.write("\n\nFUNCTIONALITY CHECK: Next List is good")
            if (len(driver.find_elements_by_css_selector("div[class^='helper']"))>0):
                title = driver.find_element_by_css_selector("div[class^='helper']")
                text_file.write ("\nNEW List Title: " + str(title.text))

        print ("Done")

# ----------------------- MAIN ---------------------------------
def test(sites,p_codes,mobile_product_list):
  browsers = ['AndroidMobile']
  for each in browsers:
    if (each == 'iOSSafari'):
      driver = setUp_iOSSafari()
    elif (each == 'iOSChrome'):
      driver = setUp_iOSChrome()
    elif (each == 'AndroidChrome'):
      driver = setUp_AndroidChrome()
    elif( each == 'AndroidMobile'):
      driver = setUp_AndroidMobile()


    for x in range(len(sites)):
      try:
        driver.get(sites[x])
        time.sleep(10)
        driver.set_page_load_timeout(60)
        new_site = sites[x].replace('http://','')
        final_site = new_site.replace('.com','')
        driver.execute_script("window.stop();")
        window_home = driver.window_handles[0]

        for product in mobile_product_list:
          file_name = each + "_" + product + "_" + final_site
          file_name.strip() # Removes all whitespace in string
          print("============== START OF TEST ==============")
          print(file_name)

          with open(file_name+".txt","w") as text_file: # Write to text file_name
            t0 = datetime.now()
            precheck.test(driver)
            embed = inject_centipede(driver,p_codes[x],product)
            time.sleep(20)
            find_centipede(sites[x],driver,window_home,each,embed,product,text_file)
            finder.monitor_igloo(driver,text_file)
            time.sleep(30)
            driver.refresh()
            t1 = datetime.now()
            print("Test duration: ", t1-t0)
            print("============== END OF TEST ==============")
            print("\n")
      except Exception as e:
          print(e)
          driver.quit()

    driver.quit()
