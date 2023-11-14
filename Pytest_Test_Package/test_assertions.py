import random
import time

import allure
from allure_commons.types import AttachmentType
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

class Tutorialninja:

    def test_tutorial_ninja(setup_and_teardown):
        # driver.get("https://tutorialsninja.com/demo/")
        # driver.maximize_window()
        expected_title="Your Store"
        actual_title=driver.title
        assert expected_title.__eq__(actual_title)
        driver.find_element(By.NAME,"search").send_keys("HP")
        driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
        time.sleep(3)
        assert driver.find_element(By.LINK_TEXT,"HP LP3065").is_displayed()
        print("HP LP3065 EXIST")
        # driver.quit()


