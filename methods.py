import time
from telnetlib import EC

from selenium.webdriver.chrome import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import xpaths


# from demo_new import driver


def webdriver_initialize():
    opt = webdriver.ChromeOptions()
    opt.add_argument("--start-maximized")
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome(options=opt)
    return driver


driver = webdriver_initialize()


def getUrl(URL):
    return driver.get(URL)


def userInput(xpath, value):
    time.sleep(5)
    return driver.find_element(By.XPATH, xpath).send_keys(value)


def clickElement(xpath):
    time.sleep(5)
    if WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.XPATH, xpath))
    ):
        return driver.find_element(By.XPATH, xpath).click()


def takeScreenshot(filename):
    return driver.save_screenshot('screenshot/' + filename + '.png')


def extractOTPfromMailBody(mailBody):
    otp = ''.join(c for c in mailBody if c.isdigit())
    print("Verification Code:", otp)
    return otp


# ---------------------------


from tempmail import EMail

email = EMail()


def mail_address(email):
    return email.address  # qwerty123@1secmail.com


# ... request some email ...

def getMessage(email):
    msg = email.wait_for_message()
    print("Subject of the ", msg.subject)
    print("Body of the ", msg.body)

    # ------- Getting messages in that mail

    email = EMail(msg.body)
    inbox = email.get_inbox()

    for msg_info in inbox:
        print(msg_info.subject, msg_info.message.body)

        numbers = ''.join(c for c in msg_info.message.body if c.isdigit())
        print("Verification Code:", numbers)
        return numbers

    # ------ Splitting otp from whole of message
