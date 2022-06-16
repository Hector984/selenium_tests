from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import unittest
import time
from pyunitreport import HTMLTestRunner
from selenium.webdriver.common.by import By

class MultipleWindows(unittest.TestCase):
    
    def setUp(self):
        srv = Service(r'./chromedriver.exe')
        self.driver = webdriver.Chrome(service = srv)
        driver = self.driver
        driver.get('https://opensource-demo.orangehrmlive.com/')
        driver.maximize_window()
        
    
    def test_multiple_windows(self):
        driver = self.driver
        parent_window = driver.current_window_handle
        
        print(f"The parent window name is {parent_window}")
        driver.find_element(By.XPATH, '//img[@alt="LinkedIn OrangeHRM group"]').click()
        
        # Return to parent window to open facebook 
        driver.switch_to.window(parent_window)
        driver.find_element(By.XPATH, '//img[@alt="OrangeHRM on Facebook"]').click()
        
        # Return to parent window to opwn twitter
        driver.switch_to.window(parent_window)
        driver.find_element(By.XPATH, '//img[@alt="OrangeHRM on twitter"]').click()
        
        # This method returns a list with the source of the page
        # It stores the pages in the order that we clicked to the links
        # In this example the first element is linkedIn, the second one is Facebook
        # and the last is twitter
        child_windows = driver.window_handles
        
        print("Changing of window")
        driver.switch_to.window(child_windows[1])
        print(f"Title is {driver.title}")
        time.sleep(3)
        
        print("Changing of window")
        driver.switch_to.window(child_windows[2])
        print(f"Title is {driver.title}")
        time.sleep(3)
        
        print("Changing of window")
        driver.switch_to.window(child_windows[3])
        print(f"Title is {driver.title}")
        time.sleep(3)
        
        # for child in child_windows:
            
        #     print(child)
        #     if parent_window != child:
        #         print("Changing of window")
        #         driver.switch_to.window(child)
        #         print(f"Title is {driver.title}")
        #         print(child)
        #         driver.find_element(By.ID, 'email-address').send_keys('hectorqhector.com')
                
        #         Closes the current tab or window
        #         driver.close()
        
        driver.switch_to.window(parent_window)
        time.sleep(3)
        
    
    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()
    
if __name__=="__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='reportes', report_name='report'))
        
        