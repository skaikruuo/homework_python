import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.shop_page import ShopPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop(driver):
    shop = ShopPage(driver)
    shop.login()
    shop.cart()
    shop.checkout()
    shop.info()

    total_element = driver.find_element(By.XPATH, "//div[@class='summary_total_label']")
    final_total = total_element.text
    print("Итоговая стоимость:", final_total)

    assert final_total == 'Total: $58.29'
