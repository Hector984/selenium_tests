from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import unittest
from pyunitreport import HTMLTestRunner
from selenium.webdriver.common.by import By

class HomeTest(unittest.TestCase):
    
    def setUp(self):
        srv = Service(r'./chromedriver.exe')
        self.driver = webdriver.Chrome(service = srv)
        driver = self.driver
        driver.get('https://opensource-demo.orangehrmlive.com/')
        driver.maximize_window()
        
    
    def test_user_login(self):
        driver = self.driver
        user_input = driver.find_element(By.ID, 'txtUsername')
        
        enable_status = user_input.is_enabled()
        displayed_status = user_input.is_displayed()
        
        print(f'Enable {enable_status} and Displayed {displayed_status}')
        
        user_input.clear()
        attr_data = user_input.get_attribute('type')
        font_value = user_input.value_of_css_property('font-size')
        
        print(f'Attribute of the element {attr_data} and Property {font_value}')
        
        user_input.send_keys('Admin')
        
        password_input = driver.find_element(By.ID, 'txtPassword')
        
        password_input.clear()
        password_input.send_keys('admin123')
        
        btn_login = driver.find_element(By.ID, 'btnLogin').click()
        
    
        
    
    
    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()
    
if __name__=="__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='reportes', report_name='google-report'))
        
        