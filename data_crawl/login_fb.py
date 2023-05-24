from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from os import getenv
from dotenv import load_dotenv

load_dotenv()

def login(browser):
    browser.get("https://www.facebook.com/")

    txtUser = browser.find_element(By.ID, "email")
    txtUser.send_keys(getenv('email'))

    txtPass = browser.find_element(By.ID, "pass")
    txtPass.send_keys(getenv('pass'))

    txtPass.send_keys(Keys.ENTER)
