from selenium.webdriver.common.by import By

class LoginPage(object):
    
    def __init__(self, driver):
        
        self.driver = driver
        self.url = 'http://automationpractice.com/index.php?controller=authentication&back=my-account'
        self.selector_name_email_id = 'email'
        self.selector_name_password_id = 'passwd'
        self.login_button_id = 'SubmitLogin'
        self.create_account_email_selector_id = 'email_create'
        self.create_account_button_selector_id = 'SubmitCreate'
    
    def open(self):
        
        self.driver.get(self.url)
    
    def send_email(self, email):
        
        driver = self.driver
        driver.find_element(By.ID, self.selector_name_email_id).clear()
        driver.find_element(By.NAME, self.selector_name_email_id).send_keys(email)
    
    def send_password(self, password):
        
        driver = self.driver
        driver.find_element(By.ID, self.selector_name_password_id).clear()
        driver.find_element(By.ID, self.selector_name_password_id).send_keys(password)
    
    def click_login(self):
        
        driver = self.driver
        driver.find_element(By.ID, self.login_button_id).click()
        
    def create_account(self,email):
        self.driver.find_element(By.ID, self.create_account_email_selector_id).clear()
        self.driver.find_element(By.ID, self.create_account_email_selector_id).send_keys(email)
        
        self.driver.find_element(By.ID, self.create_account_button_selector_id).click()
        