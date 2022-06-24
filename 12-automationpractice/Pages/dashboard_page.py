
from selenium.webdriver.common.by import By

class DashboardPage(object):
    
    def __init__(self, driver):
        
        self.driver = driver
        self.logout_selector_text = '//a[text()=" Logout"]'
        
        
    def logout(self):
        logout_link = self.driver.find_elements(By.XPATH, self.logout_selector_text)
        logout_link[1].click()
        
                    