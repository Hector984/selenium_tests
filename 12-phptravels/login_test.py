import unittest
import os
import time
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Pages.login_page import LoginPage
from Pages.dashboard_page import DashboardPage
from credentials import Credentials

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
        credentials = Credentials()
        login_user = LoginPage(driver)
        login_user.open()
        login_user.send_email(credentials.email_customer_front_end)
        login_user.send_password(credentials.password_customer_front_end)
        login_user.click_login()
        
        time.sleep(5)
        
        dashboard = DashboardPage(driver)
        dashboard.logout()
        
        self.assertEqual('https://www.phptravels.net/account/dashboard', driver.current_url)
        
    @classmethod
    def tearDownClass(clc):
        clc.driver.implicitly_wait(3)
        clc.driver.quit()
    
if __name__=="__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='reportes', report_name='report'))