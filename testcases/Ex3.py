import time
from flask import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


service = Service(executable_path="C:\\swathi_online training\\JarFiles\\Chromedriver\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.google.com/")
driver.maximize_window()
print("hello world!")


