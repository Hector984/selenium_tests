import unittest
import os
import time
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

class DoubleClick(unittest.TestCase):
    
    def setUp(self):
        ruta = os.path.abspath("../chromedriver.exe")
        srv = Service(ruta)
        self.driver = webdriver.Chrome(service=srv)
        driver = self.driver
        driver.get('http://automationpractice.com/index.php')
        driver.maximize_window()
        driver.implicitly_wait(30)
    
    def test_doubleclick(self):
        
        self.driver.find_element(By.CLASS_NAME, 'login').click()
        
        self.driver.find_element(By.ID, 'email_create').clear()
        self.driver.find_element(By.ID, 'email_create').send_keys('hector1@hector.com')
        
        self.driver.find_element(By.ID, 'SubmitCreate').click()
        
        self.driver.find_element(By.ID, 'days').click()
        day_selector = self.driver.find_element(By.ID, 'days')
        day_dropdown = Select(day_selector)
        day_dropdown.select_by_value('12')
    
    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()
    
if __name__=="__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='reportes', report_name='report'))