import unittest
import os
import time
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Pages.index_page import IndexPage
from Pages.login_page import LoginPage
from Pages.woman_page import WomanPage
from cart_actions import Cart
from locators import Locators
from variables import Variables



class WomenPageTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(clc):
        ruta = os.path.abspath("../chromedriver.exe")
        srv = Service(ruta)
        clc.driver = webdriver.Chrome(service=srv)
        driver = clc.driver
        driver.maximize_window()
        driver.implicitly_wait(30)
    
    def test_women_page(self):
        driver = self.driver
        login_user = LoginPage(driver)
        cart = Cart(driver)
        locator = Locators()
        women = WomanPage(driver)
        login_user.open()
        
        # Log in
        login_user.send_email('hector@hector.com')
        login_user.send_password('12345678')
        login_user.click_login()
        
        # Go to women page
        women.women_page()
        
        # Select item and add to cart
        women.select_item(locator.FADED_SHORT)
        time.sleep(3)
        cart.add_to_cart()
        time.sleep(2)
        cart.continue_shopping()
        cart.view_shopping_cart()
        time.sleep(2) 
        women.women_page()
        
        time.sleep(5)
    
    def test_sort_by(self):
        driver = self.driver
        index = IndexPage(driver)
        women = WomanPage(driver)
        variables = Variables()
        index.open()
        
        women.women_page()
        index.sort_by(variables.lowest_first)
        time.sleep(5)
        
        
    @classmethod
    def tearDownClass(clc):
        clc.driver.implicitly_wait(3)
        clc.driver.quit()
    
if __name__=="__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='reportes', report_name='report'))