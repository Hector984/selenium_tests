import unittest
import os
import time
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Pages.login_page import LoginPage

class LoginTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(clc):
        ruta = os.path.abspath("../chromedriver.exe")
        srv = Service(ruta)
        clc.driver = webdriver.Chrome(service=srv)
        driver = clc.driver
        driver.maximize_window()
        driver.implicitly_wait(30)
    
    def test_login_user(self):
        driver = self.driver
        login_user = LoginPage(driver)
        login_user.open()
        login_user.send_email('hector@hector.com')
        login_user.send_password('12345678')
        login_user.click_login()
        
        time.sleep(5)
        
    @classmethod
    def tearDownClass(clc):
        clc.driver.implicitly_wait(3)
        clc.driver.quit()
    
if __name__=="__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='reportes', report_name='report'))