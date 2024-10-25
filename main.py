import data
from methods import MethodsUrbanRoutesPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from locators import UrbanRoutesPage

class TestUrbanRoutes:
    driver = None
    methods = None

    @classmethod
    def setup_class(cls):
        # Configurar las opciones del navegador
        options = Options()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

        # Iniciar el servicio de Chrome
        service = Service()  # Puedes pasar el path del driver aquí si es necesario

        # Inicializar el driver con opciones
        cls.driver = webdriver.Chrome(service=service, options=options)
        cls.driver.get(data.urban_routes_url)
        cls.locators = UrbanRoutesPage()
        cls.routes_page = MethodsUrbanRoutesPage(cls.driver)

        cls.driver.implicitly_wait(10)


    def test_set_route(self):
        self.routes_page.set_from_field()
        self.routes_page.set_to_field()
        assert self.routes_page.get_from() == data.address_from
        assert self.routes_page.get_to() == data.address_to

    def test_click_button_get_a_cab(self):
        self.routes_page.click_button_get_a_cab()

    def test_click_button_comfort(self):
        self.routes_page.click_button_comfort()
        assert self.routes_page.verify_click_button_comfort() == 'Manta y pañuelos'

    def test_add_phone_number(self):
        self.routes_page.click_button_phone_number()
        self.routes_page.click_phone_number_field()
        self.routes_page.set_phone_number_field()
        assert self.routes_page.get_phone_number_field() == data.phone_number
        self.routes_page.click_button_following()
        self.routes_page.set_code_sms_field()
        self.routes_page.click_button_confirm()
        assert self.routes_page.verify_phone_number_field() == data.phone_number

    def test_add_payment_method(self):
        self.routes_page.click_payment_method()
        self.routes_page.click_add_card()
        self.routes_page.click_number_card_field()
        self.routes_page.set_number_card_field()
        assert self.routes_page.get_number_card_field() == data.card_number
        self.routes_page.click_code_card_field()
        self.routes_page.set_code_card_field()
        assert self.routes_page.get_code_card_field() == data.card_code
        self.routes_page.click_body_credit_card()
        self.routes_page.click_button_add()
        self.routes_page.click_button_x()
        assert self.routes_page.verify_button_card_name() == 'Tarjeta'

    def test_click_message_for_driver_field(self):
        self.routes_page.click_message_for_driver_field()
        self.routes_page.set_message_for_driver_field()
        assert self.routes_page.get_message_for_driver_field() == data.message_for_driver

    def test_click_blanket_scarves_field(self):
        self.routes_page.click_blanket_scarves_field()

    def test_click_add_ice_cream(self):
        self.routes_page.click_add_ice_cream()
        self.routes_page.click_add_ice_cream()
        assert self.routes_page.verify_twice_click_ice_cream() == '2'

    def test_click_button_get_a_taxi(self):
        self.routes_page.click_button_looking_for_taxi()

    def test_wait_window_waiting_taxi(self):
        assert self.routes_page.wait_window_waiting_taxi() == 'Detalles'


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

