from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def initiate_chrome_driver(executable_path="./chromedriver"):
    """
    Initiates a chrome driver.
    """
    service = Service(executable_path=executable_path)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")

    return webdriver.Chrome(service=service, options=chrome_options)


def get_element_without_waiting(driver, element_name):
    """
    Returns an element of the page without waiting for it to be loaded.
    """

    return driver.find_element(By.CLASS_NAME, element_name)


def get_element_with_explicit_waiting(driver, element_name):
    """
    Returns an element of the page with explicit waiting.
    """

    return WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element(By.CLASS_NAME, element_name))


def get_element_with_fluent_waiting(driver, element_name):
    """
    Returns an element of the page with fluent waiting.
    """

    wait = WebDriverWait(driver, 10, poll_frequency=1,
                         ignored_exceptions=[NoSuchElementException])

    return wait.until(
        lambda driver: driver.find_element(By.CLASS_NAME, element_name))


def click_list_element(element):
    """
    Clicks the list element.
    """
    element.click()
