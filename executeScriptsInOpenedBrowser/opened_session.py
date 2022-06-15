import unittest
import time
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class OpenedSession(unittest.TestCase):
    
    def setUp(self):
        opt = Options();
        opt.add_experimental_option('debuggerAddress', 'localhost:8989')
        srv = Service(r'./chromedriver.exe')
        self.driver = webdriver.Chrome(service = srv, chrome_options=opt)
        driver = self.driver
        # driver.get('https://es-la.facebook.com/')
        driver.maximize_window()

    def test_user_registration(self):
        driver = self.driver
        input = driver.find_element(By.ID, 'email')
        input.clear()
        input.send_keys('hectoruam96@gmail.com')

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()
    
if __name__=="__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='reportes', report_name='report'))