# from pyvirtualdisplay import Display
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
# display = Display(visible=0, size=(1024, 768))
# display.start()


class education(object):
	"""education class contain the schoolName, degree, fieldOfStudy and date of an education record"""
	def __init__(self, schoolName, degree, fieldOfStudy, date):
		self.schoolName = schoolName
		self.degree = degree
		self.fieldOfStudy = fieldOfStudy
		self.date = date

	def output(self):
		print("schoolName: " + self.schoolName)
		print("degree: " + self.degree)
		print("fieldOfStudy: " + self.fieldOfStudy)
		print("date: " + self.date +'\n')

class experience(object):
	"""experience class contain the company, title and date of an experience record"""
	def __init__(self, company, title, date):
		self.company = company
		self.title = title
		self.date = date

	def output(self):
		print("company: " + self.company)
		print("title: " + self.title)
		print("date: " + self.date +'\n')



class person(object):
	"""person class contains the name of a person, a list of education background and a list experience """
	def __init__(self, name):
		self.name = name
		self.edulist = []
		self.explist = []

	def addedurecord(self, edurecord):
		self.edulist.append(edurecord)

	def addexprecord(self, exprecord):
		self.explist.append(exprecord)

	def output(self):
		print("Name of the person:" + self.name)
		print("Education background:")
		for element in self.edulist:
			element.output()
		print("Experience list:")
		for element in self.explist:
			element.output()


target = person("Jinlei")

driver = webdriver.Firefox()

driver.get("https://www.linkedin.com/")
time.sleep(1)
email = driver.find_element_by_id('login-email')
email.send_keys("emailaddress")
time.sleep(1)
password = driver.find_element_by_id('login-password')
password.send_keys("loginpassword")

password.send_keys(Keys.RETURN)

mainsearchbox = driver.find_element_by_id('main-search-box')
mainsearchbox.send_keys("chen jinlei")
time.sleep(5)
mainsearchbox.send_keys(Keys.ARROW_DOWN)
time.sleep(1)
mainsearchbox.send_keys(Keys.RETURN)

time.sleep(5)

bgedu = driver.find_element_by_id('background-education')
edulist = bgedu.find_elements(By.XPATH, './div')

# TODO: needs to handle some exception when certain information is not provided

for element in edulist:
	schoolName = element.find_element(By.XPATH, './/h4').text
	degree = element.find_element(By.XPATH, './/h5/span[@class="degree"]').text
	fieldOfStudy = element.find_element(By.XPATH, './/h5/span[@class="major"]').text
	date = element.find_element(By.XPATH, './/span[@class="education-date"]').text
	target.addedurecord(education(schoolName, degree, fieldOfStudy, date))

bgexp = driver.find_element_by_id('background-experience')
bglist = bgexp.find_elements(By.XPATH, './div')
for element in bglist:
	company = element.find_element(By.XPATH, './/header/h5[not(@*)]').text
	title = element.find_element(By.XPATH, './/header/h4').text
	datelist = element.find_elements(By.XPATH, './/span[@class="experience-date-locale"]/time')
	if len(datelist) == 2:
		date = str(element.find_element(By.XPATH, './/span[@class="experience-date-locale"]/time[1]').text) + ' - ' + str(element.find_element(By.XPATH, './/span[@class="experience-date-locale"]/time[2]').text)
	else:
		date = str(element.find_element(By.XPATH, './/span[@class="experience-date-locale"]/time[1]').text) + ' - ' + 'present'
	target.addexprecord(experience(company, title, date))

target.output()

#target.output()


time.sleep(3)


driver.quit()
# display.stop()
