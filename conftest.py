from selenium import webdriver
import pytest


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(3)#неявное ожидание 3 секунды, чтобы все загрузилось
    yield browser
    browser.close()

