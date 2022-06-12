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
        driver.get('http://seleniumpractise.blogspot.com/2016/08/how-to-handle-autocomplete-feature-in.html')
        driver.maximize_window()
        driver.implicitly_wait(20)
        
    def test_autocomplete(self):
        driver = self.driver
        
        autocomplete = driver.find_element(By.ID, 'tags')
        autocomplete.send_keys("S")
        time.sleep(3)
        
        elements = driver.find_elements(By.XPATH, '//li[@class="ui-menu-item"]//div')
        
        for item in elements:
            
            print(f'Suggestions are {item.text}')
            
            if(item.text == "Selenium"):
                print(f'Record found {item.text}')
                item.click()
                break
    
    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()
    
if __name__=="__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='reportes', report_name='report'))