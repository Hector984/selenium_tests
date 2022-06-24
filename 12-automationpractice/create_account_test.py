import unittest
import os
import time
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Pages.create_account_page import CreateAccountPage
from Pages.index_page import IndexPage
from Pages.login_page import LoginPage
from variables import Variables

class CreateAccountTest(unittest.TestCase):
    
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
        create_account = CreateAccountPage(driver)
        index_page = IndexPage(driver)
        login_page = LoginPage(driver)
        variables = Variables()
        
        # Open the page and click in sign in button
        index_page.open()
        index_page.sign_in()
        
        # Create account email
        login_page.create_account('hector@hector.com')
        
        # Create account form
        create_account.gender('Mr.')
        create_account.first_name('hector')
        create_account.last_name('gómez')
        create_account.password('12345678')
        create_account.date_of_birth('12', variables.Agosto, '1990')
        
        create_account.first_name_address('galaxia')
        create_account.last_name_address('orion')
        create_account.company('KoKo store')
        create_account.address('Cuautitlan, Mexico')
        create_account.city("Mexico")
        create_account.state(variables.California)
        create_account.zip_code('54840')
        time.sleep(2)
        create_account.country(variables.United_States)
        time.sleep(2)
        # Optional 
        # create_account.additional_info('Nothing to say')
        # create_account.home_phone('5512345678')
        
        create_account.mobile_phone('5512345678')
        create_account.address_alias('koko')
        # create_account.register()
        
        time.sleep(5)
        
        # self.assertEqual('https://www.phptravels.net/account/dashboard', driver.current_url)
        
    @classmethod
    def tearDownClass(clc):
        clc.driver.implicitly_wait(3)
        clc.driver.quit()
    
if __name__=="__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='reportes', report_name='report'))