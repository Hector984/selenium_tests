from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import unittest
from pyunitreport import HTMLTestRunner
from selenium.webdriver.common.by import By

class HomeTest(unittest.TestCase):
    
    def setUp(self):
        srv = Service(r'./chromedriver.exe')
        self.driver = webdriver.Chrome(service = srv)
        driver = self.driver
        driver.get('https://opensource-demo.orangehrmlive.com/')
        driver.maximize_window()
        
    
    
    
    
    
    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()
    
if __name__=="__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='reportes', report_name='google-report'))
        
        