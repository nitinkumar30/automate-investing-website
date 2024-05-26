from methods import *
from xpaths import *
from variables import *

# driver = webdriver_initialize()

# Open link
getUrl(URL_login)

# Do logging in
userInput(xpath_inputMail, main_mail)
userInput(xpath_inputPass, main_pswd)
clickElement(xpath_btnLogin)
takeScreenshot('login')

time.sleep(5)

# Do necessary investment
clickElement(xpath_tabMarketList)
time.sleep(20)
clickElement(xpath_teamSelected)
time.sleep(10)
clickElement(xpath_placeOrder1_55)
time.sleep(10)
clickElement(xpath_selectAll)
takeScreenshot('putAllMoney')
time.sleep(20)
clickElement(xpath_btnCnfrm)
print("Confirm button clicked...")
time.sleep(20)
clickElement(xpath_btnOngoingMatches)
print("Ongoing Matches button...")
time.sleep(20)

driver.close()
