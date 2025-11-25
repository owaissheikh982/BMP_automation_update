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


random_cars = [

    "Honda Civic EX",
    "Mercedes-Benz C",
    "Mercedes-Benz E-Class E350",
    "Dodge Charger R/T",
    "Toyota Corolla Altis",
    "Toyota RAV4 Adventure",
    # "Toyota Land Cruiser Prado",
    "Hyundai Elantra Sport",
    "Vauxhall Corsa SE",
    "Mini Cooper S",
    "Land Rover Defender P300",
    "Suzuki Swift GLX",
    "Suzuki Vitara GL+"
]
selected_cars = random.choice(random_cars)
random_number = random.randint(1, 99)

def log_step(test_case, step, status, message=""):
    """Log steps into a CSV file"""
    with open("Rentify_log.csv", mode="a", newline="", encoding="utf-8") as file:
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
        test_case = "Vehicles Add"

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

        # ========== STEP 3: Navigate to Vehicles ==========
        try:
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, constent.RENTIFY_BUTT0N))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, constent.VEHICLES_BUTTON))).click()
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, constent.ADD_VEHICLES_BUTTON))).click()
            log_step(test_case, "Navigate to Vehicles", "PASS")
        except Exception as e:
            log_step(test_case, "Navigate to Vehicles", "FAIL", traceback.format_exc())
            self.fail(f"Failed at Navigate to Vehicles: {e}")


          # ========== STEP 4: Enter Brand Detail ==========
        fill_field(wait,By.XPATH,constent.UPLOAD_PROFILE,r"C:\Users\Awais\Pictures\image\profile\profilegirl.jpg",test_case, "Upload Vehicles Image")
        fill_field(wait,By.XPATH,constent.PROF_ADDRESS,r"C:\Users\Awais\Pictures\image\profile\profilegirl.jpg",test_case, "Upload Vehicles Thumb Image")
        fill_field(wait,By.XPATH,constent.INS_CERTIFICATE,r"C:\Users\Awais\Downloads\CRM_Buzinessify.docx ",test_case, "Upload Reg_Doc")
        fill_field(wait,By.NAME,constent.BRAND_NAME,selected_cars,test_case, "Upload Car Name")
        fill_field(wait,By.NAME,constent.BRAND_AR_NAME,selected_cars,test_case, "Upload Car Name_AR")

        # ========== STEP 4: Select Brand ==========
        try:
            wait.until(EC.element_to_be_clickable((By.NAME, constent.V_BRAND_NAME))).click()
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, f"//div[text()='Skoda']"))).click()
            log_step(test_case, "Select Brand", "PASS")
        except Exception as e:
            log_step(test_case, "Select Brand", "FAIL", traceback.format_exc())
            self.fail(f"Failed at Select Brand: {e}")    

        # ========== STEP 4: Select Model ==========
        try:
            wait.until(EC.element_to_be_clickable((By.NAME, constent.V_MODEL_NAME))).click()
            time.sleep(3)
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, f"//div[text()='Skoda Fabia']"))).click()
            log_step(test_case, "Select Model", "PASS")
        except Exception as e:
            log_step(test_case, "Select Model", "FAIL", traceback.format_exc())
            self.fail(f"Failed at Select Model: {e}")    

        # ========== STEP 4: Select Variant ==========
        try:
            wait.until(EC.element_to_be_clickable((By.NAME, constent.V_VARIANT_NAME))).click()
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, f"//div[text()='Skoda Fabia Monte Carlo']"))).click()
            log_step(test_case, "Select Variant", "PASS")
        except Exception as e:
            log_step(test_case, "Select Variant", "FAIL", traceback.format_exc())
            self.fail(f"Failed at Select Variant: {e}")   


        # ========== STEP 4: Select Vehicle Condition ==========
        try:
            wait.until(EC.element_to_be_clickable((By.NAME, constent.V_CONDITION_NAME))).click()
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, f"//div[text()='New']"))).click()
            log_step(test_case, "Select Vehicle Condition", "PASS")
        except Exception as e:
            log_step(test_case, "Select Vehicle Condition", "FAIL", traceback.format_exc())
            self.fail(f"Failed at Select Vehicle Condition: {e}")    

        # ========== STEP 4: Select Year ==========
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, constent.V_YEAR))).click()
            wait.until(EC.element_to_be_clickable(
                (By.XPATH,"//button[text()='2024']"))).click()
            log_step(test_case, "Select Year", "PASS")
        except Exception as e:
            log_step(test_case, "Select Year", "FAIL", traceback.format_exc())
            self.fail(f"Failed at Select Year: {e}")    

        
        # ========== STEP 4: Purchase Date ==========
        try:
            pickup_time = wait.until(
             EC.element_to_be_clickable((By.XPATH, "//label[normalize-space(text())='Car Purcahase Date']/preceding-sibling::div//input")))
            pickup_time.click()
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='1']"))).click()

            log_step(test_case, "Purchase Date", "PASS")

        except Exception as e:
            log_step(test_case, "Purchase Date", "FAIL", traceback.format_exc())
            
        fill_field(wait,By.NAME,constent.V_PURCHASE_PRICE,"450000",test_case, "Upload Purchase Price")
        fill_field(wait,By.NAME,constent.V_RENT_PRICE,"450",test_case, "Upload Rent Price")

        # ========== STEP 4:Select Transmission ==========
        try:
            wait.until(EC.element_to_be_clickable((By.NAME, constent.V_TRANSMISSION))).click()
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, f"//div[text()='Automatic']"))).click()
            log_step(test_case, "Select Transmission", "PASS")
        except Exception as e:
            log_step(test_case, "Select Transmission", "FAIL", traceback.format_exc())
            self.fail(f"Failed at Select Transmission: {e}")    
        

        # ========== STEP 4:Select Body Type ==========
        try:
            wait.until(EC.element_to_be_clickable((By.NAME, constent.V_BODY_TYPE))).click()
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, f"//div[text()='SUV']"))).click()
            log_step(test_case, "Select Body Type", "PASS")
        except Exception as e:
            log_step(test_case, "Select Body Type", "FAIL", traceback.format_exc())
            self.fail(f"Failed at Select Body Type: {e}")    
        
        fill_field(wait,By.NAME,constent.V_TOP_SPEED,"200",test_case, "Upload Top Speed")
        fill_field(wait,By.NAME,constent.V_ACCELERATION,"1.0",test_case, "Upload Acceleration")

        # ========== STEP 4:Select Number OF Seats ==========
        try:
            wait.until(EC.element_to_be_clickable((By.NAME, constent.V_SEATS))).click()
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, f"//div[text()='2 Seats']"))).click()
            log_step(test_case, "Select Number OF Seats", "PASS")
        except Exception as e:
            log_step(test_case, "Select Number OF Seats", "FAIL", traceback.format_exc())
            self.fail(f"Failed at Select Number OF Seats: {e}")    

        fill_field(wait,By.NAME,constent.V_FUEL_TANK,"70",test_case, "Fuel Tank Range")

        # ========== STEP 4: Select Fuel Type ==========
        try:
            wait.until(EC.element_to_be_clickable((By.NAME, constent.V_FUEL_TYPE))).click()
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//div[text()='Petrol']"))).click()
            
            
            log_step(test_case, "Fuel Type", "PASS")
        except Exception as e:
            log_step(test_case, "Fuel Type", "FAIL", traceback.format_exc())
            self.fail(f"Failed at Fuel Type: {e}")  

        fill_field(wait,By.NAME,constent.V_MILEAGE,"200",test_case, "ADD Mileage")

        # ========== STEP 4: Exterior Color ==========
        try:
            wait.until(EC.element_to_be_clickable((By.NAME, constent.V_EX_COLOR))).click()
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//div[text()='Blue']"))).click()
            
            log_step(test_case, "Exterior Color", "PASS")
        except Exception as e:
            log_step(test_case, "Exterior Color", "FAIL", traceback.format_exc())
            self.fail(f"Failed at Exterior Color: {e}")  
    
        # ========== STEP 4: Interior Color ==========
        try:
            wait.until(EC.element_to_be_clickable((By.NAME, constent.V_IN_COLOR))).click()
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//div[text()='Blue']"))).click()
            
            log_step(test_case, "Interior Color", "PASS")
        except Exception as e:
            log_step(test_case, "Interior Color", "FAIL", traceback.format_exc())
            self.fail(f"Failed at Interior Color: {e}")  

        fill_field(wait,By.NAME,constent.V_NUM_PLATE,"BKR-2334",test_case, "Add Number Plate")

        
        # ========== STEP 4: Fitness Date ==========
        try:
            pickup_time = wait.until(
             EC.element_to_be_clickable((By.XPATH, "//label[contains(text(), 'Fitness Renewal Date')]/preceding::input[1]")))
            pickup_time.click()
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='25']"))).click()

            log_step(test_case, "Fitness Date", "PASS")

        except Exception as e:
            log_step(test_case, "Fitness Date", "FAIL", traceback.format_exc())
        
        fill_field(wait,By.NAME,constent.V_HORSE_POWER,"200",test_case, "ADD Horse Power")


        # ========== STEP 4: Features ==========
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, constent.V_FEATURES))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Rear Armrest with Cup Holders']"))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Multi Function Steering Wheel']"))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Heated And Cooled Cup Holders']"))).click()
            
            
            log_step(test_case, "Features", "PASS")
        except Exception as e:
            log_step(test_case, "Features", "FAIL", traceback.format_exc())
            self.fail(f"Failed at Features: {e}")  
      
        # ========== STEP 4: Features On Home ==========
        # try:
        #     # wait.until(EC.element_to_be_clickable((By.XPATH, constent.V_FEATURES_HOME))).click()
        #     checkbox = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='checkbox' and @name='is_feature']")))
        #     driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
        #     time.sleep(1)
        #     checkbox.click()
           
        #     log_step(test_case, "Features On Home", "PASS")
        # except Exception as e:
        #     log_step(test_case, "Features On Home", "FAIL", traceback.format_exc())
        #     self.fail(f"Failed at Features On Home: {e}")  

        fill_field(wait,By.NAME,constent.V_INSURER_NAME,"DEMO",test_case, "ADD Insurer Name")
        
        
        # ========== STEP 4: Insurance Date ==========
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(), 'Insurance issue date')]/preceding::input[1]"))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='4']"))).click()

            log_step(test_case, "Insurance Date", "PASS")

        except Exception as e:
            log_step(test_case, "Insurance Date", "FAIL", traceback.format_exc())
        
        # ========== STEP 4: Insurance Expiry Date ==========
        try:
            pickup_time = wait.until(
             EC.element_to_be_clickable((By.XPATH, "//label[contains(text(), 'Insurance expiry date')]/preceding::input[1]")))
            pickup_time.click()
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='4']"))).click()

            log_step(test_case, "Insurance Expiry Date", "PASS")

        except Exception as e:
            log_step(test_case, "Insurance Expiry Date", "FAIL", traceback.format_exc())

        fill_field(wait,By.NAME,constent.V_PRE_PAYMENT,"123",test_case, "Pre-Payment")
        # fill_field(wait,By.XPATH,"//div[contains(@class,'ql-container')][1]","123",test_case, "Description")
        # fill_field(wait,By.XPATH,"//div[contains(@class,'ql-container')][2]","123",test_case, "Description_AR")
        
      
        # ========== STEP 29: Submit Form ==========
        try:
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, constent.FORM_SUBMIT))).click()
            log_step(test_case, "Submit Form", "PASS")
            time.sleep(10)    

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
    with open("Rentify_log.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if file.tell() == 0:  # agar file empty hai to header likho
            writer.writerow(["Timestamp", "Test Case", "Step", "Status", "Message"])

    unittest.main()
