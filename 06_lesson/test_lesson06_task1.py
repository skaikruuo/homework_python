from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    start_btn = driver.find_element(By.CSS_SELECTOR, "#start button")
    start_btn.click()

    wait.until(EC.visibility_of_element_located((By.ID, "finish")))
    element = driver.find_element(By.ID, "finish")
    text = element.text
    assert text == "Hello World!"

    driver.save_screenshot("screenshots/full_screen.png")

    driver.quit()
