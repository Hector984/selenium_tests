from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import unittest
import time
from pyunitreport import HTMLTestRunner
from selenium.webdriver.common.by import By

class Frames(unittest.TestCase):
    
    def setUp(self):
        srv = Service(r'./chromedriver.exe')
        self.driver = webdriver.Chrome(service = srv)
        driver = self.driver
        driver.get('https://www.redbus.in/')
        driver.maximize_window()
        
    
    def test_multiple_windows(self):
        driver = self.driver
        signup_button = driver.find_element(By.XPATH, '//i[contains(@id,"profile")]').click()
        signup_link = driver.find_element(By.XPATH, '//li[contains(text(),"Sign In/Sign Up")]').click()
        
        driver.switch_to.frame(driver.find_element(By.XPATH, '//iframe[@class="modalIframe"]'))
        
        driver.find_element(By.ID, 'newFbId').click()
        
        # Switch to parent frame
        driver.switch_to.parent_frame()
    
    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()
    
if __name__=="__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='reportes', report_name='report'))
        
        