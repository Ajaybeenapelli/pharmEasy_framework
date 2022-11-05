import pytest
from Library.excel_lib import ReadExcel
from POM.labtests import labtests
from Library.config import Config
import datetime


class Testlabtests:
    read_xl =ReadExcel()
    data = read_xl.read_testdata(Config.labtest_testdata_sheet)

    @pytest.mark.parametrize("mobile_nmbr, p_name, age, pName, pincode, H_No, street", data)
    def test_Lab_test(self, mobile_nmbr, p_name, age, pName, pincode, H_No, street, init_driver):
        driver = init_driver

        try:
            PE = labtests(driver)
            PE.lab_tests()
            PE.All_tests()
            PE.Select_lab_test()
            PE.select()
            PE.Add_patients()
            PE.click_Add_patient_details_btn()
            PE.Enter_mobile_nmbr(mobile_nmbr)
            PE.click_continue_btn()
            PE.click_continue_btn_()
            PE.patient_details()
            PE.patient_details_()
            PE.entr_patient_name(p_name)
            PE.entr_patient_age(age)
            PE.select_gender()
            PE.click_Add_details_btn()
            PE.add_new_adrs()
            PE.entr_Address_name(pName)
            PE.entr_pincode(pincode)
            PE.entr_houseNo(H_No)
            PE.entr_street_name(street)
            PE.select_address_type()
            PE.click_save_btn()
            PE.click_slot_continue()

        except AssertionError as error_msg:
            td = datetime.datetime.now()
            name = f'screenshots_{td.hour}_{td.minute}_{td.second}.png'
            driver.save_screenshot(Config.screenshots_path+ name)
            raise error_msg