import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.calc_page import CalculatorPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calc(driver):
    calc = CalculatorPage(driver)
    calc.open()
    calc.delay()
    calc.primer()
    calc.get_result()

    result_element = WebDriverWait(driver, 45).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )
    assert result_element, "Результат не равен 15"
