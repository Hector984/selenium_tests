from datetime import datetime
import unittest
import time
from selenium.webdriver.chrome.options import Options # Para tests en el background
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pyunitreport import HTMLTestRunner

class Alerts(unittest.TestCase):
    
    def setUp(self):
        # opt = Options()
        # opt.headless = True
        srv = Service(r'./chromedriver.exe')
        # self.driver = webdriver.Chrome(service = srv, chrome_options=opt)
        self.driver = webdriver.Chrome(service = srv)
        driver = self.driver
        driver.get('https://mail.rediff.com/cgi-bin/login.cgi')
        driver.maximize_window()
    
    def test_alerts(self):
        driver = self.driver
        
        submit_btn = driver.find_element(By.NAME, 'proceed').click()
        time.sleep(3)
        alert = driver.switch_to.alert
        print(f"{alert.text}")
        alert.accept()
    
        
        
    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()
    
if __name__=="__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='reportes', report_name='google-report'))