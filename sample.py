# from pyvirtualdisplay import Display
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
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
		self.info = ''

	def addedurecord(self, edurecord):
		self.edulist.append(edurecord)

	def addexprecord(self, exprecord):
		self.explist.append(exprecord)

	def addinfo(self, info):
		self.info = info

	def output(self):
		print("Name of the person:" + self.name)
		print("Education background:")
		for element in self.edulist:
			element.output()
		print("Experience list:")
		for element in self.explist:
			element.output()

def login(driver, emailadd, pswd):
	driver.get("https://www.linkedin.com/")
	time.sleep(1)
	email = driver.find_element_by_id('login-email')
	email.send_keys(emailadd)
	time.sleep(1)
	password = driver.find_element_by_id('login-password')
	password.send_keys(pswd)
	password.send_keys(Keys.RETURN)
	return 1

def search(driver, keyword):
	try:
		mainsearchbox = driver.find_element_by_id('main-search-box')
	except NoSuchElementException:
		print("There is no search box found, you may need to pass some verification manually")
		cont = input("Problem fixed? y/n")
		if cont == 'y':
			mainsearchbox = driver.find_element_by_id('main-search-box')
		else:
			return 0
	mainsearchbox.send_keys(keyword)
	time.sleep(2)
	searchbutton = driver.find_element(By.XPATH, '//button[@class="search-button"]')
	searchbutton.click()
	time.sleep(2)
	try:
		firstperson = driver.find_element(By.XPATH, "//li[@class=\"mod result idx1 people\"]").find_element(By.XPATH,'.//a[@class="title main-headline"]')
	except NoSuchElementException:
		firstperson = driver.find_element(By.XPATH, "//li[@class=\"mod result idx2 people\"]").find_element(By.XPATH,'.//a[@class="title main-headline"]')
	firstperson.click()
	time.sleep(2)
	return 1

def fetchdata(driver, target):
	# try:
	# 	linkedinmember = driver.find_element(By.XPATH, '//span[@class="full-name" and @dir="auto"]').text
	# 	if linkedinmember = 


	try:
		bgedu = driver.find_element_by_id('background-education')
		edulist = bgedu.find_elements(By.XPATH, './div')

		#TODO: needs to handle some exception when certain information is not provided

		for element in edulist:
			try:	
				schoolName = element.find_element(By.XPATH, './/h4').text
			except NoSuchElementException:
				schoolName = ''
			try:
				degree = element.find_element(By.XPATH, './/h5/span[@class="degree"]').text
			except NoSuchElementException:
				degree = ''
			try:
				fieldOfStudy = element.find_element(By.XPATH, './/h5/span[@class="major"]').text
			except NoSuchElementException:
				fieldOfStudy = ''
			try:
				date = element.find_element(By.XPATH, './/span[@class="education-date"]').text
			except NoSuchElementException:
				date = ''
			target.addedurecord(education(schoolName, degree, fieldOfStudy, date))
	except NoSuchElementException:
		print("No background education found for the target")

	try:
		bgexp = driver.find_element_by_id('background-experience')
		bglist = bgexp.find_elements(By.XPATH, './div')
		for element in bglist:
			try:
				company = element.find_element(By.XPATH, './/header/h5[not(@*)]').text
			except NoSuchElementException:
				company = ''
			try:
				title = element.find_element(By.XPATH, './/header/h4').text
			except NoSuchElementException:
				title = ''
			try:
				datelist = element.find_elements(By.XPATH, './/span[@class="experience-date-locale"]/time')
				if len(datelist) == 2:
					date = str(element.find_element(By.XPATH, './/span[@class="experience-date-locale"]/time[1]').text) + ' - ' + str(element.find_element(By.XPATH, './/span[@class="experience-date-locale"]/time[2]').text)
				else:
					date = str(element.find_element(By.XPATH, './/span[@class="experience-date-locale"]/time[1]').text) + ' - ' + 'present'
			except NoSuchElementException:
				date = ''
			target.addexprecord(experience(company, title, date))
	except NoSuchElementException:
		print("No background experience found for the target")

target = person("Jinlei")

driver = webdriver.Firefox()

login(driver, '482655720@qq.com', '1a2b3c4dD')
if search(driver, 'Kai Tang University of Michigan'):	
	fetchdata(driver, target)
else:
	print("failed to find the target")

target.output()

time.sleep(3)

