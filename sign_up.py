from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

#Define the function
def test_signup_popup(driver):
    driver.get("https://softwaretestingv1.praesignis.com/softwaretestingv1/Sign_Up_Page.html")
    time.sleep(3)
#Test Case 001: Fill in name, email and password with correct details
    #driver.find_element(By.ID, "name").send_keys("Katharina")
    #driver.find_element(By.ID, "email").send_keys("kathi_hoelzl@gmx.at")
    #driver.find_element(By.ID, "password").send_keys("123AbC!!!")
#Test Case 002: Invalid email address
    #driver.find_element(By.ID, "name").send_keys("Katharina")
    #driver.find_element(By.ID, "email").send_keys("kathi_hoelzlgmx.at")
    #driver.find_element(By.ID, "password").send_keys("123AbC!!!")
#Test Case 003: Invalid name with numbers
    #driver.find_element(By.ID, "name").send_keys("Kath123")
    #driver.find_element(By.ID, "email").send_keys("kathi_hoelzl@gmx.at")
    #driver.find_element(By.ID, "password").send_keys("123AbC!!!")
#Test Case 003: Invalid password
    #driver.find_element(By.ID, "name").send_keys("Katharina")
    #driver.find_element(By.ID, "email").send_keys("kathi_hoelzl@gmx.at")
    #driver.find_element(By.ID, "password").send_keys("123ma")
#Test Case 004: All empty fields
    #driver.find_element(By.ID, "name").send_keys("")
    #driver.find_element(By.ID, "email").send_keys("")
    #driver.find_element(By.ID, "password").send_keys("")
#Test Case 005: Missing name
    #driver.find_element(By.ID, "name").send_keys("")
    #driver.find_element(By.ID, "email").send_keys("kathi_hoelz@gmx.at")
    #driver.find_element(By.ID, "password").send_keys("abC123!")
#Test Case 006: Username has number
    #driver.find_element(By.ID, "name").send_keys("123Ksath")
    #driver.find_element(By.ID, "email").send_keys("kathi_hoelz@gmx.at")
    #driver.find_element(By.ID, "password").send_keys("abC123!")
#Test Case 007: Weak password
    driver.find_element(By.ID, "name").send_keys("Katharina")
    driver.find_element(By.ID, "email").send_keys("kathi_hoelz@gmx.at")
    driver.find_element(By.ID, "password").send_keys("qwrtzuiopas")
#Submitting the form by clicking the sign up button
    driver.find_element(By.XPATH, "//form[@id='signupForm']//button[text()='Sign Up']").click()
    time.sleep(3)
#Verify the popup
    popup = driver.find_element(By.ID, "promo-popup")
    popup_message = driver.find_element(By.ID, "promo-popup-message").text


    assert popup.is_displayed(), "Sign-Up popup did not display."
    assert "success" in popup_message.lower(), f"Unexpected message: {popup_message}"

    print("Sign-Up popup test passed on", driver.name)

#Run the test
chrome_driver = webdriver.Chrome()
test_signup_popup(chrome_driver)
chrome_driver.quit()