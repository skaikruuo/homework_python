from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")

    user_name = driver.find_element(By.ID, "user-name")
    user_name.send_keys("standard_user")

    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    backpack = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    backpack.click()

    t_short = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    t_short.click()

    onesie = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
    onesie.click()

    cart = driver.find_element(By.ID, "shopping_cart_container")
    cart.click()

    checkout = driver.find_element(By.CLASS_NAME, "checkout_button")
    checkout.click()

    first_name = driver.find_element(By.ID, "first-name")
    first_name.send_keys("Валерия")

    last_name = driver.find_element(By.ID, "last-name")
    last_name.send_keys("Васильева")

    zip = driver.find_element(By.ID, "postal-code")
    zip.send_keys("142100")

    continue_btn = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.ID, "continue"))
    )
    continue_btn.click()

    total_element = driver.find_element(By.XPATH, "//div[@class='summary_total_label']")
    final_total = total_element.text
    print("Итоговая стоимость:", final_total)

    driver.quit()

    assert final_total == 'Total: $58.29'
