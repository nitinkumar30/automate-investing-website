from methods import *
from xpaths import *
from variables import *

# Open link
getUrl(URL_login)

# Logging in
userInput(xpath_inputMail, frnd1_mail)
userInput(xpath_inputPass, frnd1_pswd)
clickElement(xpath_btnLogin)
takeScreenshot('login')

time.sleep(5)

# Do investment
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
