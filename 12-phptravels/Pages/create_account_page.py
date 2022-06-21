from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CreateAccountPage(object):
    
    
    def __init__(self,driver):
        
        self.driver = driver
        
        self.mr_gender_selector_id = 'uniform-id_gender1'
        self.mrs_gender_selector_id = 'uniform-id_gender2'
        self.first_name_selector_id = 'customer_firstname'
        self.last_name_selector_id = 'customer_lastname'
        self.password_selector_id = 'passwd'
        
        self.day_selector_id = 'days'
        self.month_selector_id = 'months'
        self.year_selector_id = 'years'
        
        self.newsletter_selector_id = 'newsletter'
        self.special_offers_selector_id = 'optin'
        
        self.address_first_name_selector_id = 'firstname'
        self.address_last_name_selector_id = 'lastname'
        self.address_company_selector_id = 'company'
        self.address_selector_id = 'address1'
        self.address_line_two_selector_id = 'address2'
        self.city_selector_id = 'city'
        self.state_selector_id = 'id_state'
        self.zip_code_selector_id = 'postcode'
        self.country_selector_id = 'id_country'
        self.additional_info_selector_id = 'other'
        self.home_phone_selector_id = 'phone'
        self.mobile_phone_selector_id = 'phone_mobile'
        self.address_alias_selector_id = 'alias'
        self.register_button_selector_id = 'submitAccount'
    
    def gender(self, gender):
        
        driver = self.driver
        if(gender == 'Mr.'):
            
            driver.find_element(By.ID, self.mr_gender_selector_id).click()
                
        else:
            
            driver.find_element(By.ID, self.mrs_gender_selector_id).click()
    
    def first_name(self, first_name):
        
        self.driver.find_element(By.ID, self.first_name_selector_id).clear()
        self.driver.find_element(By.ID, self.first_name_selector_id).send_keys(first_name)
    
    def last_name(self, last_name):
        
        self.driver.find_element(By.ID, self.last_name_selector_id).clear()
        self.driver.find_element(By.ID, self.last_name_selector_id).send_keys(last_name)
    
    def password(self, password):
        
        self.driver.find_element(By.ID, self.password_selector_id).clear()
        self.driver.find_element(By.ID, self.password_selector_id).send_keys(password)
    
    def date_of_birth(self, day, month, year):
        
        day_selector = self.driver.find_element(By.ID, self.day_selector_id)
        day_dropdown = Select(day_selector)
        day_dropdown.select_by_visible_text(day)
        
        month_selector = self.driver.find_element(By.ID, self.month_selector_id)
        month_dropdown = Select(month_selector)
        month_dropdown.select_by_visible_text(month)
        
        year_selector = self.driver.find_element(By.ID, self.year_selector_id)
        year_dropdown = Select(year_selector)
        year_dropdown.select_by_visible_text(year)
    
    def newsletter(self):
        
        self.driver.find_element(By.ID, self.newsletter_selector_id).click()
        
    def special_offers(self):
        
        self.driver.find_element(By.ID, self.special_offers_selector_id).click()
    
    # Address methods
    def first_name_address(self, first_name):
        self.driver.find_element(By.ID, self.address_first_name_selector_id).clear()
        self.driver.find_element(By.ID, self.address_first_name_selector_id).send_keys(first_name)
        
    def last_name_address(self, last_name):
        self.driver.find_element(By.ID, self.address_last_name_selector_id).clear()
        self.driver.find_element(By.ID, self.address_last_name_selector_id).send_keys(last_name)
        
    def company(self, company):
        self.driver.find_element(By.ID, self.address_company_selector_id).clear()
        self.driver.find_element(By.ID, self.address_company_selector_id).send_keys(company)
    
    def address(self, address):
        self.driver.find_element(By.ID, self.address_selector_id).clear()
        self.driver.find_element(By.ID, self.address_selector_id).send_keys(address)
    
    def addressLineTwo(self, address):
        self.driver.find_element(By.ID, self.address_line_two_selector_id).clear()
        self.driver.find_element(By.ID, self.address_line_two_selector_id).send_keys(address)
    
    def city(self, city):
        self.driver.find_element(By.ID, self.city_selector_id).clear()
        self.driver.find_element(By.ID, self.city_selector_id).send_keys(city)
    
    def state(self, state):
        state_selector = self.driver.find_element(By.ID, self.state_selector_id)
        state_dropdown = Select(state_selector)
        state_dropdown.deselect_by_visible_text(state)
    
    def zip_code(self, zip_code):
        self.driver.find_element(By.ID, self.zip_code_selector_id).clear()
        self.driver.find_element(By.ID, self.zip_code_selector_id).send_keys(zip_code)
    
    def country(self, country):
        country_selector = self.driver.find_element(By.ID, self.country_selector_id)
        country_dropdown = Select(country_selector)
        country_dropdown.deselect_by_visible_text(country)
    
    def additional_info(self, text):
        self.driver.find_element(By.ID, self.additional_info_selector_id).clear()
        self.driver.find_element(By.ID, self.additional_info_selector_id).send_keys(text)
    
    def home_phone(self, phone):
        self.driver.find_element(By.ID, self.home_phone_selector_id).clear()
        self.driver.find_element(By.ID, self.home_phone_selector_id).send_keys(phone)
        
    def mobile_phone(self, phone):
        self.driver.find_element(By.ID, self.mobile_phone_selector_id).clear()
        self.driver.find_element(By.ID, self.mobile_phone_selector_id).send_keys(phone)
    
    def address_alias(self, address):
        self.driver.find_element(By.ID, self.address_alias_selector_id).clear()
        self.driver.find_element(By.ID, self.address_alias_selector_id).send_keys(address)
    
    def register(self):
        self.driver.find_element(By.ID, self.register_button_selector_id).click()
        