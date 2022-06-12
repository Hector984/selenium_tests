import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pyunitreport import HTMLTestRunner

class Autocomplete(unittest.TestCase):
    
    def setUp(self):
        srv = Service(r'./chromedriver.exe')
        self.driver = webdriver.Chrome(service = srv)
        driver = self.driver
        driver.get('https://www.goibibo.com/')
        driver.maximize_window()
        driver.implicitly_wait(20)
        
    def test_autocomplete(self):
        driver = self.driver
        
        container = driver.find_element(By.CLASS_NAME, 'sc-iJKOTD').click()
        
        time.sleep(3)
        
        autocomplete = driver.find_element(By.XPATH, '//input[@type="text"]')
        autocomplete.send_keys("M")
        time.sleep(3)
        
        elements = driver.find_elements(By.CLASS_NAME, 'autoCompleteTitle')
        
        for item in elements:
            
            print(f'Suggestions are {item.text}')
            
            if(item.text.__contains__('Mysore')):
                print(f'Record found {item.text}')
                item.click()
                break
    
    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()
    
if __name__=="__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='reportes', report_name='report'))