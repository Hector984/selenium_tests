from selenium.webdriver.common.by import By



class Cart(object):
    
    
    
    def __init__(self, driver):
        
        self.driver = driver
    
    
    # Add to cart
    def add_to_cart(self):
        self.driver.find_element(By.NAME, 'Submit').click()
    
    def continue_shopping(self):
        self.driver.find_element(By.XPATH, '//span[@title="Continue shopping"]').click()
    
    def view_shopping_cart(self):
        self.driver.find_element(By.XPATH, '//a[@title="View my shopping cart"]').click()
    