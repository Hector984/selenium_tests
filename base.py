import unittest
import os
import time
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains

class DoubleClick(unittest.TestCase):
    
    def setUp(self):
        ruta = os.path.abspath("../chromedriver.exe")
        # print("Ruta del chrome.exe")
        # print(ruta)
        srv = Service(ruta)
        self.driver = webdriver.Chrome(service=srv)
        driver = self.driver
        driver.get('https://demos.telerik.com/kendo-ui/treeview/animation')
        driver.maximize_window()
        driver.implicitly_wait(30)
    
    def test_doubleclick(self):
        
        pass
    
    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()
    
if __name__=="__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='reportes', report_name='report'))