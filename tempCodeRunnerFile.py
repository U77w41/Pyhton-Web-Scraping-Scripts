# Import Dependencies
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# We have to download chrome driver and add the path in PATH
PATH = r"C:\Users\Ujjwa\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://twitter.com/login")