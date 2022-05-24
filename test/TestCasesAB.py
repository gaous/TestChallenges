import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import CustomData.datas as data


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        # Initiating the chrome browser
        self.driver = webdriver.Chrome()

    def tearDown(self) -> None:
        # Closing the tab
        self.driver.close()

    def test_for_checking_test_A(self):
        # Going to the google website
        self.driver.get(data.GOOGLE_LINK)
        # Closing popup from google
        element = self.driver.find_elements_by_xpath(data.XPATH_LINK_TO_SECOND_BUTTON_IN_GOOGLE_POPUP)
        element.__getitem__(1).click()
        # Finding the search bar and entering 'CyberAlpaca' text
        element = self.driver.find_element_by_name(data.SEARCHBAR_ELEMENT_NAME)
        element.click()
        element.send_keys(data.CYBERALPACA)
        element.send_keys(Keys.ENTER)
        # Checking if the website of CyberAlpaca appears in the search bar
        element = self.driver.find_element_by_xpath(data.XPATH_LINK_TO_CYBERALPACA)
        self.assertEqual(element.text, data.CYBERALPACA_LINK)

    def test_for_checking_test_B(self):
        # Going to cyberalpaca website
        self.driver.get(data.CYBERALPACA_LINK)
        # Finding and going to the services page
        element = self.driver.find_element_by_link_text(data.SERVICE_ELEMENT_TEXT)
        element.click()
        # Retrieving text of the header and checking appropriate text.
        element = self.driver.find_element_by_xpath(data.XPATH_LINK_TO_OUR_SERVICE_HEADER)
        self.assertEqual(element.text, data.OUR_SERVICES)

        element = self.driver.find_elements_by_xpath(data.XPATH_LINK_TO_AUTOMATED_GUI_TESTING)
        element.__getitem__(0).click()
        element = self.driver.find_element_by_xpath(data.XPATH_LINK_TO_SQUISH1)
        self.assertEqual(element.get_attribute("title"), "Squish")

        element = self.driver.find_elements_by_xpath(data.XPATH_LINK_TO_AUTOMATED_GUI_TESTING)
        element.__getitem__(1).click()
        element = self.driver.find_element_by_xpath(data.XPATH_LINK_TO_SQUISH2)
        self.assertEqual(element.get_attribute("title"), "Squish")

        element = self.driver.find_elements_by_xpath(data.XPATH_LINK_TO_AUTOMATED_GUI_TESTING)
        element.__getitem__(2).click()
        element = self.driver.find_element_by_xpath(data.XPATH_LINK_TO_SQUISH3)
        self.assertEqual(element.get_attribute("title"), "Squish")

        element = self.driver.find_elements_by_xpath(data.XPATH_LINK_TO_AUTOMATED_GUI_TESTING)
        element.__getitem__(3).click()
        element = self.driver.find_element_by_xpath(data.XPATH_LINK_TO_SQUISH4)
        self.assertEqual(element.get_attribute("title"), "Squish")

        element = self.driver.find_elements_by_xpath(data.XPATH_LINK_TO_AUTOMATED_GUI_TESTING)
        element.__getitem__(4).click()
        element = self.driver.find_element_by_xpath(data.XPATH_LINK_TO_SOAP)
        self.assertNotEqual(element.get_attribute("title"), "Squish")


if __name__ == '__main__':
    unittest.main()
