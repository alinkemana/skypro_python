from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")

    username = driver.find_element(By.NAME, "custname")
    username.send_keys("Алина")

    driver.find_element(
        By.XPATH, "//button[text()='Submit order']").click()
    assert driver.current_url == ("https://httpbin.qa-territory.online/post")

    driver.quit()
