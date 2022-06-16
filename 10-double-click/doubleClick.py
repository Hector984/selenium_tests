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
        
        driver = self.driver
        
        # Check if accpts cokies button is on the screen
        time.sleep(5)
        if len(driver.find_elements(By.XPATH, '//button[text()="Accept Cookies"]')) > 0 :
            
            driver.find_element(By.XPATH, '//button[text()="Accept Cookies"]').click()
        
        option = driver.find_element(By.XPATH, '//span[text()="Furniture"]')
        act = ActionChains(driver)
        
        act.double_click(option).perform()
        
        time.sleep(3)
        
        tables = driver.find_element(By.XPATH, '//span[text()="Tables & Chairs"]').text
        
        self.assertAlmostEqual('Tables & Chairs', tables)
    
    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()
    
if __name__=="__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='reportes', report_name='report'))