import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from home_page import HomePage

class HomeTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(clc):
        clc.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        driver = clc.driver
        #driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        driver.implicitly_wait(30)
    
    def test_search(self):
        google = HomePage(self.driver)
        google.open()
        google.search('earrings')
        
        print(google.keyword)
        # self.assertEqual('Platzi', google.keyword)
        
        
    @classmethod
    def tearDownClass(clc):
        clc.driver.implicitly_wait(3)
        clc.driver.quit()
    
if __name__=="__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='reportes', report_name='google-report'))