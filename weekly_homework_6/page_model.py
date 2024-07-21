from weekly_homework_6.Configs.general_model import GeneralPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from email_validator import validate_email, EmailNotValidError

class FormvalidationTest(GeneralPage):

    def __init__(self,browser):
        super().__init__(browser,"https://high-flyer.hu/selenium/simplevalidation.html")

    def email_input(self):
        return self.browser.find_element(By.ID,'test-email')

    def email_valid(self):
        return self.browser.find_element(By.ID, 'test-email').get_attribute('data-jsv-field-isvalid')

    def password_input(self):
        return self.browser.find_elements(By.XPATH, '//input[@type="password"]')[0]

    def password_valid(self):
        return self.browser.find_elements(By.XPATH, '//input[@type="password"]')[0].get_attribute('data-jsv-field'
                                                                                                  '-isvalid')

    def password_confirm_input(self):
        return self.browser.find_element(By.ID,'test-confirm-password')

    def password_confirm_valid(self):
        return self.browser.find_element(By.ID,'test-confirm-password').get_attribute('data-jsv-field-isvalid')

    def customer_number_input(self):
        return self.browser.find_element(By.ID,'test-customer-number')

    def customer_number_valid(self):
        return self.browser.find_element(By.ID,'test-customer-number').get_attribute('data-jsv-field-isvalid')

    def dealer_number_input(self):
        return self.browser.find_element(By.ID,'test-dealer-number')

    def dealer_num_valid(self):
        return self.browser.find_element(By.ID, 'test-dealer-number').get_attribute('data-jsv-field-isvalid')

    def random_input_input(self):
        return self.browser.find_element(By.ID,'test-random-field')

    def date_input(self):
        return self.browser.find_element(By.ID,'test-date-field')

    def urlfiel_input(self):
        return self.browser.find_element(By.ID,'test-url-field')

    def random_textarea_input(self):
        return self.browser.find_element(By.ID,'test-random-textarea')

    def card_type_select(self):
        return self.browser.find_element(By.ID,'test-card-type')

    def card_number_input(self):
        return self.browser.find_element(By.NAME,'cardNumber')

    def card_cvv(self):
        return self.browser.find_element(By.NAME,'cardCvv')

    def exp_month(self):
        return self.browser.find_element(By.ID,'test-card-month')

    def exp_year(self):
        return self.browser.find_element(By.ID,'test-card-year')

    def single_checkbox(self):
        return self.browser.find_element(By.ID,'test-single-checkbox')

    def receive_email_yes(self):
        return self.browser.find_element(By.ID,'test-save-email-yes')

    def receive_email_no(self):
        return self.browser.find_element(By.ID,'test-save-email-no')

    def agree_terms_cb(self):
        return self.browser.find_element(By.NAME,'terms')

    def agree_more(self):
        return self.browser.find_element(By.XPATH,'//input[@value="more"]')

    def signup_btn(self):
        return WebDriverWait(self.browser,5).until(EC.element_to_be_clickable((By.ID,'test-button')))


    def correct_email(self):
        return self.browser.find_element(By.ID,'test-email').get_attribute('value')

    def is_valid_email(self):
        try:
            validate_email(self.correct_email())
            return True
        except EmailNotValidError:
            return False

    def pipa(self):
        return self.browser.find_element(By.ID,'w-iqdjmnf8').get_attribute('value')

#Negatív ág:

    def incorrect_password(self):
        ip = WebDriverWait(self.browser,10).until(EC.visibility_of_any_elements_located((By.XPATH,'//div[@class="validate-field-error-message"]')))
        return ip[1].text


    def incorrect_pass_conf(self):
        ipc = WebDriverWait(self.browser, 10).until(EC.visibility_of_any_elements_located((By.XPATH, '//div[@class="validate-field-error-message"]')))
        return ipc[2].text

    def incorrect_customer(self):
        ic = WebDriverWait(self.browser, 10).until(EC.visibility_of_any_elements_located((By.XPATH, '//div[@class="validate-field-error-message"]')))
        return ic[3].text

    def incorrect_dealer(self):
        ic = WebDriverWait(self.browser, 10).until(EC.visibility_of_any_elements_located((By.XPATH, '//div[@class="validate-field-error-message"]')))
        return ic[4].text
    def incorrect_random(self):
        ic = WebDriverWait(self.browser, 10).until(EC.visibility_of_any_elements_located((By.XPATH, '//div[@class="validate-field-error-message"]')))
        return ic[5].text



