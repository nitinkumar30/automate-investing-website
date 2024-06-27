import time
from telnetlib import EC

from selenium.webdriver.chrome import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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


def windowSize(x, y):
    driver.set_window_size(x, y)


def maximiseWindow():
    driver.maximize_window()


def userInput(xpath, value):
    time.sleep(5)
    driver.find_element(By.XPATH, xpath).send_keys(value)
    return True


def clickElement(xpath):
    time.sleep(2)
    if WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.XPATH, xpath))
    ):
        driver.find_element(By.XPATH, xpath).click()
    return True


def takeScreenshot(filename):
    driver.save_screenshot('screenshot/' + filename + '.png')
    return True


def checkEnabled(xpath):
    if driver.find_element(By.XPATH, xpath).is_enabled():
        return True
    else:
        return False


def checkPresence(xpath):
    if driver.find_element(By.XPATH, xpath).is_displayed():
        return True
    else:
        return False


def extractOTPfromMailBody(mailBody):
    otp = ''.join(c for c in mailBody if c.isdigit())
    print("Verification Code:", otp)
    return otp

