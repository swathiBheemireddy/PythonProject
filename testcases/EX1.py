import time
from flask import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

#driver = webdriver.Chrome(executable_path= "C:\\swathi_online training\\JarFiles\\Chromedriver\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")


#app=Flask(__name__)
#@app.route('/')
#def home():

#if __name__ == '__main__':
#option = webdriver.ChromeOptions()
#driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=option)
service = Service(executable_path="C:\\swathi_online training\\JarFiles\\Chromedriver\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.google.com/")
driver.maximize_window()
print("hello world!")
#driver.find_element(B)
    #return render_template('hello.html',n1='swathi',n2='venkat')
    #driver.sendkeys("hello world")
    #time.sleep(2000)
#driver.implicitly_wait()
# ...driver.quit()
