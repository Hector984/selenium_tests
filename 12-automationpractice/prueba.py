import unittest
import os
import time
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        
        driver = self.driver
        
        driver.find_element(By.LINK_TEXT, 'Sign in').click()
        driver.find_element(By.ID, 'email').clear()
        driver.find_element(By.ID, 'email').send_keys('hector@hector.com')
        
        driver.find_element(By.ID, 'passwd').clear()
        driver.find_element(By.ID, 'passwd').send_keys('12345678')
        
        driver.find_element(By.ID, 'SubmitLogin').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//a[text()="Women"]').click()
        driver.find_element(By.LINK_TEXT, 'Faded Short Sleeve T-shirts').click()
        
        driver.find_element(By.NAME, 'Submit').click()
        
        time.sleep(5)

        driver.find_element(By.XPATH, '//span[@title="Continue shopping"]').click()
        
        driver.find_element(By.XPATH, '//a[@title="View my shopping cart"]').click()
        time.sleep(5)
        driver.back()
        driver.back()        
        time.sleep(5)
    
        # //a[@title="Proceed to checkout"]
    
    
    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()
    
if __name__=="__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='reportes', report_name='report'))