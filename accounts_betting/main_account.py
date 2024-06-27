import time

from assets.methods import *
from assets.xpaths import *
from assets.variables import *


def do_bet(mail, pswd):
    # Open link
    getUrl(URL_login)

    # Do logging in
    userInput(xpath_inputMail, mail)
    userInput(xpath_inputPass, pswd)
    clickElement(xpath_btnLogin)
    takeScreenshot('login')

    windowSize(572, 1280)

    time.sleep(5)
    # if checkPresence(xpath_alertClose):
    #     print("Alert box present, needs to be closed now ...")
    #     clickElement(xpath_alertBoxClose)

    maximiseWindow()

    # Do necessary investment
    assert clickElement(xpath_tabMarketList), takeScreenshot('error')
    time.sleep(10)
    assert clickElement(xpath_teamSelected), takeScreenshot('error')
    # time.sleep(5)
    assert clickElement(xpath_placeOrder1_55), takeScreenshot('error')
    # time.sleep(5)
    assert clickElement(xpath_selectAll), takeScreenshot('error')
    takeScreenshot('putAllMoney')
    # time.sleep(5)
    assert clickElement(xpath_btnCnfrm), takeScreenshot('error')
    print("Confirm button clicked...")
    # time.sleep(5)
    if checkEnabled(xpath_btnClose):
        clickElement(xpath_btnClose)
        print("Ongoing Matches button...")
    time.sleep(5)
    print("<=========   TRANSACTION DONE   =========>")
    # driver.close()
