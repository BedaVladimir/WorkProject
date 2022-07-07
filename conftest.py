import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser")
    browser = webdriver.Edge()
    browser.set_window_size(1920, 1080)
    browser.get("https://portal.onegroup.ru/")
    browser.implicitly_wait(3)
    yield browser
    print("\nquit browser")
    browser.quit()


@pytest.fixture
def browser_dev4():
    print("\nоткрыт портал")
    browser = webdriver.Edge()
    browser.implicitly_wait(10)
    browser.maximize_window()
    browser.get("https://dev-bitrix4.onegroup.ru/")
    browser.find_element(By.CSS_SELECTOR, "[name='USER_LOGIN']").send_keys("beda_vv")
    browser.find_element(By.CSS_SELECTOR, "[name='USER_PASSWORD']").send_keys("TestPassword")
    browser.find_element(By.CSS_SELECTOR, ".login-btn").click()
    yield browser
    print("\nзакрыт портал")
    browser.quit()


@pytest.fixture
def browser_dev():
    print("\nоткрыть портал")
    browser = webdriver.Edge()
    browser.implicitly_wait(10)
    browser.maximize_window()
    browser.get("https://dev-bitrix2.onegroup.ru/")
    # browser.find_element(By.CSS_SELECTOR, ".content a ").click()
    browser.find_element(By.CSS_SELECTOR, "[name='USER_LOGIN']").send_keys("beda_vv")
    browser.find_element(By.CSS_SELECTOR, "[name='USER_PASSWORD']").send_keys("TestPassword")
    browser.find_element(By.CSS_SELECTOR, ".login-btn").click()
    yield browser
    browser.quit()
