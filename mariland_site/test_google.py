import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from google_page import GooglePage

class GoogleTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(clc):
        clc.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        driver = clc.driver
        #driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        driver.implicitly_wait(30)
    
    def test_search(self):
        google = GooglePage(self.driver)
        google.open()
        google.search('earrings')
        
        # self.assertEqual('Platzi', google.keyword)
        
        
    @classmethod
    def tearDownClass(clc):
        clc.driver.implicitly_wait(3)
        clc.driver.quit()
    
if __name__=="__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='reportes', report_name='google-report'))