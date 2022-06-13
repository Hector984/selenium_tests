from datetime import datetime
import unittest
import time
from selenium.webdriver.chrome.options import Options # Para tests en el background
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pyunitreport import HTMLTestRunner

class Screenshot(unittest.TestCase):
    
    def setUp(self):
        opt = Options()
        opt.headless = True
        srv = Service(r'./chromedriver.exe')
        self.driver = webdriver.Chrome(service = srv, chrome_options=opt)
        driver = self.driver
        driver.get('https://google.com/')
        driver.maximize_window()
    
    def test_take_screenshot(self):
        driver = self.driver
        
        # If no specific path to save the file is given then is stored in the current directory
        driver.get_screenshot_as_file(f"google_{self.current_time()}.png")
        
    def current_time(self):
        return datetime.now().strftime("%H_%M_%S_%d_%m_%Y")
        
        
    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()
    
if __name__=="__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='reportes', report_name='google-report'))