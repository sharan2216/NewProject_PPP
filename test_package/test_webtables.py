import time

from selenium import webdriver
from selenium.webdriver.common.by import By
#comment 1 added
#comment 2 added


def test_omayo_webtables():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://omayo.blogspot.com/")
    time.sleep(2)
    table_rows=driver.find_elements(By.XPATH,"//table[@id='table1']//tr")
    row_count=len(table_rows)
    print("No of Rows in a Table :",row_count)
    table_columns=driver.find_elements(By.XPATH,"//table[@id='table1']//th")
    print("Table Columns are :",len(table_columns))
    first_columns_values=driver.find_elements(By.XPATH,"//table[@id='table1']//tr/*[1]")
    for i in first_columns_values:
        print(i.text)
    print()
    second_columns_values = driver.find_elements(By.XPATH, "//table[@id='table1']//tr/*[2]")
    for i in second_columns_values:
        print(i.text)
    print()
    third_columns_values = driver.find_elements(By.XPATH, "//table[@id='table1']//tr/*[3]")
    for i in third_columns_values:
        print(i.text)
    print()
    print("Headings values are :")
    heading_values=driver.find_elements(By.XPATH,"//table[@id='table1']//th")
    for i in heading_values:
        print(i.text)

    cell_value=driver.find_element(By.XPATH,"(//table[@id='table1']//tr)[4]//td[3]")
    print("4th row and 3rd column values is :",cell_value.text)

    table_rows=driver.find_elements(By.XPATH,"//table[@id='table1']//tr")
    row_count=len(table_rows)
    table_columns= driver.find_elements(By.XPATH,"//table[@id='table1']//th")
    col_count=len(table_columns)

    for r in range(1,row_count):
        for c in range(1,col_count):
            cell_xpath=driver.find_element(By.XPATH,"(//table[@id='table1']//tr)["+str(r)+"]//*["+str(c)+"]")
            print(cell_xpath.text)
    driver.quit()