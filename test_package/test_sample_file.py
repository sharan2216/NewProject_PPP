import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_omayo_webtables():
    driver = webdriver.Chrome()
    driver.get("https://omayo.blogspot.com/")
    driver.maximize_window()
    time.sleep(2)

    driver.execute_script("window.scrollBy(0,500)")
    time.sleep(3)
    alert_demo=driver.find_element(By.XPATH,"//h2[normalize-space()='AlertDemo']")
    driver.execute_script("arguments[0].scrollIntoView()",alert_demo)
    time.sleep(5)