'''
Created on Mar 3, 2017

@author: OA-User2
'''
import unittest

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test(unittest.TestCase):


    def setUp(self):
        global driver
        driver=webdriver.Chrome()
        url='http://wwwdev.openagent.com.au/find-agents/nsw/dover-heights/2030/1/recent?ref=&tid='
        driver.get(url);
        driver.maximize_window()
        driver.implicitly_wait(20)


    def tearDown(self):
        driver.quit()


    def testSearchResult(self):
 #       WebDriverWait(driver, 10).until(
  #          EC.visibility_of_element_located((By.XPATH,"//input[contains(@placeholder,'Name')]")))
  #      driver.find_element_by_xpath("//input[contains(@placeholder,'Name')]").click().send_keys('nancy')
        name =driver.find_element_by_id('name')
        name.click()
        name.send_keys('nancy')
        time.sleep(3)
        driver.find_element_by_xpath("//input[contains(@placeholder,'Email')]").click().send_keys('cainaisi@qq.com')
        driver.find_element_by_xpath("//input[contains(@placeholder,'phone')]").click().send_keys('0414660628')
        driver.find_element_by_xpath("//button[contains(@class,'btn')]").click()
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()