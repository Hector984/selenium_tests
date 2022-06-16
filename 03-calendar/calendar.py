import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pyunitreport import HTMLTestRunner

class Calendar(unittest.TestCase):
    
    def setUp(self):
        srv = Service(r'./chromedriver.exe')
        self.driver = webdriver.Chrome(service = srv)
        driver = self.driver
        driver.get('https://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html')
        driver.maximize_window()
        driver.implicitly_wait(20)
        
    # First aproach
    def test_calendar(self):
        driver = self.driver
        
        input_calendar = driver.find_element(By.ID, 'datepicker').click()
        time.sleep(3)
        day = driver.find_element(By.XPATH, '//a[text()="14"]').click()
        time.sleep(3)
    
    # Second aproach
    def test_calendar_by_selecting_calendar_table(self):
        driver = self.driver
        
        input_calendar = driver.find_element(By.ID, 'datepicker').click()
        time.sleep(3)
        # List of web elements
        days_list = driver.find_elements(By.XPATH, '//table[@class="ui-datepicker-calendar"]//a')
        
        for day in days_list:
            
            # Web element
            date = day.text
            
            if(date == '25'):
                day.click()
                time.sleep(3)
                break
        
    
    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()
    
if __name__=="__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='reportes', report_name='report'))