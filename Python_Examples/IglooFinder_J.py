from selenium import webdriver
#from selenium.webdriver.common import action_chains, keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from random import randint
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# enable browser logging



def monitor_igloo(driver):

    time.sleep(2)
    if (len(driver.find_elements_by_css_selector("div[class^='widget_zone"))>0):
        element = driver.find_elements_by_css_selector("div[class^='widget_zone']")
        Igloo_run(element, driver)

    elif (len(driver.find_elements_by_css_selector("iframe[id^='google_ads_iframe_']"))>0):
        gframe = driver.find_elements_by_css_selector("iframe[id^='google_ads_iframe_']")

        for j in gframe:
            id = j.get_attribute("id")
            driver.switch_to.frame(id)
            if (len(driver.find_elements_by_css_selector("div[class^='widget_zone']"))>0):
                element = driver.find_elements_by_css_selector("div[class^='widget_zone']")
                print ("In Google iFrame")
                Igloo_run(element, driver)
                break
            else:
                print ("No Widget")
                driver.switch_to.default_content()


def Igloo_run(element, driver):
    li = []
    ad_list = []
    for e in element:
        li.append(idtest)

    print("\nLIST OF ID = "+str(li))
    for i in range(len(li)):
        print("ITEM = "+li[i])
        id_now = li[i]
        print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ START AT "+id_now+" ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        for z in range(4):

            e_ids = driver.find_elements_by_id(id_now)
            for e_id in e_ids:
                idt = e_id.get_attribute("id")
                att = e_id.find_elements_by_css_selector("div")
                driver.execute_script("return arguments[0].scrollIntoView();", e_id)

                if (len(att)>0):

                    partner = att[4].text
                    ad_list.append(partner)
                    status = att[5].text
                    timing = att[3].text
                    countdown = att[2].text
                    c = timing.split("s")
                    ig_status = att[1].text
                    if (str(partner) == "sntmedia"):

                        if (len(driver.find_elements_by_css_selector('iframe[class="SYNAPIFR"]'))>0):
                            iframe1 = driver.find_element_by_css_selector('iframe[class="SYNAPIFR"]')
                            print ("In SYNAPIFR")
                            driver.switch_to.frame(iframe1)
                            #driver.switch_to.default_content()
                            time.sleep(1)

                            if (len(driver.find_elements_by_css_selector('iframe[src="//w1.synapsys.us/images/"]'))>0):
                                iframe2 = driver.find_elements_by_css_selector('iframe[src="//w1.synapsys.us/images/"]')
                                for a in iframe2:
                                    if (a):
                                        if (len(driver.find_elements_by_css_selector('img[src*="w1.synapsys.us"]'))>0):
                                            psa = driver.find_element_by_css_selector('img[src*="w1.synapsys.us"]')
                                            print ("Its a PSA")
                                            e_ids.append(e)
                                            driver.switch_to.default_content()
                                        else:
                                            print("\nit is swap widget")
                                            e_ids.append(e)
                                            driver.switch_to.default_content()

                            else:
                                print ("Synacore Ad")
                                e_ids.append(e)
                                driver.switch_to.default_content()

                    print("AD NETWORK = "+str(partner))
                    print("PRICE = "+str(status))
                    print("TIMING = "+str(timing))
                    print("COUNTDOWN = "+str(countdown))
                    print("IG_STATUS = "+str(ig_status))

                    if (str(c[0]) == "N/A"):
                        time.sleep(2)
                        print ("----------------------------")
                    elif (((c[0])=='0') or (float(c[0])<0)):
                        time.sleep(2)
                        print ("----------------------------")
                    elif (float(c[0])>0):
                        time.sleep(float(c[0]))
                        print ("----------------------------")
