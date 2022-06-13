import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pyunitreport import HTMLTestRunner

class CalendarGoibibo(unittest.TestCase):
    
    def setUp(self):
        srv = Service(r'./chromedriver.exe')
        self.driver = webdriver.Chrome(service = srv)
        driver = self.driver
        driver.get('https://www.goibibo.com/')
        driver.maximize_window()
        driver.implicitly_wait(20)
        
    # First aproach
    def test_calendar_goibibo(self):
        driver = self.driver
        
        # Change the text according to the day
        input_calendar = driver.find_element(By.XPATH, '//p[text()="Monday"]').click()
        time.sleep(3)
        days_list = driver.find_elements(By.XPATH, '//div[@class="DayPicker-Body"]//div[@class="DayPicker-Day"]')
        time.sleep(3)
        
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