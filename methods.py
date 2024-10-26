import helpers
import data
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Se cambió el nombre de la clase por UrbanRoutesPage y se agregaron los localizadores en el archivo métodos, además se modificaron los localizadores xpath.

class UrbanRoutesPage:

    def __init__(self, driver):
        self.driver = driver

    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    button_get_a_cab = (By.CLASS_NAME, 'button.round')
    button_comfort = (By.XPATH, '//*[@class="tcard-icon"]/img[@alt="Comfort"]')
    verify_comfort = (By.CLASS_NAME, 'r-sw-label')
    button_phone_number = (By.CLASS_NAME, 'np-text')
    phone_number_field = (By.CLASS_NAME, 'input-container')
    id_phone_field = (By.ID, 'phone')
    button_following = (By.CLASS_NAME, 'button.full')
    code_sms_field = (By.ID, 'code')
    button_confirm = (By.XPATH, '//*[text()="Confirmar"]')
    payment_method = (By.CLASS_NAME, 'pp-button.filled')
    add_card = (By.CLASS_NAME, 'pp-row.disabled')
    number_card_field = (By.CLASS_NAME, 'card-number-input')
    text_number_card_field = (By.ID, 'number')
    code_card_field = (By.CLASS_NAME, 'card-code-input')
    text_code_card_field = (By.NAME, 'code')
    body_credit_card = (By.CLASS_NAME, 'card-wrapper')
    button_add = (By.XPATH, '//*[text()="Agregar"]')
    button_x = (By.XPATH, '//div[@class="payment-picker open"]/div[@class="modal"]/div[@class="section active"]/button[@class="close-button section-close"]')
    button_card_name = (By.CLASS_NAME, 'pp-value-text')
    message_for_driver_field = (By.XPATH, '//*[text()="Mensaje para el conductor..."]')
    text_message_for_driver_field = (By.ID, 'comment')
    blanket_scarves_field = (By.XPATH, '//span[@class="slider round"]')
    add_ice_cream = (By.XPATH, '//div[@class="counter-plus"]')
    verify_twice_ice_cream = (By.XPATH, '//div[@class="counter-value"]')
    button_looking_for_taxi = (By.CSS_SELECTOR, '.smart-button')
    window_waiting_taxi = (By.CLASS_NAME, 'order-body')

#1. Configurar la dirección
    def click_from_field(self):
        self.driver.find_element(*self.from_field).click()

    def set_from_field(self):
        self.driver.find_element(*self.from_field).send_keys(data.address_from)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def click_to_field(self):
        self.driver.find_element(*self.to_field).click()

    def set_to_field(self):
        self.driver.find_element(*self.to_field).send_keys(data.address_to)

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def click_button_get_a_cab(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME,'button.round')))
        self.driver.find_element(*self.button_get_a_cab).click()

#2. Seleccionar la tarifa Comfort.
    def click_button_comfort(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@class="tcard-icon"]/img[@alt="Comfort"]')))
        self.driver.find_element(*self.button_comfort).click()

    def verify_click_button_comfort(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'r-sw-label')))
        return self.driver.find_element(*self.verify_comfort).text

#3. Rellenar el número de teléfono.
    def click_button_phone_number(self):
        self.driver.find_element(*self.button_phone_number).click()

    def click_phone_number_field(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'input-container')))
        self.driver.find_element(*self.phone_number_field).click()

    def set_phone_number_field(self):
        self.driver.find_element(*self.id_phone_field).send_keys(data.phone_number)

    def get_phone_number_field(self):
        return self.driver.find_element(*self.id_phone_field).get_property('value')

    def click_button_following(self):
        self.driver.find_element(*self.button_following).click()

    def set_code_sms_field(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'code')))
        self.driver.find_element(*self.code_sms_field).send_keys(helpers.retrieve_phone_code(driver=self.driver))

    def click_button_confirm(self):
        self.driver.find_element(*self.button_confirm).click()

    def verify_phone_number_field(self):
        return self.driver.find_element(*self.button_phone_number).text

 #4. Agregar una tarjeta de crédito.
    def click_payment_method(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'pp-button.filled')))
        self.driver.find_element(*self.payment_method).click()

    def click_add_card(self):
        self.driver.find_element(*self.add_card).click()

    def click_number_card_field(self):
        self.driver.find_element(*self.number_card_field).click()

    def set_number_card_field(self):
        self.driver.find_element(*self.text_number_card_field).send_keys(data.card_number)

    def get_number_card_field(self):
        return self.driver.find_element(*self.text_number_card_field).get_property('value')

    def click_code_card_field(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'card-code-input')))
        self.driver.find_element(*self.code_card_field).click()

    def set_code_card_field(self):
        self.driver.find_element(*self.text_code_card_field).send_keys(data.card_code)

    def get_code_card_field(self):
        return self.driver.find_element(*self.text_code_card_field).get_property('value')

    def click_body_credit_card(self):
        self.driver.find_element(*self.body_credit_card).click()

    def click_button_add(self):
        self.driver.find_element(*self.button_add).click()

    def click_button_x(self):
        self.driver.find_element(*self.button_x).click()

    def verify_button_card_name(self):
        return self.driver.find_element(*self.button_card_name).text

#5. Escribir un mensaje para el controlador.
    def click_message_for_driver_field(self):
        self.driver.find_element(*self.message_for_driver_field).click()

    def set_message_for_driver_field(self):
        self.driver.find_element(*self.text_message_for_driver_field).send_keys(data.message_for_driver)

    def get_message_for_driver_field(self):
        return self.driver.find_element(*self.text_message_for_driver_field).get_property('value')

#6. Pedir una manta y pañuelos.
    def click_blanket_scarves_field(self):
        self.driver.find_element(*self.blanket_scarves_field).click()

    def verify_click_blanket_scarves_field(self):
        return self.driver.find_element(*self.blanket_scarves_field).is_displayed()

#7. Pedir 2 helados
    def click_add_ice_cream(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div[@class="counter-plus"]')))
        self.driver.find_element(*self.add_ice_cream).click()

    def verify_twice_click_ice_cream(self):
        return self.driver.find_element(*self.verify_twice_ice_cream).text

#8. Aparece el modal para buscar un taxi.
    def click_button_looking_for_taxi(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.smart-button')))
        self.driver.find_element(*self.button_looking_for_taxi).click()

#9. Esperar a que aparezca la información del conductor en el modal (opcional).
    def wait_window_waiting_taxi(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div[text()="Detalles"]')))
        return self.driver.find_element(By.XPATH, '//div[text()="Detalles"]').text

