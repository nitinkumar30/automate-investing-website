from accounts_betting.main_account import *
import datetime

# Do bet in all the following accounts
do_bet(main_mail, main_pswd)
do_bet(frnd1_mail, frnd1_pswd)

# Prints current date and time
print(datetime.datetime.now())
driver.close()
 