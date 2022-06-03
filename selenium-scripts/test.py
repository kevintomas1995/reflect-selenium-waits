from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def print_list_items(element):
    """
    Prints the items of the list.
    """
    print(element.find_element(By.CLASS_NAME, "list-header").text)

    for item in element.find_elements(By.TAG_NAME, "li"):
        print(item.text)

    print("*" * 20)


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

    wait = WebDriverWait(driver, timeout=10, poll_frequency=1,
                         ignored_exceptions=[NoSuchElementException])

    return wait.until(
        lambda driver: driver.find_element(By.CLASS_NAME, element_name))


# Create a new instance of the Chrome driver
service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service=service)

# Load the page
SITE = "http://localhost:3000/"
driver.get(SITE)

# Access the list called instant
# instant_el = get_element_without_waiting(driver, "instant")
# print_list_items(instant_el)


# This will throw an exception because the list is not loaded yet
# selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"css selector","selector":".miliseconds"}
#   (Session info: chrome=102.0.5005.61)
# milisec_el = get_element_without_waiting(driver, "miliseconds")
# print_list_items(milisec_el)


# Waiting strategies
# Explicit wait
# instant_el = get_element_with_explicit_waiting(driver, "instant")
# print_list_items(instant_el)

# milisec_el = get_element_with_explicit_waiting(driver, "miliseconds")
# print_list_items(milisec_el)

# timeout_element = get_element_with_explicit_waiting(driver, "timeout")
# print_list_items(timeout_element)

# Implicit wait
# driver.implicitly_wait(5)

# instant_el = get_element_without_waiting(driver, "instant")
# print_list_items(instant_el)

# milisec_el = get_element_without_waiting(driver, "miliseconds")
# print_list_items(milisec_el)

# timeout_element = get_element_without_waiting(driver, "timeout")
# print_list_items(timeout_element)

# Fluent wait
instant_el = get_element_with_fluent_waiting(driver, "instant")
print_list_items(instant_el)

milisec_el = get_element_with_fluent_waiting(driver, "miliseconds")
print_list_items(milisec_el)

timeout_element = get_element_with_fluent_waiting(driver, "timeout")
print_list_items(timeout_element)


driver.quit()
