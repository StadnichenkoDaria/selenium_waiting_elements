import os.path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true", help="Maximize browser window")
    parser.addoption("--drivers", action="store_true", default=os.path.expanduser("~/Develop/drivers"))
    parser.addoption("--browser", action="store", default="chrome", choices=["chrome", "firefox", "opera"])
    parser.addoption("--url", action="store", default="https://demo.opencart.com")


@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    maximized = request.config.getoption("--maximized")
    drivers = request.config.getoption("--drivers")

    if browser == "chrome":
        service = Service(executable_path=drivers + "/chromedriver")
        driver = webdriver.Chrome(service=service)
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=drivers + "/geckodriver")
    elif browser == "opera":
        driver = webdriver.Opera(executable_path=drivers + "/operadriver")

    driver.maximize_window()

    request.addfinalizer(driver.close)

    driver.get(url)
    driver.url = url

    return driver
