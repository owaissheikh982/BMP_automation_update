import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import constent
import datetime
import csv
import traceback
import random

random_number = random.randint(1, 99)

def log_step(test_case, step, status, message=""):
    """Log steps into a CSV file"""
    with open("CRM_log.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            test_case, step, status, message
        ])

def fill_field(wait, locator_type, locator, value, test_case, step_name):
    """Common function to fill form fields with logging and error handling"""
    try:
        element = wait.until(EC.presence_of_element_located((locator_type, locator)))
        element.send_keys(value)
        log_step(test_case, step_name, "PASS")
    except Exception as e:
        log_step(test_case, step_name, "FAIL", traceback.format_exc())

def drop_down(wait, locator_type, locator,value, test_case, step_name):
    """Common function to fill form fields with logging and error handling"""
    try:
        wait.until(EC.element_to_be_clickable((locator_type, locator))).click()
        wait.until(EC.element_to_be_clickable((locator_type, value))).click()
        log_step(test_case, step_name, "PASS")
    
    except Exception as e:
        log_step(test_case, step_name, "FAIL", traceback.format_exc())


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def test_login_valid(self):
        driver = self.driver
        wait = self.wait
        test_case = "Lead Creation"

        # ========== STEP 1: Open Website ==========
        try:
            driver.get(constent.WEB_URL)
            log_step(test_case, "Open Website", "PASS")
        except Exception as e:
            log_step(test_case, "Open Website", "FAIL", traceback.format_exc())
            self.fail(f"Failed at Open Website: {e}")

        # ========== STEP 2: Login ==========
        try:
            wait.until(EC.presence_of_element_located((By.NAME, constent.EMAIL_NAME))
                        ).send_keys(constent.EMAIL)
            driver.find_element(By.NAME, constent.PASSWORD_NAME).send_keys(constent.PASSWORD)
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, constent.LOGIN_SUBMIT_BUTTON_XPATH))).click()
            log_step(test_case, "Login", "PASS")
        
        except Exception as e:
            log_step(test_case, "Login", "FAIL", traceback.format_exc())
            self.fail(f"Failed at Login: {e}")

        # ========== STEP 3: Navigate to CRM ==========
        try:
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, constent.CRM_BUTT0N))).click()
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, constent.LEAD_BUTTON))).click()
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, constent.ADD_LEADS_BUTTON))).click()
            log_step(test_case, "Navigate To Leads", "PASS")
        except Exception as e:
            log_step(test_case, "Navigate To Leads", "FAIL", traceback.format_exc())
            self.fail(f"Failed at Navigate To Leads: {e}")

       
        # ========== STEP 4: Enter Leads Detail ==========
        drop_down(wait,By.XPATH,"//label[normalize-space()='Lead Owner']/parent::div//input","//div[text()='owais sheikh (tapanew768@bitfami.com)']",test_case,"Select Lead Owner")
        drop_down(wait,By.XPATH,"//label[normalize-space()='Assigned To']/parent::div//input","//div[text()='owais sheikh (tapanew768@bitfami.com)']",test_case,"Select Lead Owner")
        fill_field(wait,By.XPATH,constent.UPLOAD_PROFILE,r"C:\Users\Awais\Pictures\image\profile\profilegirl.jpg",test_case, "Upload Profile Image")
        fill_field(wait,By.NAME,constent.MODEL_NAME,f"Models {random_number}",test_case, "Upload Models")
        fill_field(wait,By.NAME,constent.MODEL_AR_NAME,f"Model AR {random_number}",test_case, "Upload Model_AR")

        # ========== STEP 4: Select Brand ==========
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, constent.SELECT_BRAND))).click()
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//div[text()='Fiat']"))).click()
            
            
            log_step(test_case, "Select Brand", "PASS")
        except Exception as e:
            log_step(test_case, "Select Brand", "FAIL", traceback.format_exc())
            self.fail(f"Failed at Select Brand: {e}")  

      

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
    with open("CRM_log.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if file.tell() == 0:  # agar file empty hai to header likho
            writer.writerow(["Timestamp", "Test Case", "Step", "Status", "Message"])

    unittest.main()
