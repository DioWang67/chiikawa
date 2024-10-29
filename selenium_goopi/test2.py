#!/usr/bin/env python3
# -*- coding:utf-8 -*-



from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import configparser
import os
from selenium.webdriver.support.ui import Select
import sys
import keyboard
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By





class autodrive():

	def config(self):
		config = configparser.ConfigParser()
		f = open("config.ini",encoding="utf-8")
		content = f.readlines()
		for lines in content:
			lines = lines.strip('\n')
			print(lines)
			f.close()



		config.read(('config.ini'), encoding='utf-8')

		self.name = config.get('information','name')  # SERVER的IP位置
		self.mail = config.get('information','mail')		
		self.phone = config.get('information','phone')
		self.adress= config.get('information','adress')
		self.card= config.get('information','card')
		self.carddate= config.get('information','carddate')
		self.Securitycode= config.get('information','Securitycode')
		self.line1= config.get('information','line')

		self.account= config.get('logging','account')
		self.password= config.get('logging','password')		
		self.product= config.get('productname','product')
		self.size= config.get('productname','size')
		self.quantity= config.get('productname','quantity')

	def logging(self):

		driver = webdriver.Edge()
		driver.implicitly_wait(15)
		driver.get('https://www.goopi.co/')
		driver.maximize_window()
		element = driver.find_element(By.XPATH,'//*[@id="fixed-menu-container"]/div[2]/a[3]').click()
		element2 = driver.find_element(By.XPATH,'/html/body/div[8]/div[1]/div/div/div/div/div/div/div/div/div[2]/div/div/div/form/div[2]/div/div/input')
		element = driver.find_element(By.XPATH,'/html/body/div[8]/div[1]/div/div/div/div/div/div/div/div/div[2]/div/div/div/form/div[1]/div/div/input')	

		element.send_keys(self.mail)
		# time.sleep(0.5)
		element2.send_keys(self.password)		
		element2.submit()
		element2 = driver.find_element(By.XPATH,'//*[@id="sign-in-recaptcha"]').click()

		# time.sleep(2)

		while True:
			try:
				if keyboard.is_pressed('Enter'):
					print("you pressed Esc, so exiting...")
					break
			except:
				print("wait for press T")
				break
				time.sleep(0.5)
		print("login OK")

		start1 =time.perf_counter()

		while 1:
			start =time.perf_counter()
			try:
				time.sleep(0.5)
				link =driver.find_element(By.PARTIAL_LINK_TEXT,self.product)

				link.click()
				print ("已搜索到目標")
				end=time.perf_counter()
				break
			except:

				print("尚未搜尋到")
				time.sleep(0.5)

		print ("搜尋時間"+str(end-start))

		driver.switch_to.window(driver.window_handles[1])
		# time.sleep(1)

		Select(driver.find_element(By.XPATH,'/html/body/div[8]/div[1]/div/div/div/div[2]/div[3]/div[2]/div[3]/div[1]/div[2]/select')).select_by_value("string:"+self.size)

		quantity = driver.find_element(By.XPATH,'/html/body/div[8]/div[1]/div/div/div/div[2]/div[3]/div[2]/div[3]/div[2]/div[2]/div/input').clear()
		quantity = driver.find_element(By.XPATH,'/html/body/div[8]/div[1]/div/div/div/div[2]/div[3]/div[2]/div[3]/div[2]/div[2]/div/input').send_keys(self.quantity)
		# quantity.send_keys(self.quantity)

		BUY =driver.find_element(By.XPATH,'//*[@id="#btn-variable-buy-now"]/div/span')
		BUY.click()
		# time.sleep(3)
		settleaccounts = driver.find_element(By.XPATH,'//*[@id="checkout-container"]/div/div[3]/div[4]/div[2]/section/div[2]/a').click()

		seven =  driver.find_element(By.XPATH,'//*[@id="seven-eleven-address"]/div/div').click()
		# time.sleep(2)
		driver.switch_to.window(driver.window_handles[1])

		seven2 = driver.find_element(By.XPATH,'//*[@id="byName"]').click()
		# time.sleep(5)
		# driver.switch_to.window(driver.window_handles[1])
		driver.switch_to.frame("frmMain")





		seven3 = driver.find_element(By.ID,'storeNameKey').send_keys(self.adress)
		seven4 = driver.find_element(By.XPATH,'//*[@id="send"]').click()
		seven5 = driver.find_element(By.XPATH,'//*[@id="ol_stores"]/li').click()
		driver.switch_to.default_content()
		seven6 = driver.find_element(By.XPATH,'//*[@id="sevenDataBtn"]').click()
		seven7 = driver.find_element(By.XPATH,'//*[@id="AcceptBtn"]').click()
		seven8 = driver.find_element(By.XPATH,'//*[@id="submit_butn"]').click()


		phone =  driver.find_element(By.XPATH,'//*[@id="order-customer-phone"]').send_keys(self.phone)
		print ("填入電話")

		
		phone =  driver.find_element(By.XPATH,'//*[@id="order-customer-phone"]').send_keys(self.phone)


		line1 =  driver.find_element(By.XPATH,'//*[@id="user-field-598198f2d4e395db79000a21"]').send_keys(self.line1)
		name =  driver.find_element(By.XPATH,'//*[@id="recipient-name"]').send_keys(self.name)
		phone =  driver.find_element(By.XPATH,'//*[@id="recipient-phone"]').send_keys(self.phone)
		time.sleep(0.5)
		driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
		driver.switch_to.frame(0)


		card =  driver.find_element(By.XPATH,'//*[@id="input-file"]').send_keys(self.card)
		driver.switch_to.default_content()
		driver.switch_to.frame(1)
		name =  driver.find_element(By.XPATH,'//*[@id="input-file"]').send_keys(self.name)
		driver.switch_to.default_content()
		driver.switch_to.frame(2)
		carddate =  driver.find_element(By.XPATH,'//*[@id="input-file"]').send_keys(self.carddate)
		driver.switch_to.default_content()
		driver.switch_to.frame(3)
		Securitycode =  driver.find_element(By.XPATH,'//*[@id="input-file"]').send_keys(self.Securitycode)
		driver.switch_to.default_content()


		time.sleep(0.5)
		check =  driver.find_element(By.XPATH,'/html/body/div[8]/div/div/div/div/div[5]/div[1]/form/div/label/input')
		check_conditions = driver.find_element(By.XPATH,'/html/body/div[8]/div/div/div/div/div[5]/div[1]/form/div/label/input')

		driver.execute_script("arguments[0].click();", check_conditions)
		submit =  driver.find_element(By.XPATH,'//*[@id="place-order-recaptcha"]').click()

		end1=time.perf_counter()
		print ("搜尋時間"+str(end1-start1))


		while True:
			try:
				if keyboard.is_pressed('Enter'):
					print("you pressed Esc, so exiting...")
						
					# sys.exit(0)
					break
			except:
				print("wait for press T")
				break
				time.sleep(0.5)

	# def webd(self):
		# print("5")
		# link =driver.find_element(By.C_S'info-box-inner-wrapper').get_attribute("title")
		# link.click()
		# time.sleep(10)
		# driver.quit()

if __name__ == "__main__" :
	autodrive = autodrive()

	autodrive.config()
	autodrive.logging()
	# autodrive.webdrive()

