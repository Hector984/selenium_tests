from selenium.webdriver.common.by import By
import time

class LoginPage(object):
    
    def __init__(self, driver):
        
        self.driver = driver
        self.url = "https://opensource-demo.orangehrmlive.com/index.php/auth/login"
        self.username_text_box_id = 'txtUsername'
        self.password_text = 'txtPassword'
        self.login_btn = 'btnLogin'
    
    def open(self):
        self.driver.get(self.url)
    
    def enter_username(self, username):
        
        time.sleep(3)
        self.driver.find_element(By.ID, self.username_text_box_id).clear()
        self.driver.find_element(By.ID, self.username_text_box_id).send_keys(username)
    
    def enter_password(self, password):
        
        time.sleep(3)
        self.driver.find_element(By.ID, self.password_text).clear()
        self.driver.find_element(By.ID, self.password_text).send_keys(password)
        
    def click_login(self):
        
        self.driver.find_element(By.ID, self.login_btn).click()