import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import cons.constent as constent
import datetime
import csv
import traceback


def log_step(test_case, step, status, message=""):
    """Log steps into a CSV file"""
    with open("test_log.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            test_case, step, status, message
        ])



class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def test_login_valid(self):
        driver = self.driver
        wait = self.wait
        test_case = "Affiliate Creation"

        # ========== STEP 1: Open Website ==========
        try:
            driver.get(constent.WEB_URL)
            log_step(test_case, "Open Website", "PASS")
        except Exception as e:
            log_step(test_case, "Open Website", "FAIL", traceback.format_exc())
            self.fail(f"Failed at Open Website: {e}")

        # ========== STEP 2: Login ==========
        try:
            if constent.EMAIL == "tapanew768@bitfami.com" and constent.PASSWORD=="Awais1234@":
                wait.until(EC.presence_of_element_located((By.NAME, constent.EMAIL_NAME))
                        ).send_keys(constent.EMAIL)
                driver.find_element(By.NAME, constent.PASSWORD_NAME).send_keys(constent.PASSWORD)
                wait.until(EC.element_to_be_clickable(
                    (By.XPATH, constent.LOGIN_SUBMIT_BUTTON_XPATH))).click()
                log_step(test_case, "Login", "PASS")
            else :
                log_step(test_case, "Login", "FAIL")

        except Exception as e:
            log_step(test_case, "Login", "FAIL", traceback.format_exc())
            self.fail(f"Failed at Login: {e}")

        # ========== STEP 3: Navigate to Affiliate ==========
        try:
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, constent.AFFILIATE_BUTT0N))).click()
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, constent.ADD_AFFILIATE_BUTTON))).click()
            log_step(test_case, "Navigate to Affiliate", "PASS")
        except Exception as e:
            log_step(test_case, "Navigate to Affiliate", "FAIL", traceback.format_exc())
            self.fail(f"Failed at Navigate to Affiliate: {e}")

        # ========== STEP 4: Upload Profile ==========
        try:
            uploadimage = wait.until(
                EC.presence_of_element_located((By.XPATH, constent.UPLOAD_PROFILE)))
            uploadimage.send_keys(r"C:\Users\Awais\Pictures\image\profile\profilegirl.jpg")
            log_step(test_case, "Upload Profile Image", "PASS")
        except Exception as e:
            log_step(test_case, "Upload Profile Image", "FAIL", traceback.format_exc())
            self.fail(f"Failed at Upload Profile Image: {e}")

        # ========== STEP 4: Upload Address ==========
        try:
            uploadaddress = wait.until(
                EC.presence_of_element_located((By.XPATH, constent.PROF_ADDRESS)))
            uploadaddress.send_keys(r"C:\Users\Awais\Pictures\image\profile\profilegirl.jpg")
            log_step(test_case, "Upload Address", "PASS")
        except Exception as e:
            log_step(test_case, "Upload Address", "FAIL", traceback.format_exc())
            self.fail(f"Failed at Upload Address: {e}")

        # ========== STEP 4: Upload Insurance Certificate ==========
        try:
            ins_cer = wait.until(
                EC.presence_of_element_located((By.XPATH, constent.INS_CERTIFICATE)))
            ins_cer.send_keys(r"C:\Users\Awais\Pictures\image\profile\profilegirl.jpg")
            
            log_step(test_case, "Upload Insurance Certificate", "PASS")
        except Exception as e:
            log_step(test_case, "Upload Insurance Certificate", "FAIL", traceback.format_exc())
            self.fail(f"Failed at Upload AddrInsurance Certificateess: {e}")

        # ========== STEP 4: Upload Bank Verification ==========
        try:
            bank_verf = wait.until(
                EC.presence_of_element_located((By.XPATH, constent.BANK_VER)))
            bank_verf.send_keys(r"C:\Users\Awais\Pictures\image\profile\profilegirl.jpg")
            # bank_verf.send_keys("")
            log_step(test_case, "Upload Bank Verification", "PASS")
        except Exception as e:
            log_step(test_case, "Upload Bank Verification", "FAIL", traceback.format_exc())
            self.fail(f"Failed at Upload Bank Verification: {e}")

        # ========== STEP 5: First Name ==========
        try:
            f_name = wait.until(
                EC.presence_of_element_located((By.NAME, constent.FIRST_NAME)))
            f_name.send_keys(constent.FIRST_KEY)
            log_step(test_case, "Enter First Name", "PASS")
        except Exception as e:
            log_step(test_case, "Enter First Name", "FAIL", traceback.format_exc())

        # ========== STEP 6: Last Name ==========
        try:
            l_name = wait.until(
                EC.presence_of_element_located((By.NAME, constent.LAST_NAME)))
            l_name.send_keys(constent.LAST_KEY)
            log_step(test_case, "Enter Last Name", "PASS")
        except Exception as e:
            log_step(test_case, "Enter Last Name", "FAIL", traceback.format_exc())

        # ========== STEP 7: Phone ==========
        try:
            p_num = wait.until(
                EC.presence_of_element_located((By.NAME, constent.PHONE_NO)))
            p_num.send_keys(constent.PHONE_NO_KEY)
            log_step(test_case, "Enter Phone Number", "PASS")
        except Exception as e:
            log_step(test_case, "Enter Phone Number", "FAIL", traceback.format_exc())

        # ========== STEP 8: Email (Unique) ==========
        try:
            unique_email = f"test_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}@example.com"
            email = wait.until(
                EC.presence_of_element_located((By.NAME, constent.EMAIL_NAME)))
            email.send_keys(unique_email)
            log_step(test_case, "Enter Email", "PASS")
        except Exception as e:
            log_step(test_case, "Enter Email", "FAIL", traceback.format_exc())

        # ========== STEP 9: Country & City ==========
        try:
            wait.until(EC.element_to_be_clickable((By.NAME, "country_id"))).click()
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//div[text()='United Arab Emirates']"))).click()
            time.sleep(5)
            wait.until(EC.element_to_be_clickable((By.NAME, "city_id"))).click()
            wait.until(EC.presence_of_element_located(
                (By.XPATH, "//div[text()='Abu Dhabi']"))).click()
            log_step(test_case, "Select Country & City", "PASS")
        except Exception as e:
            log_step(test_case, "Select Country & City", "FAIL", traceback.format_exc())

        # ========== STEP 10: Driving License ==========
        try:
            dri_lic = wait.until(
                EC.presence_of_element_located((By.NAME, constent.DRVING_LIC)))
            dri_lic.send_keys(constent.DRVING_LIC_KEY)
            log_step(test_case, "Enter Driving License", "PASS")
        except Exception as e:
            log_step(test_case, "Enter Driving License", "FAIL", traceback.format_exc())

        # ========== STEP 11: Driving License Expiry ==========
        try:
            calendar_driv = wait.until(
             EC.element_to_be_clickable((By.XPATH, "//label[text()='Driving License Expiry Date']/..//input")))
            calendar_driv.click()
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='5']"))).click()
            log_step(test_case, "Enter Driving License Expiry", "PASS")
        except Exception as e:
            log_step(test_case, "Enter Driving License Expiry", "FAIL", traceback.format_exc())

        
        # ========== STEP 12: CNIC No. ==========
        try:
            nic = wait.until(
                EC.presence_of_element_located((By.NAME, constent.CNIC)))
            nic.send_keys(constent.CNIC_KEY )
            log_step(test_case, "Enter CNIC No.", "PASS")
        except Exception as e:
            log_step(test_case, "Enter CNIC No.", "FAIL", traceback.format_exc())

        # ========== STEP 13: CNIC Expiry ==========
        try:
            calendar_cnic = wait.until(
             EC.element_to_be_clickable((By.XPATH, "//label[text()='National ID / Passport Expiry Date']/..//input")))
            calendar_cnic.click()
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='5']"))).click()
            log_step(test_case, "Enter CNIC Expiry", "PASS")
        except Exception as e:
            log_step(test_case, "Enter CNIC Expiry", "FAIL", traceback.format_exc())

        # ========== STEP 14: Business Address ==========
        try:
            bus_add = wait.until(
             EC.presence_of_element_located((By.NAME, constent.BUS_ADD)))
            bus_add.send_keys(constent.BUS_ADD_KEY )
            log_step(test_case, "Enter Business Address", "PASS")
        except Exception as e:
            log_step(test_case, "Enter Business Address", "FAIL", traceback.format_exc())

        # ========== STEP 15: Mailing Address ==========
        try:
            mail_add = wait.until(
             EC.presence_of_element_located((By.NAME, constent.MAIL_ADD)))
            mail_add.send_keys(constent.MAIL_ADD_KEY )
            log_step(test_case, "Enter Mailing Address", "PASS")
        except Exception as e:
            log_step(test_case, "Enter Mailing Address", "FAIL", traceback.format_exc())

        # ========== STEP 16: Type Of Affiliate ==========
        try:
            wait.until(EC.element_to_be_clickable((By.NAME, "type_id"))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='2-5 Cars']"))).click()
            log_step(test_case, "Enter Type Of Affiliate", "PASS")
        except Exception as e:
            log_step(test_case, "Enter Type Of Affiliate", "FAIL", traceback.format_exc())

        # ========== STEP 17: Affiliate Vehicles ==========
        try:
            aff_veh = wait.until(
             EC.presence_of_element_located((By.NAME, constent.AFF_VEH)))
            aff_veh.send_keys(constent.AFF_VEH_KEY )
            log_step(test_case, "Enter Affiliate Vehicles", "PASS")
        except Exception as e:
            log_step(test_case, "Enter Affiliate Vehicles", "FAIL", traceback.format_exc())

        # ========== STEP 18: Comission Type ==========
        try:
            wait.until(EC.element_to_be_clickable((By.NAME, "comission_type_id"))).click()
            wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Percentage']"))).click()
            log_step(test_case, "Enter Comission Type", "PASS")
        except Exception as e:
            log_step(test_case, "Enter Comission Type", "FAIL", traceback.format_exc())

        # ========== STEP 19: Select Currency ==========
        try:
            wait.until(EC.element_to_be_clickable((By.NAME, "currency_id"))).click()
            wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='AED']"))).click()
            log_step(test_case, "Select Currency", "PASS")
        except Exception as e:
            log_step(test_case, "Select Currency", "FAIL", traceback.format_exc())
        
        # ========== STEP 20: Enter Bank Name ==========
        try:
            bank_name = wait.until(
             EC.presence_of_element_located((By.NAME, constent.BANK_NAME)))
            bank_name.send_keys(constent.BANK_NAME_KEY)
            log_step(test_case, "Enter Bank Name", "PASS")
        except Exception as e:
            log_step(test_case, "Enter Bank Name", "FAIL", traceback.format_exc())

        
        # ========== STEP 21: Enter Account Title ==========
        try:
            acc_title = wait.until(
             EC.presence_of_element_located((By.NAME, constent.ACC_HOLDER)))
            acc_title.send_keys(constent.ACC_HOLDER_KEY)
            log_step(test_case, "Enter Account Title", "PASS")
        except Exception as e:
            log_step(test_case, "Enter Account Title", "FAIL", traceback.format_exc())

        
        # ========== STEP 22: Enter IBAN No. ==========
        try:
            acc_iban = wait.until(
             EC.presence_of_element_located((By.NAME, constent.ACC_IBAN)))
            acc_iban.send_keys(constent.ACC_IBAN_KEY)
            log_step(test_case, "Enter IBAN No.", "PASS")
        except Exception as e:
            log_step(test_case, "Enter IBAN No.", "FAIL", traceback.format_exc())
        
        # ========== STEP 23: Enter SWIFT/BIC Code ==========
        try:
            bic = wait.until(
             EC.presence_of_element_located((By.NAME, constent.BIC)))
            bic.send_keys(constent.BIC_KEY)
            log_step(test_case, "Enter SWIFT/BIC Code", "PASS")
        except Exception as e:
            log_step(test_case, "Enter SWIFT/BIC Code", "FAIL", traceback.format_exc())
        
        # ========== STEP 24: Enter Payment Method ==========
        try:
            p_method = wait.until(
                EC.presence_of_element_located((By.NAME, constent.P_METHOD)))
            p_method.send_keys(constent.P_METHOD_KEY)
            log_step(test_case, "Enter Payment Method", "PASS")
        except Exception as e:
            log_step(test_case, "Enter Payment Method", "FAIL", traceback.format_exc())
        
        # ========== STEP 25: Enter Payment Terms ==========
        try:
            p_terms = wait.until(
                 EC.presence_of_element_located((By.NAME, constent.P_TERMS)))
            p_terms.send_keys(constent.P_TERMS_KEY)
            log_step(test_case, "Enter Payment Terms", "PASS")
        except Exception as e:
            log_step(test_case, "Enter Payment Terms", "FAIL", traceback.format_exc())

        
        # ========== STEP 26: Select Contract Start Date ==========
        try:
            calendar_c_start = wait.until(
             EC.element_to_be_clickable((By.XPATH, "//label[text()='Contract Start Date']/..//input")))
            calendar_c_start.click()
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='5']"))).click()
            log_step(test_case, "Select Contract Start Date", "PASS")
        except Exception as e:
            log_step(test_case, "Select Contract Start Date", "FAIL", traceback.format_exc())
        
        # ========== STEP 27: Select Contract End Date ==========
        try:
            calendar_c_end = wait.until(
             EC.element_to_be_clickable((By.XPATH, "//label[text()='Contract End Date']/..//input")))
            calendar_c_end.click()
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='20']"))).click()
            log_step(test_case, "Select Contract End Date", "PASS")
        except Exception as e:
            log_step(test_case, "Select Contract End Date", "FAIL", traceback.format_exc())

        
        # ========== STEP 28: Enter Note / Special Instruction ==========
        try:
            note = wait.until(
             EC.presence_of_element_located((By.NAME, constent.NOTE)))
            note.send_keys(constent.NOTE_KEY)
            log_step(test_case, "Note / Special Instruction", "PASS")
        except Exception as e:
            log_step(test_case, "Note / Special Instruction", "FAIL", traceback.format_exc())


        # ========== STEP 29: Submit Form ==========
        try:
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, constent.FORM_SUBMIT))).click()
            log_step(test_case, "Submit Form", "PASS")

            try:
                toast_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//*[@id='_rht_toaster']//div")))
                toast_text = toast_element.text
                print("Toast Message:", toast_text)
                log_step("Toast Message", "PASS", toast_text.strip())
            except Exception as e:
                log_step("Toast Message", "FAIL", f"No toast captured: {str(e)}")

        except Exception as e:
            log_step(test_case, "Submit Form", "FAIL", traceback.format_exc())
            self.fail(f"Failed at Submit Form: {e}")

    

        
        
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    # Create CSV header if not exists
    with open("test_log.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if file.tell() == 0:  # agar file empty hai to header likho
            writer.writerow(["Timestamp", "Test Case", "Step", "Status", "Message"])

    unittest.main()
