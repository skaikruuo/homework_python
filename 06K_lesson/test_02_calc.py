from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calc():
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    delay = driver.find_element(By.ID, "delay")
    delay.clear()
    delay.send_keys("1")

    button_7 = driver.find_element(By.XPATH, "//div[@class='keys']//span[text()='7']")
    button_7.click()

    button_plus = driver.find_element(By.XPATH, "//div[@class='keys']//span[text()='+']")
    button_plus.click()

    button_8 = driver.find_element(By.XPATH, "//div[@class='keys']//span[text()='8']")
    button_8.click()

    button_equal = driver.find_element(By.XPATH, "//div[@class='keys']//span[text()='=']")
    button_equal.click()

    result_element = WebDriverWait(driver, 1).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )
    assert result_element, "Результат не равен 15"

    driver.quit()
