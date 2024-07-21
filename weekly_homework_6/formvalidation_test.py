import time
from weekly_homework_6.Configs.config import get_preconfigured_chrome_driver
from weekly_homework_6.page_model import FormvalidationTest


TEST_DATA = {
    "email": "yardy@yarr.com",
    "password": "123456",
    "confirmp": "123456",
    "customer": "2345643",
    "dealer": "0412",
    "randomfield": "twelve",
    "date format": "2024-04-05",
    "urlfield": "https://progmasters.hu/szoftvertesztelo-kepzes/",
    "randomtext": "csakegybeszoveglehkezeteknelkul",
    "card type": "Master Card",
    "card_number": "4445556664487945",
    "card_cvv": "5555",
    "exp_month": "April",
    "exp_year": "2025",
}

NEGATIV_TEST_DATA = {
    "email": "yardyyarr.com",
    "password": "123",
    "confirmp": "156",
    "customer": "",
    "dealer": "",
    "randomfield": "twelsa",
    "date format": "2024-04-05",
    "urlfield": "https://progmasters.hu/szoftvertesztelo-kepzes/",
    "randomtext": "csakegybeszoveglehetekezeteknelkul",
    "card type": "Master Card",
    "card_number": "4445556664487945",
    "card_cvv": "5555",
    "exp_month": "April",
    "exp_year": "2025",
    "errormsg_pass1": "Should be between 6 and 20 characters",
    "errormsg_pass2": "This field can't be empty",
    "errormsg_pass3": 'Should contain "twelve"',
    "errormsg_pass4": 'Should be a 4 character number'
}

#High-flayer-en lévő űrlap kitöltése.
class TestFormvalidation:

    def setup_method(self):
        page = FormvalidationTest(get_preconfigured_chrome_driver())
        self.page = page
        page.open()
    def teardown_method(self):
        self.page.close()

#Pozitív ágú tesztelés:
    def test_signup(self):

        self.page.email_input().send_keys(TEST_DATA["email"])
        self.page.password_input().send_keys(TEST_DATA['password'])
        self.page.password_confirm_input().send_keys(TEST_DATA['confirmp'])
        self.page.customer_number_input().send_keys(TEST_DATA['customer'])
        self.page.dealer_number_input().send_keys(TEST_DATA['dealer'])
        self.page.random_input_input().send_keys(TEST_DATA['randomfield'])
        self.page.date_input().send_keys(TEST_DATA['date format'])
        self.page.urlfiel_input().send_keys([TEST_DATA['urlfield']])
        self.page.random_textarea_input().send_keys([TEST_DATA['randomtext']])
        self.page.card_type_select().send_keys(TEST_DATA['card type'])
        self.page.card_number_input().send_keys(TEST_DATA['card_number'])
        self.page.card_cvv().send_keys([TEST_DATA['card_cvv']])
        self.page.exp_month().send_keys(TEST_DATA['exp_month'])
        self.page.exp_year().send_keys(TEST_DATA['exp_year'])
        self.page.single_checkbox().click()
        self.page.receive_email_yes().click()
        self.page.agree_terms_cb().click()
        self.page.agree_more().click()
        #Elvárás, hogy kattintható legyen a sign up gomb.
        assert self.page.signup_btn().is_enabled()
        #E-mail cím validálása:
        assert self.page.is_valid_email(), f'The email {TEST_DATA["email"]} is not valid.'
        #Mezők végi pipa validálása:
        assert self.page.email_valid() == 'true'
        assert self.page.password_valid() == 'true'
        assert self.page.password_confirm_valid() == 'true'
        assert self.page.customer_number_valid() == 'true'
        assert self.page.dealer_num_valid() == 'true'

#Negatív ágú tesztelés:
    def test_negative_signup(self):
        self.page.email_input().send_keys(NEGATIV_TEST_DATA["email"])
        self.page.password_input().send_keys(NEGATIV_TEST_DATA['password'])
        self.page.password_confirm_input().send_keys(NEGATIV_TEST_DATA['confirmp'])
        self.page.customer_number_input().send_keys(NEGATIV_TEST_DATA['customer'])
        self.page.dealer_number_input().send_keys(NEGATIV_TEST_DATA['dealer'])
        self.page.random_input_input().send_keys(NEGATIV_TEST_DATA['randomfield'])
        self.page.date_input().send_keys(NEGATIV_TEST_DATA['date format'])
        self.page.urlfiel_input().send_keys([NEGATIV_TEST_DATA['urlfield']])

        assert self.page.incorrect_password() == NEGATIV_TEST_DATA["errormsg_pass1"] or NEGATIV_TEST_DATA["errormsg_pass2"]
        assert self.page.incorrect_pass_conf() == "Please complete Desired Password"
        assert self.page.incorrect_customer() == NEGATIV_TEST_DATA['errormsg_pass2']
        assert self.page.incorrect_dealer() == NEGATIV_TEST_DATA['errormsg_pass2'] or NEGATIV_TEST_DATA["errormsg_pass4"]
        assert self.page.incorrect_random() == NEGATIV_TEST_DATA['errormsg_pass3']







