from selenium import webdriver
import time
options=webdriver.ChromeOptions()
browser = webdriver.Chrome('D:/Jayesh/chromedriver.exe')
#maximize_window
browser.maximize_window()
browser.get('https://jayesh15.github.io/')
time.sleep(10)
browser.get_screenshot_as_file("screenshot.png") #screenshot location location
browser.quit()

