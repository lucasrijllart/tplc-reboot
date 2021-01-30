import time
import sys

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

WAIT = 15

# start webdriver
driver_path = "/usr/bin/geckodriver"
print("Starting webdriver with executable:", driver_path)
options = Options()
options.headless = True
driver = webdriver.Firefox(executable_path=driver_path, options=options)
driver.set_window_size(1000, 1000)  # smaller can hide login button

# get TPLC page
tplc_ip = sys.argv[1] if len(sys.argv) >= 2 else "192.168.0.93"
print("Getting login page using IP:", tplc_ip)
driver.get(f"http://{tplc_ip}/")

# login
print("Writing password")
try:
    driver.find_element_by_id("pcPassword").send_keys("admin")
except NoSuchElementException:
    print("Could not find pcPassword element, this is generally because another browser is logged in")
    exit()
button_login = WebDriverWait(driver, WAIT).until(EC.element_to_be_clickable((By.ID, "loginBtn")))
button_login.click()
print("Clicked log in")

# reboot
WebDriverWait(driver, WAIT).until(EC.invisibility_of_element((By.CLASS_NAME, "loading-container-inner")))
print("Main page loaded, clicking reboot")
button_reboot = WebDriverWait(driver, WAIT).until(EC.element_to_be_clickable((By.ID, "top-control-reboot")))
button_reboot.click()
print("Clicked reboot, clicking yes")
button_ok = WebDriverWait(driver, WAIT).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-msg-ok")))
button_ok.click()
print("Reboot started")

# print progress from popup
progress_wait = 10  # seconds
print(f"Waiting {progress_wait} seconds")
time.sleep(progress_wait)
print("Progress:", driver.find_element_by_class_name("progressbar-percentage").text)

# reboot in progress, exit
print("Quitting")
driver.quit()
