from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select 

class IndexPage(object):
    
    
    def __init__(self,driver):
        
        self.driver = driver
        self.url = 'http://automationpractice.com/index.php'
        self.sign_in_selector_class = 'login'
        self.sort_By_selector_id = 'selectProductSort'
        
    def open(self):
        
        self.driver.get(self.url)
        
    def sign_in(self):
        
        self.driver.find_element(By.CLASS_NAME, self.sign_in_selector_class).click()
    
    def sort_by(self, sort):
        
        driver = self.driver
        order_by_selector = driver.find_element(By.ID, self.sort_By_selector_id)
        drop_down = Select(order_by_selector)
        drop_down.select_by_visible_text(sort)