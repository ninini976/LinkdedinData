# from pyvirtualdisplay import Display
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
import time
# display = Display(visible=0, size=(1024, 768))
# display.start()

driver = webdriver.Firefox()

driver.get("https://www.linkedin.com/")
time.sleep(1)
email = driver.find_element_by_id('login-email')
email.send_keys("yangtony@umich.edu")
time.sleep(1)
password = driver.find_element_by_id('login-password')
password.send_keys("nnsshxsssnnrbt")

password.send_keys(Keys.RETURN)

mainsearchbox = driver.find_element_by_id('main-search-box')
mainsearchbox.send_keys("jinlei chen")
time.sleep(2)
mainsearchbox.send_keys(Keys.ARROW_DOWN)
mainsearchbox.send_keys(Keys.RETURN)

bgedu = driver.find_element_by_id('background-education')
text_edu = bgedu.text
print(text_edu)

time.sleep(1)

bgexp = driver.find_element_by_id('background-experience')
text_exp = bgexp.text
print(text_exp)


time.sleep(3)


driver.quit()
# display.stop()