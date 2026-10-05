from selenium import webdriver
from selenium.webdriver.common.by import By

def test_element_state():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/radio-button")

    button = driver.find_element(By.ID, "yesRadio")
    assert button.is_displayed() == True  

    assert button.is_enabled() == True

    driver.quit()
