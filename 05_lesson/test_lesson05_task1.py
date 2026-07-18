from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/")

    html = driver.find_element(By.LINK_TEXT, "HTML form")
    html.click()

    assert driver.current_url.endswith("/forms/post")

    driver.back()
    assert driver.current_url.endswith("https://httpbin.org/")

    driver.quit()
