from selenium import webdriver
from locators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(object):
    
    def __init__(self, driver):
        self._driver = driver
        self._url = 'https://www.phptravels.net/login'
        self.front_end_login_links_xpath = '//small[text()="http://www.phptravels.net/login"]'
    
    @property
    def is_loaded(self):
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.NAME, 'q')))
        return True
    
    @property
    def keyword(self):
        input_field = self._driver.find_element(By.NAME, 'q')
        return input_field.get_attribute('value')
    
    # Abre el explorador en la url indicada
    def open(self):
        self._driver.get(self._url)
        
    # Iniciar sesion como Customer Front-End
    def login_customer_fron_end(self):
        link = self._driver.find_elements(By.XPATH, self.front_end_login_links_xpath)
        link[0].click()
        
    # Iniciar sesion como Customer Front-End
    def login_agent_fron_end(self):
        self._driver.get('https://www.phptravels.net/login')
        link = self._driver.find_elements(By.XPATH, self.front_end_login_links_xpath)
        link[1].click()
    
    def enter_login_customer_front_end_credentials(self):
        
        self._driver.find_element(By.NAME, "email").send_keys(Locators.email_customer_front_end)
        self._driver.find_element(By.NAME, "password").send_keys(Locators.password_customer_front_end)
    
    def click_login_button(self):
        self._driver.find_element(By.XPATH, '//span[text()="Login"]').click()   
    
    # Encuentra la barra de buscar por su nombre y envía el valor recibido
    def type_search(self, keyword):
        input_field = self._driver.find_element(By.NAME, 'q')
        input_field.send_keys(keyword)
    
    # Encuentra la barra de busqueda y envía la busqueda
    def click_submit(self):
        input_field = self._driver.find_element(By.NAME, 'q')
        input_field.submit()

    # Método que realiza una busqueda
    def search(self, keyword):
        self.type_search(keyword)
        self.click_submit()