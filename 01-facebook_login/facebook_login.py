import unittest
import time
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

class FacebookRegistration(unittest.TestCase):
    
    def setUp(self):
        srv = Service(r'./chromedriver.exe')
        self.driver = webdriver.Chrome(service = srv)
        driver = self.driver
        driver.get('https://es-la.facebook.com/')
        driver.maximize_window()

    def test_user_registration(self):
        driver = self.driver
        create_account_btn = driver.find_element(By.XPATH, '//a[text()="Crear cuenta nueva"]').click()
        time.sleep(5)
        
        # Nombre
        firstname = driver.find_element(By.NAME, 'firstname')
        firstname.send_keys('Jose')
        
        # Apellido
        lastname = driver.find_element(By.NAME, 'lastname')
        lastname.send_keys('Orijuela')
        
        # Tel. o email
        tel_or_email = driver.find_element(By.NAME, 'reg_email__')
        tel_or_email.send_keys('jose@gmail.com')
        
        # Wait to see the email confirmation
        time.sleep(4)
        
        # Email confirmation
        email_confirm = driver.find_element(By.NAME, 'reg_email_confirmation__')
        email_confirm.send_keys('jose@gmail.com')
        
        # Contraseña
        password = driver.find_element(By.ID, 'password_step_input')
        password.send_keys('#practicandoselenium')
        
        # Día
        dia = driver.find_element(By.ID, 'day')
        
        dia_drop_down = Select(dia)
        dia_drop_down.select_by_visible_text('21')
        
        # Mes
        mes = driver.find_element(By.ID, 'month')
        mes_drop_down = Select(mes)
        
        mes_drop_down.select_by_visible_text('ago')
        
        # Año
        anio = driver.find_element(By.ID, 'year')
        anio_drop_down = Select(anio)
        anio_drop_down.select_by_visible_text('1998')
        
        # Sexo
        sexo = driver.find_element(By.XPATH, '//input[@value="2"]').click()
        
        time.sleep(3)
        # Submit button
        # register_button = driver.find_element(By.XPATH, '//button[@name="websubmit"]').click()
        # time.sleep(15)

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()
    
if __name__=="__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='reportes', report_name='google-report'))