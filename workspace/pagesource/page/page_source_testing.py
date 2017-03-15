'''
Created on Mar 15, 2017

@author: OA-User2
'''
import unittest
from selenium import webdriver


class Test(unittest.TestCase):


    def setUp(self):
        global driver
        driver=webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('http://www.openagent.com.au/')


    def tearDown(self):
        driver.quit()


    def testName(self):
        html_source = driver.page_source
  
        cano=self.assertTrue('<link rel="canonical"' in html_source)
        print cano
#         if cano:
#             print len('<link rel="canonical"' in html_source)
            


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()