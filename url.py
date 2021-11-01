from selenium import webdriver
import time
options=webdriver.ChromeOptions()
browser = webdriver.Chrome('D:/Jayesh/chromedriver.exe')
#maximize_window
browser.maximize_window()
browser.get('https://jayesh15.github.io/')
time.sleep(10)
browser.quit()

