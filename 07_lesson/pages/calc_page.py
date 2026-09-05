from selenium.webdriver.common.by import By


class CalculatorPage:

    def __init__(self, driver):
        self.driver = driver

    SEVEN = (By.XPATH, "//div[@class='keys']//span[text()='7']")
    PLUS = (By.XPATH, "//div[@class='keys']//span[text()='+']")
    EIGHT = (By.XPATH, "//div[@class='keys']//span[text()='8']")
    EQUALLY = (By.XPATH, "//div[@class='keys']//span[text()='=']")

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def delay(self):
        self.driver.find_element(By.ID, 'delay').clear()
        self.driver.find_element(By.ID, 'delay').send_keys("45")

    def primer(self):
        self.driver.find_element(*self.SEVEN).click()
        self.driver.find_element(*self.PLUS).click()
        self.driver.find_element(*self.EIGHT).click()
        self.driver.find_element(*self.EQUALLY).click()

    def get_result(self):
        result_field = self.driver.find_element(By.XPATH, "//div[@class='screen']")
        return result_field.text
