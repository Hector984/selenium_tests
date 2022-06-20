from selenium.webdriver.common.by import By

class LoginPage(object):
    
    def __init__(self, driver):
        
        self.driver = driver
        self.url = 'https://www.phptravels.net/login'
        self.selector_name_email = 'email'
        self.selector_name_password = 'password'
        self.login_button = '//span[text()="Login"]'
    
    def open(self):
        
        self.driver.get(self.url)
    
    def send_email(self, email):
        
        driver = self.driver
        driver.find_element(By.NAME, self.selector_name_email).clear()
        driver.find_element(By.NAME, self.selector_name_email).send_keys(email)
    
    def send_password(self, password):
        
        driver = self.driver
        driver.find_element(By.NAME, self.selector_name_password).clear()
        driver.find_element(By.NAME, self.selector_name_password).send_keys(password)
    
    def click_login(self):
        
        driver = self.driver
        driver.find_element(By.XPATH, self.login_button).click()
        