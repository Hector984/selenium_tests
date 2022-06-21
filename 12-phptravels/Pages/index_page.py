from selenium.webdriver.common.by import By


class IndexPage(object):
    
    
    def __init__(self,driver):
        
        self.driver = driver
        self.url = 'http://automationpractice.com/index.php'
        self.sign_in_selector_class = 'login'
        
    def sign_in(self):
        
        self.driver.find_element(By.CLASS_NAME, self.sign_in_selector_class).click()