from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Set up ChromeDriver service
service = Service(executable_path="C:\\swathi_online training\\JarFiles\\Chromedriver\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
options = Options()

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(service=service, options=options)

# Open Google
driver.get("https://www.google.com/")

# Maximize the window
driver.maximize_window()

# Print a message
print("Hello World!")

# If you want to interact with the page or extract HTML content, you can do it here

# Example: Get the page source
page_source = driver.page_source
print(page_source)

# Close the driver
driver.quit()
