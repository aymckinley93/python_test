import time
from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import data
import helpers
from data import CARD_NUMBER, PHONE_NUMBER, CARD_CODE, MESSAGE_FOR_DRIVER
from helpers import retrieve_phone_code

class UrbanRoutesPage:
    # Addresses
    FROM_FIELD = (By.ID, 'from')
    TO_FIELD = (By.ID, 'to')
    # Tariff and cell button
    SUPPORTIVE_PLAN_CARD = (By.XPATH,'//div[contains(text(), "Supportive")]')
    SUPPORTIVE_PLAN_CARD_PARENT = (By.XPATH,'//div[contains(text(), "Supportive")]//..')
    ACTIVE_PLAN_CARD = (By.XPATH,'//div[@class="tcard active"]//div[@class="tcard-title"]')
    CALL_TAXI_BUTTON = (By.XPATH, '//button[contains(text(), "Call a taxi")]')
    # Phone number
    PHONE_NUMBER_CONTROL = (By.CLASS_NAME, "np-text")
    PHONE_NUMBER_INPUT = (By.ID, "phone")
    PHONE_NUMBER_NEXT_BUTTON = (By.XPATH, '//button[contains(text(), "Next")]')
    PHONE_NUMBER_CODE_INPUT = (By.ID, "code")
    PHONE_NUMBER_CONFIRM_BUTTON = (By.XPATH, '//button[contains(text(), "Confirm")]')
    # Credit card
    PAYMENT_METHOD_CONTROL = (By.CLASS_NAME, 'pp-text')
    PAYMENT_METHOD_ADD_CARD_LOCATOR = (By.XPATH, '//div[text()="Add card"]')
    PAYMENT_METHOD_CARD_NUMBER_LOCATOR = (By.XPATH, '//div[@class="card-number-input"]//input[@id="number"]')
    PAYMENT_METHOD_CODE_LOCATOR = (By.XPATH, '//input[@class="card-input" and @id="code"]')
    PAYMENT_METHOD_LINK_BUTTON_LOCATOR = (By.XPATH, '//button[text()="Link"]')
    # Comment to taxi driver
    SELECT_MESSAGE_DRIVER = (By.CLASS_NAME, 'input-container')
    MESSAGE_DRIVER = (By.ID, 'comment')
    ENTER_MESSAGE = (By.XPATH, '//label[text()="Message to the driver..."]')
    # Blanket and handkerchief
    BLANKET_HANDKERCHIEF_LOCATOR = (By.CLASS_NAME, 'switch')
    BLANKET_HANDKERCHIEF_CHECK_LOCATOR = (By.CLASS_NAME, 'switch-input')
    # Ice creams
    ORDER_ICE_CREAM = (By.CLASS_NAME, 'counter-value')
    ICE_CREAM_ADD_BUTTON = (By.CLASS_NAME, 'counter-plus')
    # Supportive tariff
    ORDER_CAR_BUTTON = (By.CLASS_NAME, 'smart-button-wrapper')
    ORDER_CAR_SEARCH_MODAL = (By.CLASS_NAME, 'order-body')

    def __init__(self, driver):
        self.driver = driver

    def set_from(self,from_address):
        self.driver.find_element(*self.FROM_FIELD).send_keys(from_address)

    def set_to(self,to_address):
        self.driver.find_element(*self.TO_FIELD).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.FROM_FIELD).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.TO_FIELD).get_property('value')

    def click_call_taxi_button(self):
        self.driver.find_element(*self.CALL_TAXI_BUTTON).click()

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)
        self.click_call_taxi_button()

    def select_supportive_plan(self):
        self.driver.find_element(*self.SUPPORTIVE_PLAN_CARD).click()


    def get_current_selected_plan(self):
        return self.driver.find_element(*self.ACTIVE_PLAN_CARD).text

    def set_phone(self, number):
        self.driver.find_element(*self.PHONE_NUMBER_CONTROL).click()
        self.driver.find_element(*self.PHONE_NUMBER_INPUT).send_keys(PHONE_NUMBER)
        self.driver.find_element(*self.PHONE_NUMBER_NEXT_BUTTON).click()
        code = helpers.retrieve_phone_code(self.driver)
        self.driver.find_element(*self.PHONE_NUMBER_CODE_INPUT).send_keys(code)
        self.driver.find_element(*self.PHONE_NUMBER_CONFIRM_BUTTON).click()

    def get_phone(self):
        return self.driver.find_element(*self.PHONE_NUMBER_INPUT).get_attribute('value')


    def fill_card(self, card_number, code):
        self.driver.find_element(*self.PAYMENT_METHOD_CONTROL).click()
        self.driver.find_element(*self.PAYMENT_METHOD_ADD_CARD_LOCATOR).click()
        self.driver.find_element(*self.PAYMENT_METHOD_CARD_NUMBER_LOCATOR).send_keys(CARD_NUMBER)
        self.driver.find_element(*self.PAYMENT_METHOD_CODE_LOCATOR).send_keys(CARD_CODE)
        self.driver.find_element(*self.PAYMENT_METHOD_LINK_BUTTON_LOCATOR).click()

    def get_add_card_locator(self):
        return self.driver.find_element(*self.PAYMENT_METHOD_ADD_CARD_LOCATOR).get_attribute('value')

    def get_credit_card_locator(self):
        return self.driver.find_element(*self.PAYMENT_METHOD_CARD_NUMBER_LOCATOR).get_attribute('value')

    def get_payment_method_locator(self):
        return self.driver.find_element(*self.PAYMENT_METHOD_CONTROL).get_attribute('value')

    def select_driver_message(self):
        self.driver.find_element(*self.SELECT_MESSAGE_DRIVER).click()

    def set_driver_message(self, message=data.MESSAGE_FOR_DRIVER):
        self.driver.find_element(*self.MESSAGE_DRIVER).send_keys(message)

    def driver_message_click(self):
        self.driver.find_element(*self.ENTER_MESSAGE).click()

    def get_driver_comment(self):
        return self.driver.find_element(*self.MESSAGE_DRIVER).get_attribute('value')

    def set_handkerchief_blanket_slider(self):
        self.driver.find_element(*self.BLANKET_HANDKERCHIEF_LOCATOR).click()

    def get_handkerchief_blanket_slider(self):
        return self.driver.find_element(*self.BLANKET_HANDKERCHIEF_CHECK_LOCATOR).get_property('checked')

    def set_ice_cream(self):
        for ice_cream in range(2):
            self.driver.find_element(*self.ICE_CREAM_ADD_BUTTON).click()
            number_of_ice_creams = 2

    def get_ice_cream(self):
        return int(self.driver.find_elements(*self.ORDER_ICE_CREAM)[0].text)


    def set_order_button(self):
        self.driver.find_element(*self.ORDER_CAR_BUTTON).click()

    def get_order_button(self):
        return self.driver.find_element(*self.ORDER_CAR_SEARCH_MODAL).is_displayed()


