from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.chrome.options import Options
import os

# Set up the ChromeDriver service and options
service = Service(executable_path="C:\\swathi_online training\\JarFiles\\Chromedriver\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# Define your variables
n1 = "Hello Swathi"
n2 = "Welcome to new world"

# Create the HTML content
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body> 
<p> {n1} <br> </p>
<p> {n2} <br> </p>
</body>
</html>
""".format(n1=n1, n2=n2)

# Write the HTML content to a temporary file
with open("hello.html", "w") as file:
    file.write(html_content)

# Open the temporary HTML file in the browser
driver.get("file://" + os.path.abspath("hello.html"))

# Maximize the browser window
driver.maximize_window()
time.sleep(15)

# Print "hello world!" to the console
print("hello world!")

# Close the driver
driver.quit()

