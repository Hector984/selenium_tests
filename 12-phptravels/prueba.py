import unittest
import os
import time
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains

class DoubleClick(unittest.TestCase):
    
    def setUp(self):
        ruta = os.path.abspath("../chromedriver.exe")
        srv = Service(ruta)
        self.driver = webdriver.Chrome(service=srv)
        driver = self.driver
        driver.get('https://phptravels.com/demo/')
        # driver.get('https://www.phptravels.net/login')
        driver.maximize_window()
        driver.implicitly_wait(30)
    
    def test_doubleclick(self):
        
        driver = self.driver
        anchor_elements = driver.find_elements(By.XPATH, '//small[text()="http://www.phptravels.net/login"]')
        
        anchor_elements[0].click()
        
        time.sleep(10)
        email = driver.find_element(By.XPATH, '//input[@name="email"]')
        email.send_keys('hector')
        
        time.sleep(8)
    
    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()
    
if __name__=="__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='reportes', report_name='report'))