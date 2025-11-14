
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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


def fill_field(wait, locator_type, locator, value, test_case, step_name):
    """Common function to fill form fields with logging and error handling"""
    try:
        element = wait.until(EC.presence_of_element_located((locator_type, locator)))
        element.send_keys(value)
        log_step(test_case, step_name, "PASS")
    except Exception as e:
        log_step(test_case, step_name, "FAIL", traceback.format_exc())

def drop_down(wait, locator_type1, locator1,locator_type2,locator2, test_case, step_name):
    """Common function to fill form fields with logging and error handling"""
    try:
        wait.until(EC.element_to_be_clickable((locator_type1, locator1))).click()
        wait.until(EC.element_to_be_clickable((locator_type2, locator2))).click()
        log_step(test_case, step_name, "PASS")
    
    except Exception as e:
        log_step(test_case, step_name, "FAIL", traceback.format_exc())