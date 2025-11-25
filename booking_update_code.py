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
import random
import time

if constent.EMAIL == "kagodad145@wivstore.com":

    random_customer = [

        "Customer 38 owais (test_20251117155216@example.com)",
        "Customer 79 owais (test_20251117161251@example.com)",
        "Customer 22 owais (test_20251117161415@example.com)",
        "Customer 48 owais (test_20251119120412@example.com)",
        "Customer 76 owais (test_20251119115844@example.com)",
        "Customer 88 owais (test_20251119115652@example.com)"
       
        ]

else:

    random_customer = [

        "Ehsab haq (sitereview2024@gmail.com)",
        "Rashed Al Mansoori (rashed.mansoori@emiratesmail.ae)",
        "Adeel Khan (adeel.khan87@gmail.com)",
        "Sana Qureshi (sana.qureshi22@hotmail.com)",
        "owais ss (sazn2000@gmail.co)",
        "Muhammad Hassan Raza (mhassanrazas@gmail.com)"
        

        ]
selected_customer = random.choice(random_customer)
if constent.EMAIL == "kagodad145@wivstore.com":
    random_cars = [

        "Mercedes-Benz GLC 300 4MATIC AMG Line",
        "Volkswagen Tiguan 2.0 TSI R-Line 4Motion",
        "Dacia Duster 1.3 TCe Prestige",
        "Subaru Forester 2.5i Premium AWD",
        "Skoda Octavia 1.6 TDI Ambition"
        ]
else:
    random_cars = [

        # "Skoda Octavia 1.6 TDI Ambition",
        # "Subaru Forester 2.5i Premium AWD",
        # "Dacia Duster 1.3 TCe Prestige",
        # "Honda Civic EX",
        # "Mercedes-Benz C",
        # "Mercedes-Benz E-Class E350",
        # "Dodge Charger R/T",
        # "Toyota Corolla Altis",
        # "Toyota RAV4 Adventure",
        # "Toyota Land Cruiser Prado",
        # "Hyundai Elantra Sport",
        # "Vauxhall Corsa SE",
        # "Mini Cooper S",
        # "Land Rover Defender P300",
        # "Suzuki Swift GLX",
        # "Suzuki Vitara GL+"
        "Mercedes-Benz C",
        "Vauxhall Corsa SE"

    ]

selected_cars = random.choice(random_cars)


def log_step(test_case, step, status, message=""):
    """Log steps into a CSV file"""
    with open("Booking_log.csv", mode="a", newline="", encoding="utf-8") as file:
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


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def test_login_valid(self):
        driver = self.driver
        wait = self.wait
        test_case = "Booking Creation"

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

        # ========== STEP 3: Navigate to Booking ==========
        try:
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, constent.BOOKING_BUTT0N))).click()
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, constent.ADD_BOOKING_BUTTON))).click()
            log_step(test_case, "Navigate to Booking", "PASS")
        except Exception as e:
            log_step(test_case, "Navigate to booking", "FAIL", traceback.format_exc())
            self.fail(f"Failed at Navigate to booking: {e}")

        # ========== STEP 4: Select Customer ==========
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, constent.SELECT_CUSTOMER))).click()
            time.sleep(5)
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, f"//div[text()='{selected_customer}']"))).click()
            log_step(test_case, "Select Customer", "PASS")
        except Exception as e:
            log_step(test_case, "Select Customer", "FAIL", traceback.format_exc())
            self.fail(f"Failed at Select Customer: {e}")    

        # ========== STEP 4:Select Vehicle ==========
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, constent.SELECT_VEHICLE))).click()
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, f"//div[text()='{selected_cars}']"))).click()
            log_step(test_case, "Select Vehicle", "PASS")
        except Exception as e:
            log_step(test_case, "Select vehicle", "FAIL", traceback.format_exc())
            self.fail(f"Failed at Select vehicle: {e}")    
        
        try:
            

            log_step(test_case, "Select Vehicle", "PASS")
        except Exception as e:
            log_step(test_case, "Select vehicle", "FAIL", traceback.format_exc())
            self.fail(f"Failed at Select vehicle: {e}")    
        
        
        

        # ========== STEP 4: Select Fuel Value ==========
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, constent.SELECT_FUEL_LEVEL))).click()
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//div[text()='Half Tank']"))).click()
            
            
            log_step(test_case, "Fuel Value", "PASS")
        except Exception as e:
            log_step(test_case, "Fuel Value", "FAIL", traceback.format_exc())
            self.fail(f"Failed at Fuel Value: {e}")  

        # ========== STEP 4: Exterior Condition ==========
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, constent.EXTERIOR_CONDITION))).click()
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//div[text()='Few Dents']"))).click()
            
            
            log_step(test_case, "Exterior Condition", "PASS")
        except Exception as e:
            log_step(test_case, "Exterior Condition", "FAIL", traceback.format_exc())
            self.fail(f"Failed at Exterior Condition: {e}")  
    
        # ========== STEP 4: Interior Condition ==========
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, constent.INTERIOR_CONDITION))).click()
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//div[text()='Excellent']"))).click()
            
            log_step(test_case, "Interior Condition", "PASS")
        except Exception as e:
            log_step(test_case, "Interior Condition", "FAIL", traceback.format_exc())
            self.fail(f"Failed at Interior Condition: {e}")  

        # ========== STEP 4: Tyre Condition ==========
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, constent.TYRE_CONDITION))).click()
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//div[text()='Excellent']"))).click()
            
            
            log_step(test_case, "Tyre Condition", "PASS")
        except Exception as e:
            log_step(test_case, "Tyre Condition", "FAIL", traceback.format_exc())
            self.fail(f"Failed at Tyre Condition: {e}")  
      
        # ========== STEP 4: Spare Tyre ==========
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, constent.SPARE_TYRE))).click()
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//div[text()='Yes']"))).click()
            
            
            log_step(test_case, "Spare Tyre", "PASS")
        except Exception as e:
            log_step(test_case, "Spare Tyre", "FAIL", traceback.format_exc())
            self.fail(f"Failed at Spare Tyre: {e}")  
      
        # ========== STEP 4: Toolkit ==========
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, constent.TOOLKIT))).click()
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//div[text()='Yes']"))).click()
            
            
            log_step(test_case, "ToolKit", "PASS")
        except Exception as e:
            log_step(test_case, "ToolKit", "FAIL", traceback.format_exc())
            self.fail(f"Failed at ToolKit: {e}")  

        # ========== STEP 5: Mileage At Pickup ==========

        fill_field(wait,By.XPATH,constent.MILEAGE_PICKUP,"123",test_case, "Mileage At Pickup")

        # ========== STEP 5: Mileage Limit ==========

        fill_field(wait,By.XPATH,constent.MILEAGE_LIMIT,"123",test_case, "Mileage limit")
      
        # ========== STEP 4: Pickup time ==========
        try:
            pickup_time = wait.until(
             EC.element_to_be_clickable((By.XPATH, "//label[normalize-space(text())='Pickup Time']/preceding-sibling::div//input")))
            pickup_time.click()
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='25']"))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space(text())='Pickup Time']/ancestor::div[contains(@class,'group')]//button[normalize-space(text())='Apply']"))).click()

            log_step(test_case, "Pickup Time", "PASS")

        except Exception as e:
            log_step(test_case, "Pickup Time", "FAIL", traceback.format_exc())
    
            time.sleep(2)
        
        # ========== STEP 4: Return time ==========
        try:
            return_time = wait.until(
             EC.element_to_be_clickable((By.XPATH, "//label[normalize-space(text())='Return Time']/preceding-sibling::div//input")))
            return_time.click()
            wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[text()='26'])[2]"))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space(text())='Return Time']/ancestor::div[contains(@class,'group')]//button[normalize-space(text())='Apply']"))).click()
            log_step(test_case, "Return Time", "PASS")

        except Exception as e:
            log_step(test_case, "Return Time", "FAIL", traceback.format_exc())

        # ========== STEP 6: PickUp Location ==========
        fill_field(wait,By.XPATH,constent.PICKUP_LOCATION,"Al Qasba Canal, Sharjah, UAE",test_case, "Enter PickUp Location")

        # ========== STEP 7: DropOff Location ==========
        fill_field(wait,By.XPATH,constent.DROP_OFF_LOCATION,"Al Nahda Street, Sharjah",test_case, "Enter dropOff Location")

        # ========== STEP 28: Confirm Booking ==========
        try:
            confirm_booking = wait.until(
             EC.element_to_be_clickable((By.XPATH, constent.CONFIRM_BOOKING)))
            confirm_booking.click()
            log_step(test_case, "Confirm Booking", "PASS")
        except Exception as e:
            log_step(test_case, "Confirm Booking", "FAIL", traceback.format_exc())


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

    
        time.sleep(4)
        fill_field(wait,By.XPATH,constent.UPLOAD_PROFILE,r"C:\Users\Awais\Pictures\image\profile\profilegirl.jpg",test_case, "Upload Receipt Image")

        # fill_field(wait,By.XPATH,constent.UPLOAD_PROFILE,r"C:\Users\Awais\Pictures\image\profile\profilegirl.jpg",test_case, "Upload Receipt Image")
        fill_field(wait,By.NAME,constent.TRANSACTION_NAME,"1112345678",test_case, "Upload Transaction ID")
        fill_field(wait,By.NAME,constent.TERMINAL_NAME,"123456",test_case, "Enter Terminal ID")
        fill_field(wait,By.NAME,constent.RECEIPT_NAME,"12345678",test_case, "Enter Receipt No")
        fill_field(wait,By.NAME,constent.PAYMENT_NOTE_NAME,"A well-maintained Honda Civic 2021",test_case, "Upload Payment Note")
        fill_field(wait,By.NAME,constent.CUSTOMER_NOTE_NAME,"A well-maintained Honda Civic 2021",test_case, "Upload Customer Note")
        time.sleep(4)

        # ========== STEP 29: Submit Form ==========
        try:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, constent.FORM_SUBMIT)))

            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            time.sleep(1)

            element.click()
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
    with open("Booking_log.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if file.tell() == 0:  # agar file empty hai to header likho
            writer.writerow(["Timestamp", "Test Case", "Step", "Status", "Message"])

    unittest.main()
