import unittest
import os
import time
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

class Keyboard(unittest.TestCase):
    
    def setUp(self):
        ruta = os.path.abspath("../chromedriver.exe")
        srv = Service(ruta)
        self.driver = webdriver.Chrome(service=srv)
        driver = self.driver
        driver.get('https://es-la.facebook.com/')
        driver.maximize_window()
        driver.implicitly_wait(30)
    
    def test_doubleclick(self):
        
        driver = self.driver
        driver.find_element(By.ID, 'email').send_keys("Hector")
        chain = ActionChains(driver)
        
        # Select the text
        chain.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL)
        
        # Copy the text
        chain.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL)
    
        # Press tab 
        chain.key_down(Keys.TAB).key_up(Keys.TAB)
        
        # Paste the text
        chain.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL)
        
        # Press enter key
        chain.send_keys(Keys.ENTER).perform()
        
        
    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()
    
if __name__=="__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='reportes', report_name='report'))