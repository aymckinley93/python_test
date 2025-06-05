from time import sleep

from selenium import webdriver
import data
import helpers
from pages import UrbanRoutesPage


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert routes_page.get_from() == data.ADDRESS_FROM
        assert routes_page.get_to() == data.ADDRESS_TO

    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.select_supportive_plan()
        assert routes_page.get_current_selected_plan() == 'Supportive'

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.set_phone(data.PHONE_NUMBER)
        assert routes_page.get_phone() == data.PHONE_NUMBER

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.select_supportive_plan()
        routes_page.fill_card(data.CARD_NUMBER, data.CARD_CODE)
        sleep(5)
        assert routes_page.get_payment_method_locator() != 'Card'
        sleep(2)

    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.select_supportive_plan()
        routes_page.set_driver_message()
        routes_page.get_driver_comment()
        sleep(3)
        assert routes_page.get_driver_comment() == data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.select_supportive_plan()
        routes_page.set_handkerchief_blanket_slider()
        assert routes_page.get_handkerchief_blanket_slider()


    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.select_supportive_plan()
        number_of_ice_creams = 2
        routes_page.set_ice_cream()
        routes_page.get_ice_cream()
        assert routes_page.get_ice_cream() == 2

    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.select_supportive_plan()
        routes_page.set_phone(data.PHONE_NUMBER)
        assert routes_page.get_phone() == data.PHONE_NUMBER
        routes_page.set_driver_message()
        routes_page.get_driver_comment()
        routes_page.get_driver_comment()
        sleep(3)
        assert routes_page.get_driver_comment() == data.MESSAGE_FOR_DRIVER
        sleep(2)
        routes_page.set_order_button()
        sleep(3)
        assert routes_page.get_order_button()


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()