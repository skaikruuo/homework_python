from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopPage:

    BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    T_SHIRT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE = (By.ID, "add-to-cart-sauce-labs-onesie")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP = (By.ID, "postal-code")

    def __init__(self, driver):
        self.driver = driver

    def login(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()

    def cart(self):
        self.driver.find_element(*self.BACKPACK).click()
        self.driver.find_element(*self.T_SHIRT).click()
        self.driver.find_element(*self.ONESIE).click()
        self.driver.find_element(By.ID, "shopping_cart_container").click()

    def checkout(self):
        self.driver.find_element(By.CLASS_NAME, "checkout_button").click()

    def info(self):
        self.driver.find_element(*self.FIRST_NAME).send_keys("Валерия")
        self.driver.find_element(*self.LAST_NAME).send_keys("Васильева")
        self.driver.find_element(*self.ZIP).send_keys("142100")
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "continue"))).click()
