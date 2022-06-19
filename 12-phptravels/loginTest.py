import unittest
import os
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from loginPage import LoginPage


class LoginPage(unittest.TestCase):
    
    @classmethod
    def setUpClass(clc):
        ruta = os.path.abspath("../chromedriver.exe")
        srv = Service(ruta)
        clc.driver = webdriver.Chrome(service=srv)
        driver = clc.driver
        driver.maximize_window()
        driver.implicitly_wait(30)
    
    def test_login_customer_front_end(self):
        driver = self.driver
        login_user = LoginPage(driver)
        login_user.open()
        login_user.login_customer_fron_end()
        login_user.enter_login_customer_front_end_credentials()
        login_user.click_login_button()
        
        self.assertEqual('https://www.phptravels.net/account/dashboard', driver.current_url)
        
        
    @classmethod
    def tearDownClass(clc):
        clc.driver.implicitly_wait(3)
        clc.driver.quit()
    
if __name__=="__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='reportes', report_name='report'))