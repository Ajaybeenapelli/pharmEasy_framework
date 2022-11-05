import time
from Library.excel_lib import ReadExcel
from Library.config import Config


class labtests:
    read_xl = ReadExcel()
    parm_locators = read_xl.read_locator(Config.labtest_locators_sheet)

    def __init__(self, driver):
        self.driver = driver

    def lab_tests(self):
        locators = self.parm_locators['Lab_tests_']
        self.driver.find_element(*locators).click()
        time.sleep(5)

    def All_tests(self):
        locators = self.parm_locators['All_tests_']
        self.driver.find_element(*locators).click()
        self.driver.implicitly_wait(10)

    def Select_lab_test(self):
        locators = self.parm_locators['select_test_']
        self.driver.find_element(*locators).click()
        time.sleep(2)

    def select(self):
        locators = self.parm_locators['select_btn']
        self.driver.find_element(*locators).click()

    def Add_patients(self):
        locators = self.parm_locators['add_patients_count_']
        self.driver.find_element(*locators).click()

    def click_Add_patient_details_btn(self):
        locators = self.parm_locators['add_patient_details']
        self.driver.find_element(*locators).click()
        time.sleep(2)

    def Enter_mobile_nmbr(self, mobile_nmbr):
        if isinstance(mobile_nmbr, float):
            mobile_nmbr = str(int(mobile_nmbr))
        assert len(mobile_nmbr) == 10
        locators = self.parm_locators['mble_nmbr_']
        self.driver.find_element(*locators).send_keys(mobile_nmbr)

    def click_continue_btn(self):
        locators = self.parm_locators['click_continue_btn_']
        self.driver.find_element(*locators).click()
        time.sleep(30)

    def click_continue_btn_(self):
        locators = self.parm_locators['click_continue_btn_']
        self.driver.find_element(*locators).click()
        time.sleep(10)

    def patient_details(self):
        locators = self.parm_locators['click_patient_dtls_btn']
        self.driver.find_element(*locators).click()

    def patient_details_(self):
        locators = self.parm_locators['click_patient_dtls_']
        self.driver.find_element(*locators).click()

    def entr_patient_name(self, p_name):
        locators = self.parm_locators['patient_name_']
        self.driver.find_element(*locators).send_keys(p_name)

    def entr_patient_age(self, age):
        if isinstance(age, float):
            age = str(int(age))
        assert len(age) == 2
        locators = self.parm_locators['age_']
        self.driver.find_element(*locators).send_keys(age)

    def select_gender(self):
        locators = self.parm_locators['gender_']
        self.driver.find_element(*locators).click()

    def click_Add_details_btn(self):
        locators = self.parm_locators['click_add_dtls_btn']
        self.driver.find_element(*locators).click()

    def add_new_adrs(self):
        locators = self.parm_locators['add_new_address']
        self.driver.find_element(*locators).click()

    def entr_Address_name(self, pName):
        locators = self.parm_locators['address_name']
        self.driver.find_element(*locators).send_keys(pName)

    def entr_pincode(self, pincode):
        if isinstance(pincode, float):
            pincode = str(int(pincode))
        assert len(pincode) == 6
        locators = self.parm_locators['pincode_']
        self.driver.find_element(*locators).send_keys(pincode)

    def entr_houseNo(self, H_No):
        if isinstance(H_No, float):
            H_No = int(H_No)
        locators = self.parm_locators['houseNo_']
        self.driver.find_element(*locators).send_keys(H_No)

    def entr_street_name(self, street):
        locators = self.parm_locators['street_name_']
        self.driver.find_element(*locators).send_keys(street)
        time.sleep(2)

    def select_address_type(self):
        locators = self.parm_locators['address_type']
        self.driver.find_element(*locators).click()
        time.sleep(2)

    def click_save_btn(self):
        locators = self.parm_locators['click_save_btn']
        self.driver.find_element(*locators).click()

    def click_slot_continue(self):
        locators = self.parm_locators['slot_continue']
        self.driver.find_element(*locators).click()