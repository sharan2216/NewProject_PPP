import random
import time
from selenium import webdriver
# from time import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
#initialize webdriver
driver=webdriver.Chrome(options=options)

#if required update the chromeDriver version at "C:\Windows" location
#open URL and maximize window


def test_tutorial_ninja():
    driver.get("https://tutorialsninja.com/demo/")
    driver.maximize_window()
    #phone button
    # phone=driver.find_element(By.XPATH,"//a[text()='Phones & PDAs']")
    # phone.click()
    time.sleep(2)



def test_omayo():
    driver.get("https://omayo.blogspot.com/")
    driver.maximize_window()
    #phone button
    # phone=driver.find_element(By.XPATH,"//a[text()='Phones & PDAs']")
    # phone.click()
    time.sleep(2)


def test_seleniumblogspot():
    driver.get("https://seleniumpractice.blogspot.com/")
    driver.maximize_window()
    #phone button
    # phone=driver.find_element(By.XPATH,"//a[text()='Phones & PDAs']")
    # phone.click()
    time.sleep(2)


def test_seleniumbyarun():
    driver.get("https://selenium-by-arun.blogspot.com/")
    driver.maximize_window()
    #phone button
    # phone=driver.find_element(By.XPATH,"//a[text()='Phones & PDAs']")
    # phone.click()
    time.sleep(2)


def test_leet_code():
    driver.get("https://letcode.in/test")
    driver.maximize_window()
    #phone button
    # phone=driver.find_element(By.XPATH,"//a[text()='Phones & PDAs']")
    # phone.click()
    time.sleep(2)


