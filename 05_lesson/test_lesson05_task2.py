from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/forms/post")

    name = driver.find_element(By.NAME, "custname")
    name.send_keys("Valerie")

    button = driver.find_element(By.XPATH, "//button[text()='Submit order']")
    button.click()
    sleep(2)

    assert driver.current_url.endswith("https://httpbin.org/post")

    driver.quit()
