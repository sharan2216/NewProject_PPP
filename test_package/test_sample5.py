import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_tutorials_ninja():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    time.sleep(3)
    expected_title="Your Store"
    actual_title=driver.title
    time.sleep(3)
    assert expected_title.__eq__(actual_title)
    driver.find_element(By.NAME,"search").send_keys("HP")
    time.sleep(3)
    driver.find_element(By.XPATH,"//button[contains(@class,'btn-default btn-lg')]").click()
    time.sleep(3)
    print("NEXT ASSERTION line printed here")
    assert driver.find_element(By.LINK_TEXT,"HP LP3065").is_displayed()

    driver.quit()