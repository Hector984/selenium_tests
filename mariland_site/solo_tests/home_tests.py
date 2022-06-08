import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

class HomeTest(unittest.TestCase):
    
    
    def setUp(self):
        s = Service(r'./chromedriver.exe')
        self.driver = webdriver.Chrome(service=s)
        driver = self.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        driver.implicitly_wait(30)
    
    def test_navbar(self):
       driver = self.driver
       women = driver.find_element(By.CSS_SELECTOR, '#nav > ol > li.level0.nav-1.first.parent > a')
       
       # Hover on an element
       action = ActionChains(driver) 
       action.move_to_element(women).perform()
       
       texto = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'New Arrivals'))).text
       
       self.assertEqual('New Arrivals', texto)
       
       driver.find_element(By.XPATH, '//a[text()="New Arrivals"]').click()
       
       self.assertEqual(driver.current_url, 'http://demo-store.seleniumacademy.com/women/new-arrivals.html')
       
       # Click to inspect tori tank
       driver.find_element(By.CLASS_NAME, 'product-name').click()
       
       self.assertEqual(driver.current_url, 'http://demo-store.seleniumacademy.com/women/new-arrivals/tori-tank-460.html')
    
    # def test_create_new_user(self):
        
    #     driver = self.driver
        
    #     driver.find_element(By.XPATH, '//*[@id="header"]/div/div[2]/div/a/span[2]').click()
    #     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[text()="Register"]')))
        
    #     driver.find_element(By.XPATH, '//a[text()="Register"]').click()
        
    #     # Fill register form
    #     firstname = driver.find_element(By.ID, 'firstname')
    #     firstname.send_keys('Hector')
        
    #     middlename = driver.find_element(By.ID, 'middlename')
    #     middlename.send_keys('Antonio')
        
    #     lastname = driver.find_element(By.ID, 'lastname')
    #     lastname.send_keys('Jimenez')
        
    #     email_address = driver.find_element(By.ID, 'email_address')
    #     email_address.send_keys('hector4@hector.com')
        
    #     password = driver.find_element(By.ID, 'password')
    #     password.send_keys('12345678')
        
    #     confirmation = driver.find_element(By.ID, 'confirmation')
    #     confirmation.send_keys('12345678')
        
    #     driver.find_element(By.XPATH, '//*[@id="form-validate"]/div[2]/button/span/span').click()
        
    #     self.assertEqual(driver.current_url, 'http://demo-store.seleniumacademy.com/customer/account/index/')
        
    #     text = driver.find_element(By.CLASS_NAME, 'welcome-msg').text
        
    #     self.assertEqual(text, 'WELCOME, HECTOR ANTONIO JIMENEZ!')
    
    def test_create_new_user_with_existent_credentials(self):
        
        driver = self.driver
        
        driver.find_element(By.XPATH, '//*[@id="header"]/div/div[2]/div/a/span[2]').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[text()="Register"]')))
        
        driver.find_element(By.XPATH, '//a[text()="Register"]').click()
        
        # Fill register form
        firstname = driver.find_element(By.ID, 'firstname')
        firstname.send_keys('Hector')
        
        middlename = driver.find_element(By.ID, 'middlename')
        middlename.send_keys('Antonio')
        
        lastname = driver.find_element(By.ID, 'lastname')
        lastname.send_keys('Jimenez')
        
        email_address = driver.find_element(By.ID, 'email_address')
        email_address.send_keys('hector@hector.com')
        
        password = driver.find_element(By.ID, 'password')
        password.send_keys('12345678')
        
        confirmation = driver.find_element(By.ID, 'confirmation')
        confirmation.send_keys('12345678')
        
        driver.find_element(By.XPATH, '//*[@id="form-validate"]/div[2]/button/span/span').click()
        
        text = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/ul/li/ul/li/span'))).text
        
        msg = 'There is already an account with this email address. If you are sure that it is your email address, click here to get your password and access your account.'
        
        self.assertEqual(text, msg)
        
       
    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()
    
if __name__=="__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='reportes', report_name='google-report'))