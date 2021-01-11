import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:\\07. IT\\02. Software_testing\\01. To be installed\chromedriver.exe")
baseUrl = "http://www.demo.guru99.com/V4/"

class Login():

    def login_success(self):
        
        driver.get(baseUrl)

        username = driver.find_element(By.NAME, "uid")
        username.send_keys("mngr303505")

        password = driver.find_element(By.NAME, "password")
        password.send_keys("pydEtuj")

        button = driver.find_element(By.NAME, "btnLogin")
        button.click()

        time.sleep(5)

        actualTitle = driver.title
        if (actualTitle == "Guru99 Bank Manager HomePage"):
            print("Test Case Login PASSED")
        else:
            print("Test Case Login FAILED")


    def login_username_maxim_char(self):
        
        driver.get(baseUrl)

        username = driver.find_element(By.NAME, "uid")
        username.send_keys("mngr299418dadasdasdas")

        password = driver.find_element(By.NAME, "password")
        password.send_keys("EnYjAqa")

        button = driver.find_element(By.NAME, "btnLogin")
        button.click()

        time.sleep(5)

        actualTitle = driver.title
        if (actualTitle == "Guru99 Bank Manager HomePage"):
            print("Test Case Login MAX CHARACTERS PASS")
        else:
            print("Test Case Login MAX CHARACTERS FAILED")

    def login_NOK(self , usernameString, passwordString, testCase):
        
        driver.get(baseUrl)

        username = driver.find_element(By.NAME, "uid")
        username.send_keys(usernameString)

        password = driver.find_element(By.NAME, "password")
        password.send_keys(passwordString)

        button = driver.find_element(By.NAME, "btnLogin")
        button.click()

        time.sleep(5)

        actualTitle = None
        try:
            actualTitle = driver.title
        except:
            print("Test Case Login " + testCase + " PASSED")

        if actualTitle is not None:
            print("Test Case Login " + testCase + " FAILED")
        



test = Login()

test.login_success()
test.login_username_maxim_char()  

test.login_NOK("usernameNOK" , "EnYjAqa" , "wrong username and correct password" )
#test.login_NOK("mngr299418" , "dadadsadas", "correct username and wrong password" )
#test.login_NOK("userNOK" , "dadadsadas", "wrong username and wrong password" )
#test.login_NOK("" , "EnYjAqa", "empty username and correct password" )
#test.login_NOK("" , "passwordNOK", "empty username and wrong password" )
#test.login_NOK("mngr299418" , "", "correct username and empty password" )
#test.login_NOK("userNOK" , "", "wrong username and empty password" )



driver.quit()       

