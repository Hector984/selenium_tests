from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GooglePage(object):
    
    def __init__(self, driver):
        self._driver = driver
        self._url = 'http://demo-store.seleniumacademy.com/'
        self.search_locator = 'search'
    
    @property
    def is_loaded(self):
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.ID, 'search')))
        return True
    
    @property
    def keyword(self):
        input_field = self._driver.find_element(By.ID, 'search')
        return input_field.get_attribute('value')
    
    # Abre el explorador en la url indicada
    def open(self):
        self._driver.get(self._url)
    
    # Encuentra la barra de buscar por su nombre y envía el valor recibido
    def type_search(self, keyword):
        input_field = self._driver.find_element(By.ID, 'search')
        input_field.send_keys(keyword)
    
    # Encuentra la barra de busqueda y envía la busqueda
    def click_submit(self):
        input_field = self._driver.find_element(By.ID, 'search')
        input_field.submit()

    # Método que realiza una busqueda
    def search(self, keyword):
        self.type_search(keyword)
        self.click_submit()