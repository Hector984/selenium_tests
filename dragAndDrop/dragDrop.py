import unittest
import time
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class DragDrop(unittest.TestCase):
    
    def setUp(self):
        srv = Service(r'./chromedriver.exe')
        self.driver = webdriver.Chrome(service = srv)
        driver = self.driver
        driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
        driver.maximize_window()

    def test_drag_and_drop(self):
        driver = self.driver
        
        # Oslo-Noruega
        oslo = driver.find_element(By.ID, 'box1')
        noruega = driver.find_element(By.ID, 'box101')
        action = ActionChains(driver)
        action.drag_and_drop(oslo, noruega)
        
        # Estocolmo-Suecia
        estocolmo = driver.find_element(By.ID, 'box2')
        suecia = driver.find_element(By.ID, 'box102')
        action.drag_and_drop(estocolmo, suecia)
        
        # Washington-USA
        washington = driver.find_element(By.ID, 'box3')
        usa = driver.find_element(By.ID, 'box103')
        action.drag_and_drop(washington, usa)
        
        # Copenague-Dinamarca
        copenague = driver.find_element(By.ID, 'box4')
        dinamarca = driver.find_element(By.ID, 'box104')
        action.drag_and_drop(copenague, dinamarca)
        
        # Seul-Corea del sur
        seul = driver.find_element(By.ID, 'box5')
        corea = driver.find_element(By.ID, 'box105')
        action.drag_and_drop(seul, corea)
        
        # Roma-Italia
        roma = driver.find_element(By.ID, 'box6')
        italia = driver.find_element(By.ID, 'box106')
        action.drag_and_drop(roma, italia)
        
        # España-Madrid
        madrid = driver.find_element(By.ID, 'box7')
        espana = driver.find_element(By.ID, 'box107')
        action.drag_and_drop(madrid,espana)
        
        action.perform()
        
        time.sleep(3)
        

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()
    
if __name__=="__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='reportes', report_name='report'))