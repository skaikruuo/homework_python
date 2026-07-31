from selenium import webdriver


def test_session_storage_auth():
    driver = webdriver.Chrome()
    driver.get("https://gitflic.ru/")

    user1 = driver.add_cookie({
        "name": "SESSION",
        "value": "ODJjN2VmMjAtZTJhZS00ZjUwLWJmNDAtOTYxMjA5MjJlYTE3",
        "domain": "gitflic.ru"
    })

    driver.refresh()

    driver.get("https://gitflic.ru/user/airsworld")

    user1 = driver.current_url
    driver.delete_all_cookies()
    driver.refresh()

    user2 = driver.add_cookie({
        "name": "SESSION",
        "value": "NzM4NDhmMGItZWQ5MC00NTYzLWE1MDItMWFkYjlkZDFhODc2",
        "domain": "gitflic.ru"
    })

    driver.refresh()

    driver.get("https://gitflic.ru/user/vithjt348834")
    user2 = driver.current_url
    assert user1 != user2

    driver.quit()
