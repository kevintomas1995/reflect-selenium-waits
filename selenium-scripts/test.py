import unittest
from utils import *


class SearchElements(unittest.TestCase):
    def setUp(self):
        self.driver = initiate_chrome_driver()
        self.driver.get("http://localhost:3000/")

    def test_get_element_without_waiting(self):
        for element_name in ["instant", "miliseconds", "timeout"]:
            if element_name == "instant":
                element = get_element_without_waiting(
                    self.driver, element_name)

                for item in element.find_elements(By.TAG_NAME, "li"):
                    self.assertEqual(
                        "color: black;", item.get_attribute("style"))
            else:
                with self.assertRaises(NoSuchElementException):
                    get_element_without_waiting(self.driver, element_name)

    def test_get_element_with_explicit_waiting(self):
        for element_name in ["instant", "miliseconds", "timeout"]:
            element = get_element_with_explicit_waiting(
                self.driver, element_name)

            for item in element.find_elements(By.TAG_NAME, "li"):
                self.assertEqual("color: black;", item.get_attribute("style"))

    def test_get_element_with_implicit_waiting(self):
        self.driver.implicitly_wait(5)

        for element_name in ["instant", "miliseconds", "timeout"]:
            element = get_element_without_waiting(
                self.driver, element_name)

            for item in element.find_elements(By.TAG_NAME, "li"):
                self.assertEqual("color: black;", item.get_attribute("style"))

    def test_get_element_with_fluent_waiting(self):
        for element_name in ["instant", "miliseconds", "timeout"]:
            element = get_element_with_fluent_waiting(
                self.driver, element_name)

            for item in element.find_elements(By.TAG_NAME, "li"):
                self.assertEqual("color: black;", item.get_attribute("style"))

    def test_get_element_without_waiting_and_click(self):
        for element_name in ["instant", "miliseconds", "timeout"]:
            if element_name == "instant":
                element = get_element_without_waiting(
                    self.driver, element_name)

                click_list_element(element)

                for item in element.find_elements(By.TAG_NAME, "li"):
                    self.assertEqual(
                        "color: white;", item.get_attribute("style"))
            else:
                with self.assertRaises(NoSuchElementException):
                    get_element_without_waiting(self.driver, element_name)

    def test_get_element_with_explicit_waiting_and_click(self):
        for element_name in ["instant", "miliseconds", "timeout"]:
            element = get_element_with_explicit_waiting(
                self.driver, element_name)

            click_list_element(element)

            for item in element.find_elements(By.TAG_NAME, "li"):
                self.assertEqual("color: white;", item.get_attribute("style"))

    def test_get_element_with_implicit_waiting_and_click(self):
        self.driver.implicitly_wait(5)

        for element_name in ["instant", "miliseconds", "timeout"]:
            element = get_element_without_waiting(
                self.driver, element_name)

            click_list_element(element)

            for item in element.find_elements(By.TAG_NAME, "li"):
                self.assertEqual("color: white;", item.get_attribute("style"))

    def test_get_element_with_fluent_waiting_and_click(self):
        for element_name in ["instant", "miliseconds", "timeout"]:
            element = get_element_with_fluent_waiting(
                self.driver, element_name)

            click_list_element(element)

            for item in element.find_elements(By.TAG_NAME, "li"):
                self.assertEqual("color: white;", item.get_attribute("style"))

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
