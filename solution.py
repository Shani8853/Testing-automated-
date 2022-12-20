# importing necessary libraries for testing
# Selenium is used for testing
# selenium version 4 is used 
# Tested on Chrome  

from selenium import webdriver
import unittest
import time
from selenium.webdriver.support.select import Select
#from HTMLTestRunner import HTMLTestRunner
from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager    
from selenium.webdriver.common.by import By

# for removing warning 
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# creating a intance of chrome 
driver = webdriver.Chrome(options=options)

# linking the sparksfoundation website
driver.get('https://www.thesparksfoundationsingapore.org')
print("\n\n Checking for Testcases:\n\n")


# Testcase 1 : Title verification
print("Testcase 1: \n")
if (driver.title):
    print("Title verfication successfully done")
    print("Title is :\t", driver.title)
else:
    print("title verfication failed\n")


# Testcase 2 : Checking if Home Button working or not
print("\nTestcase 2 : \n")
try:
    # The sparks foundation is in text and we can simply access it using partial link text as it is a hyperlink  
    driver.find_element(By.PARTIAL_LINK_TEXT,"The Sparks Foundation").click()
    print("Home link works:\n")
except Exception as arg:
    print("The Exception is : \t ",arg)
    print("Home Link Doesn't Work! \n")


# Testcase 3 : Check if navigation bar appears
print("Testcase 3 : \n")
try:
    # navbar is a class name and thus we are using classname 
    driver.find_element(By.CLASS_NAME, "navbar")
    print("Navbar verification successfully done\n")
except Exception as arg:
    print("The Exception is : \t ",arg)
    print("Navbar verification failed! \n")


# testcase 4 : About us page working or not
print("Testcase 4 :\n")
try:
    # link text is similar to partial link text both are used when we want to access text hyperlink from webpage
    driver.find_element(By.LINK_TEXT,"About Us").click()
    time.sleep(4)
    driver.find_element(By.LINK_TEXT,"Vision, Mission and Values").click()
    time.sleep(4)
    driver.find_element(By.LINK_TEXT,"Guiding Principles").click()
    time.sleep(4)
    driver.find_element(By.LINK_TEXT,"Advisors and Patrons").click()
    time.sleep(4)
    driver.find_element(By.LINK_TEXT,"Executive Team").click()
    time.sleep(4)    
    driver.find_element(By.LINK_TEXT,"Corporate Partners").click()
    time.sleep(4)  
    # This link is not working on website shows not ready  
    # driver.find_element(By.LINK_TEXT,"Expert Mentors").click()
    # time.sleep(4)
    driver.find_element(By.PARTIAL_LINK_TEXT,"News").click()
    time.sleep(4)
    print("Pages visited successfully")
except Exception as arg:
    print("The exception is:\t",arg)
    print("Page visit failed! \n")
    time.sleep(3)


# testcase 5 : policies and code
print("TestCase 5 :\n")
try:
    driver.find_element(By.LINK_TEXT,"Policies and Code").click()
    time.sleep(4)
    driver.find_element(By.LINK_TEXT,"Policies").click()
    time.sleep(4)
    driver.find_element(By.LINK_TEXT,"Code of Ethics and Conduct").click()
    time.sleep(4)    
    driver.find_element(By.LINK_TEXT,"Personal Data Policy").click()
    time.sleep(4)    
    driver.find_element(By.LINK_TEXT,"Whistle Blowing Policy").click()
    time.sleep(4)
    driver.find_element(By.LINK_TEXT,"Service Quality Values").click()
    time.sleep(4)
    print("Policy page exists. Success!\n")
except  Exception as arg:
    print("The exception is:\t",arg)
    print("Policy page didn't load properly")


# Testcase 6 : Programs page
print("Testcase 6 :\n")
try:
    driver.find_element(By.LINK_TEXT,"Programs").click()
    time.sleep(4)
    driver.find_element(By.LINK_TEXT,"Student Scholarship Program").click()
    time.sleep(4)
    driver.find_element(By.LINK_TEXT,"Student Mentorship Program").click()
    time.sleep(4)
    driver.find_element(By.LINK_TEXT,"Student SOS Program").click()
    time.sleep(4)
    driver.find_element(By.LINK_TEXT,"Workshops").click()
    time.sleep(4)
    driver.find_element(By.LINK_TEXT,"Corporate Programs").click()
    time.sleep(4)
    print("Programs page verified!\n")
except Exception as arg:
    print("The exception is:\t",arg)


# Testcase 7 : Links Page
print("Testcase 7 :\n")
try:
    driver.find_element(By.LINK_TEXT,"LINKS").click()
    time.sleep(4)
    driver.find_element(By.LINK_TEXT,"Software & App").click()
    time.sleep(4)
    driver.find_element(By.LINK_TEXT,"Salient Features").click()
    time.sleep(4)
    driver.find_element(By.LINK_TEXT,"AI in Education").click()
    time.sleep(4)
    print("LINKS Verification successful!\n")
except Exception as arg:
    print("The exception is:\t",arg)
    print("LINKS Verification Failed")


# Testcase 8 Check if logo exists   
print("Testcase 8 : \n")
try:
    driver.find_element(By.XPATH,'//*[@id="home"]/div/div[1]/h1/a/*').click()
    print("Found logo! Success! \n")
    time.sleep(4)
except Exception as arg:
    print("The exception is:\t",arg)
    print("No logo found")


# Testcase 9 Check the form
print("Testcase 9 : \n")
try:
    driver.find_element(By.PARTIAL_LINK_TEXT,'Join Us').click()
    time.sleep(4)
    driver.find_element(By.PARTIAL_LINK_TEXT,'Why Join Us').click()
    time.sleep(4)
    driver.find_element(By.NAME,'Name').send_keys("Ritesh Singh")
    time.sleep(4)
    driver.find_element(By.NAME,"Email").send_keys("singh.ritesh2580@gmail.com")
    time.sleep(4)
    select = Select(driver.find_element(By.CLASS_NAME,"form-control"))
    time.sleep(4)
    select.select_by_visible_text("Student")
    time.sleep(4)
    driver.find_element(By.CLASS_NAME,"button-w3layouts").click()
    time.sleep(4)
    print("Form verification successful! \n")
except Exception as arg:
    print("The exception is:\t",arg)
    print("Form verification failed! \n")


# Testcase 10 : Check the contact us page 
print("Testcase 10 :\n")
try:
    driver.find_element(By.LINK_TEXT,"Contact Us").click()
    time.sleep(4)
    info = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/div[2]/p[2]")
    time.sleep(4)

    if (info.text == "+65-8402-8590, info@thesparksfoundation.sg"):
        print("Contact Information Correct!")
    else:
        print("Contact Information Incorrect")
except Exception as arg:
    print("The exception is:\t",arg)
    print("Contact page verification unsuccessful!")