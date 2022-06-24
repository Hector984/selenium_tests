from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains 

class WomanPage(object):
    
    
    def __init__(self, driver):
        
        self.driver = driver
        self.WOMEN_SELECTOR_XPATH = '//a[text()="Women"]'
        
        
    def women_page(self):
        
        self.driver.find_element(By.XPATH, self.WOMEN_SELECTOR_XPATH).click()
    
    def select_item(self, name):
         
        driver = self.driver
        driver.find_element(By.LINK_TEXT, name).click()
    
        
    