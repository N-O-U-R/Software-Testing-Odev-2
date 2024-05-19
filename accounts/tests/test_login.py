import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import django
from time import sleep

os.environ['DJANGO_SETTINGS_MODULE'] = 'Odev2.settings'
django.setup()

class LoginTests(unittest.TestCase):

    def setUp(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        chromedriver_path = os.path.join(base_dir, '../../chromedriver-win64/chromedriver.exe')
        s = Service(chromedriver_path)
        self.driver = webdriver.Chrome(service=s)
        self.driver.get("http://localhost:3000")
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()

    def test_login_valid(self):
        driver = self.driver
        driver.find_element(By.CLASS_NAME, "open-login-popup").click()
        self.wait.until(EC.visibility_of_element_located((By.ID, "login-popup")))
        username_input = self.wait.until(EC.element_to_be_clickable((By.NAME, "username")))
        username_input.clear()  # Clear any pre-filled text
        username_input.send_keys("test@test.com")
        
        password_input = self.wait.until(EC.element_to_be_clickable((By.NAME, "password")))
        password_input.clear()  # Clear any pre-filled text
        password_input.send_keys("qpalzm")
        
        submit_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='login-popup']/div/form/button")))
        submit_button.click()
        sleep(1)
        logout_button = driver.find_element(By.XPATH, "/html/body/div/header/nav/div/div[1]/ul/li[2]/ul/li[2]/form/button")
        self.assertIsNotNone(logout_button)

    def test_login_invalid(self):
        driver = self.driver
        driver.find_element(By.CLASS_NAME, "open-login-popup").click()
        self.wait.until(EC.visibility_of_element_located((By.ID, "login-popup")))
        
        username_input = self.wait.until(EC.element_to_be_clickable((By.NAME, "username")))
        username_input.clear()  # Clear any pre-filled text
        username_input.send_keys("invalid_user")
        
        password_input = self.wait.until(EC.element_to_be_clickable((By.NAME, "password")))
        password_input.clear()  # Clear any pre-filled text
        password_input.send_keys("invalid_password")
        
        submit_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='login-popup']/div/form/button")))
        submit_button.click()
        
        driver.find_element(By.CLASS_NAME, "open-login-popup").click()
        self.wait.until(EC.visibility_of_element_located((By.ID, "login-popup")))
        
        error_message = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='login-popup']/div/form/p[2]")))
        self.assertEqual("Invalid login credentials", error_message.text)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(LoginTests('test_login_valid'))
    suite.addTest(LoginTests('test_login_invalid'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
