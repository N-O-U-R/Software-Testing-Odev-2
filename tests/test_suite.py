import sys
import os
import unittest

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Odev2.settings')
import django
django.setup()

from accounts.tests.test_register import RegisterTests
from accounts.tests.test_login import LoginTests

def main_menu():
    print("Select Test Category:")
    print("1- Login Tests")
    print("2- Register Tests")
    choice = input("Enter choice: ")
    return choice

def run_tests():
    choice = main_menu()
    suite = unittest.TestSuite()
    if choice == '1':
        suite.addTests(unittest.TestLoader().loadTestsFromTestCase(LoginTests))
    elif choice == '2':
        suite.addTests(unittest.TestLoader().loadTestsFromTestCase(RegisterTests))
    else:
        print("Invalid choice")
        return

    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()
