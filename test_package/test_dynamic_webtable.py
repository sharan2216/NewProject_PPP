import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#comment 1 added
#comment 2 added

def test_tutorials_ninja():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demo.opencart.com/admin/")
    time.sleep(3)
    username=driver.find_element(By.ID,"input-username")
    username.send_keys("demo")
    time.sleep(2)
    password=driver.find_element(By.ID,"input-password")
    password.send_keys("demo")
    time.sleep(2)
    button=driver.find_element(By.XPATH,"//button[@type='submit']")
    button.click()
    time.sleep(2)
    close_btn=driver.find_element(By.XPATH,"//button[@class='btn-close']")
    close_btn.click()
    time.sleep(2)
    sales=driver.find_element(By.XPATH,"//a[contains(text(),' Sales')]")
    sales.click()
    time.sleep(2)
    orders=driver.find_element(By.XPATH,"//a[contains(text(),'Orders')]")
    orders.click()
    time.sleep(3)

    expected_customer = "Azar Tamboli"
    # cust_name = driver.find_element(By.XPATH,"//td[normalize-space()='Azar Tamboli']")
    cust_names = driver.find_elements(By.XPATH, "//form[@id='form-order']//tr/td[4]")

    i=0
    for customer in cust_names:
        if customer.text.__eq__(expected_customer):
            xpath_text = "//form[@id='form-order']//tr["+str(i)+"]/td[1]"
            driver.find_element(By.XPATH,xpath_text).click()
        i=i+1
    driver.get_screenshot_as_file("./ScreenShots/NEW_SS_SHOT.png")
    time.sleep(5)