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
import os


# ================= LOGGING FUNCTION =================
def log_step(test_case, step, status, message=""):
    """Log steps into a CSV file"""
    with open("test_log.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            test_case, step, status, message
        ])


# ================= COMMON FILL FUNCTION =================
def fill_field(wait, locator_type, locator, value, test_case, step_name):
    """Common function to fill form fields with logging and error handling"""
    try:
        element = wait.until(EC.presence_of_element_located((locator_type, locator)))
        element.send_keys(value)
        log_step(test_case, step_name, "PASS")
    except Exception as e:
        log_step(test_case, step_name, "FAIL", traceback.format_exc())


# ================= MAIN TEST CLASS =================
class AffiliateFormTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

        # Create screenshots folder if not exist
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")

    # ========== VALIDATION FUNCTION ==========
    def check_validation(self, field_name, expected_msg, xpath):
        """Helper to check validation message"""
        try:
            element = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            error_msg = element.text.strip()
            assert expected_msg in error_msg, f"Expected '{expected_msg}', got '{error_msg}'"
            log_step("Validation", f"{field_name}", "PASS", error_msg)
        except AssertionError as ae:
            screenshot_name = f"screenshots/{field_name}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            self.driver.save_screenshot(screenshot_name)
            log_step("Validation", f"{field_name}", "FAIL", f"{ae} | Screenshot: {screenshot_name}")
        except Exception as e:
            screenshot_name = f"screenshots/{field_name}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            self.driver.save_screenshot(screenshot_name)
            log_step("Validation", f"{field_name}", "FAIL", f"{e} | Screenshot: {screenshot_name}")

    # ========== MAIN TEST CASE ==========
    def test_affiliate_form(self):
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
            wait.until(EC.presence_of_element_located((By.NAME, constent.EMAIL_NAME))).send_keys(constent.EMAIL)
            driver.find_element(By.NAME, constent.PASSWORD_NAME).send_keys(constent.PASSWORD)
            wait.until(EC.element_to_be_clickable((By.XPATH, constent.LOGIN_SUBMIT_BUTTON_XPATH))).click()
            log_step(test_case, "Login", "PASS")
        except Exception as e:
            log_step(test_case, "Login", "FAIL", traceback.format_exc())
            self.fail(f"Failed at Login: {e}")

        # ========== STEP 3: Navigate to Affiliate ==========
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, constent.AFFILIATE_BUTT0N))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, constent.ADD_AFFILIATE_BUTTON))).click()
            log_step(test_case, "Navigate to Affiliate", "PASS")
        except Exception as e:
            log_step(test_case, "Navigate to Affiliate", "FAIL", traceback.format_exc())
            self.fail(f"Failed at Navigate to Affiliate: {e}")

        # ========== STEP 4: Upload Profile ==========
        fill_field(wait, By.XPATH, constent.UPLOAD_PROFILE,
                   r"C:\Users\Awais\Pictures\image\profile\profilegirl.jpg", test_case, "Upload Profile Image")


        # ========== STEP 6: Submit Empty Form for Validation ==========
        try:
            submit_btn = wait.until(EC.element_to_be_clickable(
                (By.XPATH, constent.FORM_SUBMIT)))
            driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
            time.sleep(1) 
            submit_btn.click()
            log_step(test_case, "Submit Form", "PASS")
        except Exception as e:
            log_step(test_case, "Click Save", "FAIL", traceback.format_exc())

        # ========== STEP 7: Validate Required Field Messages ==========
        validations = [
            ("Proof of address", "Proof of address is required","//div[contains(text(),'Proof of address is required')]"),
            ("Insurance certificate", "Insurance certificate is required",
             "//div[contains(text(),'Insurance certificate is required')]"),
            ("Bank account verification", "Bank account verification document is required",
             "//div[contains(text(),'Bank account verification document is required')]"),
            ("First name", "First name is required",
             "//div[contains(text(),'First name is required')]"),
            ("Last name", "Last name is required",
             "//div[contains(text(),'Last name is required')]"),
            ("Phone number", "Phone number is required","//div[contains(text(),'Phone number is required')]"),
            ("Email Address", "Invalid email address","//div[contains(text(),'Invalid email address')]"),
            ("Country", "Country is required","//div[contains(text(),'Country is required')]"),
            ("City", "City/State is required","//div[contains(text(),'City/State is required')]"),
            ("Driving license", "Driving license number is required","//div[contains(text(),'Driving license number is required')]"),
            ("License Expiry Date", "Expected date, received null","//div[contains(text(),'Expected date, received null')]"),
            ("National ID/Passport", "National ID/Passport is required","//div[contains(text(),'National ID/Passport is required')]"),
            ("ID Expiry Date", "Expected date, received null","//div[contains(text(),'Expected date, received null')]"),
        ]

        for field_name, expected_msg, xpath in validations:
            self.check_validation(field_name, expected_msg, xpath)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
