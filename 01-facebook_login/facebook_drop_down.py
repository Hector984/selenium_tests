import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pyunitreport import HTMLTestRunner
from selenium.webdriver.support.select import Select

class FacebookHome(unittest.TestCase):
    
    def setUp(self):
        srv = Service(r'./chromedriver.exe')
        self.driver = webdriver.Chrome(service = srv)
        driver = self.driver
        driver.get('https://es-la.facebook.com/')
        driver.maximize_window()
    
    def test_drop_down_button(self):
        driver = self.driver
        
        create_account_button = driver.find_element(By.XPATH, '//a[text()="Crear cuenta nueva"]')
        create_account_button.click()
        time.sleep(5)
        
        month = driver.find_element(By.ID, 'month')
        
        month_drop_down = Select(month)
        # For these three methods the priority is:
        # select_by_visible_text
        # select_by_value
        # select_by_index
        
        month_drop_down.select_by_index(3)
        time.sleep(3)
        
        month_drop_down.select_by_value("6")
        time.sleep(3)
        
        # This method is case sensitive
        month_drop_down.select_by_visible_text("ago")
        
    def test_first_option_is_jun(self):
        driver = self.driver
        create_account_btn = driver.find_element(By.XPATH, '//a[text()="Crear cuenta nueva"]').click()
        time.sleep(5)
        
        month = driver.find_element(By.ID, 'month')
        
        
        month_drop_down = Select(month)
        
        # Checking what is the first option in the select tag
        default_month = month_drop_down.first_selected_option.text
        
        self.assertEqual('jun', default_month)
    
    def test_count_elements_in_drop_down(self):
        driver = self.driver
        create_account_btn = driver.find_element(By.XPATH, '//a[text()="Crear cuenta nueva"]').click()
        time.sleep(5)
        
        month = driver.find_element(By.ID, 'month')
        
        month_drop_down = Select(month)
        
        dd_list = month_drop_down.options #This method returns an array with the options
        
        print(f"There are {len(dd_list)} options in this drop down button")
        
        self.assertEqual(12, len(dd_list))
        
        for item in dd_list:
            print(f"Value is {item.text}") 
            
            if item.text == "nov":
                item.click()
                break
        
        
        
    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()
    
if __name__=="__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='reportes', report_name='google-report'))