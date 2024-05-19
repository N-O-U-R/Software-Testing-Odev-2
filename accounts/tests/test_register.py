import unittest
import os
import django
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.test import Client
import sys
project_path = "../../"
sys.path.insert(0, project_path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'Odev2.settings'

if not django.apps.apps.ready:
    django.setup()

from django.contrib.auth.models import User

class RegisterTests(unittest.TestCase):

    def setUp(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        chromedriver_path = os.path.join(base_dir, '../../chromedriver-win64/chromedriver.exe')
        s = Service(chromedriver_path)
        self.driver = webdriver.Chrome(service=s)
        self.driver.get("http://localhost:3000")
        self.wait = WebDriverWait(self.driver, 10)
        self.client = Client()

    def tearDown(self):
        User.objects.filter(email="john.doe@example.com").delete()
        self.driver.quit()

    def test_register_valid(self):
        driver = self.driver
        driver.find_element(By.CLASS_NAME, "open-login-popup").click()
        self.wait.until(EC.visibility_of_element_located((By.ID, "login-popup")))
        
        register_button = self.wait.until(EC.element_to_be_clickable((By.ID, "go-register")))
        register_button.click()
        self.wait.until(EC.visibility_of_element_located((By.ID, "register-popup")))

        fname_input = self.wait.until(EC.element_to_be_clickable((By.NAME, "fname")))
        fname_input.clear()
        fname_input.send_keys("John Doe")
        
        email_input = self.wait.until(EC.element_to_be_clickable((By.NAME, "email")))
        email_input.clear()
        email_input.send_keys("john.doe@example.com")
        
        password_input = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='register-popup']/div/form/div[3]/input")))
        password_input.clear()
        password_input.send_keys("securepassword")

        submit_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='register-popup']/div/form/button")))
        submit_button.click()
        sleep(1)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/header/nav/div/div[1]/ul/li[2]/ul/li[2]/form/button")))
        logout_button = driver.find_element(By.XPATH, "/html/body/div/header/nav/div/div[1]/ul/li[2]/ul/li[2]/form/button")
        self.assertIsNotNone(logout_button)

        user_exists = User.objects.filter(email="john.doe@example.com").exists()
        self.assertTrue(user_exists)

    def test_register_existing_email(self):
        # Clean up any existing user with the same username or email before the test
        User.objects.filter(username='existing_user').delete()

        # Now create the user safely without running into a duplicate key error
        User.objects.create_user(username='existing_user', email='existing.email@example.com', password='password123')

        driver = self.driver
        driver.find_element(By.CLASS_NAME, "open-login-popup").click()
        self.wait.until(EC.visibility_of_element_located((By.ID, "login-popup")))
        
        register_button = self.wait.until(EC.element_to_be_clickable((By.ID, "go-register")))
        register_button.click()
        self.wait.until(EC.visibility_of_element_located((By.ID, "register-popup")))
        
        fname_input = self.wait.until(EC.element_to_be_clickable((By.NAME, "fname")))
        fname_input.clear()
        fname_input.send_keys("Test User")

        email_input = self.wait.until(EC.element_to_be_clickable((By.NAME, "email")))
        email_input.clear()
        email_input.send_keys("existing.email@example.com")

        password_input = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='register-popup']/div/form/div[3]/input")))
        password_input.clear()
        password_input.send_keys("qpalzm")

        submit_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='register-popup']/div/form/button")))
        submit_button.click()
        sleep(1)
        
        driver.find_element(By.CLASS_NAME, "open-login-popup").click()
        self.wait.until(EC.visibility_of_element_located((By.ID, "login-popup")))
        
        register_button = self.wait.until(EC.element_to_be_clickable((By.ID, "go-register")))
        register_button.click()
        self.wait.until(EC.visibility_of_element_located((By.ID, "register-popup")))
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='register-popup']/div/form/p[2]")))
        error_message = driver.find_element(By.XPATH, "//*[@id='register-popup']/div/form/p[2]")
        self.assertTrue("Email already exists" , error_message.text)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(RegisterTests('test_register_valid'))
    suite.addTest(RegisterTests('test_register_existing_email'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
