import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_main_page(browser):
    browser.get(browser.url)
    wait = WebDriverWait(browser, 3)
    wait.until(EC.title_is("Your Store"))
    wait.until(EC.visibility_of_element_located((By.ID, "search")))
    wait.until(EC.element_to_be_clickable((By.ID, "cart")))
    wait.until(EC.visibility_of_element_located((By.ID, "menu")))
    wait.until(EC.visibility_of_element_located((By.ID, "content")))


def test_product_macbook(browser):
    browser.get(browser.url + "/index.php?route=product/product&product_id=43")
    wait = WebDriverWait(browser, 3)
    wait.until(EC.title_is("MacBook"))
    wait.until(EC.visibility_of_element_located((By.ID, "product-product")))
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "thumbnails")))
    wait.until(EC.element_to_be_clickable((By.ID, "button-cart")))
    wait.until(EC.text_to_be_present_in_element((By.ID, "button-cart"), "Add to Cart"))


def test_login_page_external(browser):
    browser.get(browser.url + "/admin")
    wait = WebDriverWait(browser, 3)
    wait.until(EC.visibility_of_element_located((By.ID, "input-username")))
    wait.until(EC.visibility_of_element_located((By.NAME, "password")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()='OpenCart']")))
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Forgotten Password")))


def test_register_account(browser):
    browser.get(browser.url + "/index.php?route=account/register")
    wait = WebDriverWait(browser, 3)
    wait.until(EC.visibility_of_element_located((By.ID, "content")))
    wait.until(EC.visibility_of_element_located((By.ID, "account")))
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()='Your Password']")))
    wait.until(EC.visibility_of_element_located((By.ID, "input-password")))
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))


def test_catalog(browser):
    browser.get(browser.url + "/index.php?route=product/category&path=20")
    wait = WebDriverWait(browser, 3)
    wait.until(EC.visibility_of_element_located((By.ID, "product-category")))
    wait.until(EC.visibility_of_element_located((By.ID, "column-left")))
    wait.until(EC.element_to_be_clickable((By.ID, "list-view")))
    wait.until(EC.element_to_be_clickable((By.ID, "grid-view")))
    wait.until(EC.text_to_be_present_in_element((By.ID, "compare-total"), "Product Compare"))
