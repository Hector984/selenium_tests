import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service 

class MouseHover(unittest.TestCase):
    
    def setUp(self):
        srv = Service(r'./chromedriver.exe')
        self.driver = webdriver.Chrome(service=srv)
        driver = self.driver
        driver.get('https://seleniumpractise.blogspot.com/2016/08/how-to-perform-mouse-hover-in-selenium.html')
        driver.maximize_window()
        driver.implicitly_wait(30)
    
    def test_mousehover(self):
        
        driver = self.driver
        button = driver.find_element(By.XPATH, '//button[text()="Automation Tools"]')
        chain = ActionChains(driver)
        
        # Not chaining methods
        # chain.move_to_element(button).perform()
        
        # driver.find_element(By.XPATH, '//a[text()="Appium"]').click()
        
        # Chaining actions
        chain.move_to_element(button).pause(3).click(driver.find_element(By.XPATH, '//a[text()="Appium"]')).perform()
        
    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()
    
if __name__=="__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='reportes', report_name='report'))