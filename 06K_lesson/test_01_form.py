from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form():
    driver = webdriver.Edge()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    first_name = driver.find_element(By.NAME, "first-name")
    first_name.send_keys("Иван")

    last_name = driver.find_element(By.NAME, "last-name")
    last_name.send_keys("Петров")

    address = driver.find_element(By.NAME, "address")
    address.send_keys("Ленина, 55-3")

    email = driver.find_element(By.NAME, "e-mail")
    email.send_keys("test@skypro.com")

    phone_number = driver.find_element(By.NAME, "phone")
    phone_number.send_keys("+7985899998787")

    city = driver.find_element(By.NAME, "city")
    city.send_keys("Москва")

    country = driver.find_element(By.NAME, "country")
    country.send_keys("Россия")

    job = driver.find_element(By.NAME, "job-position")
    job.send_keys("QA")

    company = driver.find_element(By.NAME, "company")
    company.send_keys("SkyPro")

    submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_btn.click()

    zip_code = driver.find_element(By.ID, "zip-code")
    border_color = zip_code.value_of_css_property('border-color')
    assert border_color == 'rgb(245, 194, 199)'

    first_name_element = driver.find_element(By.ID, "first-name")
    border_color = first_name_element.value_of_css_property('border-color')
    assert border_color == 'rgb(186, 219, 204)'

    last_name_element = driver.find_element(By.ID, "last-name")
    border_color = last_name_element.value_of_css_property('border-color')
    assert border_color == 'rgb(186, 219, 204)'

    address_element = driver.find_element(By.ID, "address")
    border_color = address_element.value_of_css_property('border-color')
    assert border_color == 'rgb(186, 219, 204)'

    email_element = driver.find_element(By.ID, "e-mail")
    border_color = email_element.value_of_css_property('border-color')
    assert border_color == 'rgb(186, 219, 204)'

    phone_element = driver.find_element(By.ID, "phone")
    border_color = phone_element.value_of_css_property('border-color')
    assert border_color == 'rgb(186, 219, 204)'

    city_element = driver.find_element(By.ID, "city")
    border_color = city_element.value_of_css_property('border-color')
    assert border_color == 'rgb(186, 219, 204)'

    country_element = driver.find_element(By.ID, "country")
    border_color = country_element.value_of_css_property('border-color')
    assert border_color == 'rgb(186, 219, 204)'

    job_element = driver.find_element(By.ID, "job-position")
    border_color = job_element.value_of_css_property('border-color')
    assert border_color == 'rgb(186, 219, 204)'

    company_element = driver.find_element(By.ID, "company")
    border_color = company_element.value_of_css_property('border-color')
    assert border_color == 'rgb(186, 219, 204)'

    driver.quit()
