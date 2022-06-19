import unittest
import time
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from Pages.login_page import LoginPage
from Pages.home_page import HomePage
from selenium.webdriver.chrome.service import Service

class LoginTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        srv = Service(r'../chromedriver.exe')
        cls.driver = webdriver.Chrome(service = srv)
        driver = cls.driver
        driver.maximize_window()
        driver.implicitly_wait(30)

    def test_login_user(self):
        driver = self.driver
        login = LoginPage(driver)
        login.open()
        
        login.enter_username('Admin')
        login.enter_password('admin123')
        login.click_login()
        
        time.sleep(5)
    
    def test_logout_user(self):
        
        driver = self.driver
        home = HomePage(driver)
        home.logout()
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.implicitly_wait(3)
        cls.driver.quit()
    
if __name__=="__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='reportes', report_name='report'))