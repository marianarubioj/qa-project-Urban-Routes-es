import helpers
import data
from locators import UrbanRoutesPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MethodsUrbanRoutesPage:

    def __init__(self, driver):
        self.driver = driver
        self.locators = UrbanRoutesPage

#1. Configurar la dirección
    def click_from_field(self):
        self.driver.find_element(*self.locators.from_field).click()

    def set_from_field(self):
        self.driver.find_element(*self.locators.from_field).send_keys(data.address_from)

    def get_from(self):
        return self.driver.find_element(*self.locators.from_field).get_property('value')  # le agregue locators

    def click_to_field(self):
        self.driver.find_element(*self.locators.to_field).click()

    def set_to_field(self):
        self.driver.find_element(*self.locators.to_field).send_keys(data.address_to)

    def get_to(self):
        return self.driver.find_element(*self.locators.to_field).get_property('value')  # le agregue locators

    def click_button_get_a_cab(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME,'button.round')))
        self.driver.find_element(*self.locators.button_get_a_cab).click()

#2. Seleccionar la tarifa Comfort.
    def click_button_comfort(self):
        #WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]')))
        self.driver.find_element(*self.locators.button_comfort).click()

    def verify_click_button_comfort(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'r-sw-label')))
        return self.driver.find_element(*self.locators.verify_comfort).text

#3. Rellenar el número de teléfono.
    def click_button_phone_number(self):
        self.driver.find_element(*self.locators.button_phone_number).click()

    def click_phone_number_field(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[1]/form/div[1]/div')))
        self.driver.find_element(*self.locators.phone_number_field).click()

    def set_phone_number_field(self):
        self.driver.find_element(*self.locators.id_phone_field).send_keys(data.phone_number)

    def get_phone_number_field(self):
        return self.driver.find_element(*self.locators.id_phone_field).get_property('value')

    def click_button_following(self):
        self.driver.find_element(*self.locators.button_following).click()

    def set_code_sms_field(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'code')))
        self.driver.find_element(*self.locators.code_sms_field).send_keys(helpers.retrieve_phone_code(driver=self.driver))

    def click_button_confirm(self):
        self.driver.find_element(*self.locators.button_confirm).click()

    def verify_phone_number_field(self):
        return self.driver.find_element(*self.locators.button_phone_number).text

 #4. Agregar una tarjeta de crédito.
    def click_payment_method(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'pp-button.filled')))
        self.driver.find_element(*self.locators.payment_method).click()

    def click_add_card(self):
        self.driver.find_element(*self.locators.add_card).click()

    def click_number_card_field(self):
        self.driver.find_element(*self.locators.number_card_field).click()

    def set_number_card_field(self):
        self.driver.find_element(*self.locators.text_number_card_field).send_keys(data.card_number)

    def get_number_card_field(self):
        return self.driver.find_element(*self.locators.text_number_card_field).get_property('value')

    def click_code_card_field(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'card-code-input')))
        self.driver.find_element(*self.locators.code_card_field).click()

    def set_code_card_field(self):
        self.driver.find_element(*self.locators.text_code_card_field).send_keys(data.card_code)

    def get_code_card_field(self):
        return self.driver.find_element(*self.locators.text_code_card_field).get_property('value')

    def click_body_credit_card(self):
        self.driver.find_element(*self.locators.body_credit_card).click()

    def click_button_add(self):
        self.driver.find_element(*self.locators.button_add).click()

    def click_button_x(self):
        self.driver.find_element(*self.locators.button_x).click()

    def verify_button_card_name(self):
        return self.driver.find_element(*self.locators.button_card_name).text

#5. Escribir un mensaje para el controlador.
    def click_message_for_driver_field(self):
        self.driver.find_element(*self.locators.message_for_driver_field).click()

    def set_message_for_driver_field(self):
        self.driver.find_element(*self.locators.text_message_for_driver_field).send_keys(data.message_for_driver)

    def get_message_for_driver_field(self):
        return self.driver.find_element(*self.locators.text_message_for_driver_field).get_property('value')

#6. Pedir una manta y pañuelos.
    def click_blanket_scarves_field(self):
        self.driver.find_element(*self.locators.blanket_scarves_field).click()

#7. Pedir 2 helados
    def click_add_ice_cream(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]')))
        self.driver.find_element(*self.locators.add_ice_cream).click()

    def verify_twice_click_ice_cream(self):
        return self.driver.find_element(*self.locators.verify_twice_ice_cream).text

#8. Aparece el modal para buscar un taxi.
    def click_button_looking_for_taxi(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.smart-button')))
        self.driver.find_element(*self.locators.button_looking_for_taxi).click()

#9. Esperar a que aparezca la información del conductor en el modal (opcional).
    def wait_window_waiting_taxi(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div[text()="Detalles"]')))
        return self.driver.find_element(By.XPATH, '//div[text()="Detalles"]').text

