'''
Created on Jun 27, 2018

@author: karsu
'''
# To install the Python client library:
# pip install -U selenium

# Import the Selenium 2 namespace (aka "webdriver")
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import sys

def getfiles_from_finviz():
    
    #caps = DesiredCapabilities().CHROME
    #caps["pageLoadStrategy"] = "normal"  #  complete
    #driver = webdriver.Chrome(desired_capabilities=caps)
    
    driver = webdriver.Chrome()
    
    print('------- Going to Finviz site -------')
    
    try:
        driver.get('https://finviz.com/login.ashx')
    except:
        print(sys.exc_info()[0])
        driver.quit()
        sys.exit()

#===============================================================================
# to_continue = input("To continue enter 'y' or 'q' to quit : ")
# if (to_continue == 'q'):
#     driver.quit()
#     sys.exit()
#===============================================================================

    username = driver.find_element_by_name('email')
    password = driver.find_element_by_name('password')
    username.send_keys("")
    password.send_keys("")
    login_attempt = driver.find_element_by_xpath("//*[@type='submit']")
    
    print('------- Logging in -------')
    
    try:
        login_attempt.submit()
    except:
        print(sys.exc_info()[0])
        driver.quit()
        sys.exit()

#===============================================================================
# to_continue = input("To continue enter 'y' or 'q' to quit : ")
# if (to_continue == 'q'):
#     driver.quit()
#     sys.exit()
#===============================================================================

    print('------- Gap up download -------')
        
    time.sleep(3)
    driver.get('https://elite.finviz.com/screener.ashx?v=111&f=sh_avgvol_o500,sh_curvol_o750,sh_price_o2,sh_relvol_o1.5,ta_gap_u1&ft=4&o=-volume')
    technicallink = driver.find_element_by_partial_link_text("Technical").click()
    time.sleep(5)
    driver.find_element_by_partial_link_text("export").click()
    
    time.sleep(5)
    
    print('------- Gap down download -------')
    
    driver.get('https://elite.finviz.com/screener.ashx?v=111&f=sh_avgvol_o500,sh_curvol_o750,sh_price_o2,sh_relvol_o1.5,ta_gap_d1&ft=4&o=-change')
    technicallink = driver.find_element_by_partial_link_text("Technical").click()
    time.sleep(5)
    driver.find_element_by_partial_link_text("export").click()
    time.sleep(10)
    
    
    driver.quit()

if __name__ == '__main__': 
    getfiles_from_finviz()


#https://elite.finviz.com/screener.ashx?v=111&f=sh_avgvol_o500,sh_curvol_o750,sh_price_o2,sh_relvol_o1.5,ta_gap_d1&ft=4&o=-change
