from selenium.webdriver.common.by import By

class HomePage(object):
    
    def __init__(self, driver):
        
        self.driver = driver
        
        self.welcome_id = 'welcome'
        self.logout_link_text = 'Logout'
    
    
    def logout(self):
        self.driver.find_element(By.ID, self.welcome_id).click()
        self.driver.find_element(By.LINK_TEXT, self.logout_link_text).click()