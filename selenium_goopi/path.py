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
		self.iineid= config.get('information','line')

		self.account= config.get('logging','account')
		self.password= config.get('logging','password')		
		self.product= config.get('productname','product')
		self.size= config.get('productname','size')
		self.quantity= config.get('productname','quantity')

	def logging(self):
		# print("Press Enter to continue or press Esc to exit:")
		# while True:
		#     try:
		#         if keyboard.is_pressed('T'):
		#             print("you pressed Enter, so printing the list..")
		#             print(a)
		#             break
		#         if keyboard.is_pressed('Esc'):
		#             print("you pressed Esc, so exiting...")
							
		#             sys.exit(0)
		#     except:
		#         break


		# print("qwe")


		options = Options()

		driver = webdriver.Edge()
		driver.get('https://www.goopi.co/')
		# element2 = driver.find_element(By.XPATH,'//*[@id="byName"]/a').click()
		options.add_argument("--enable-javascript")

		time.sleep(10)

				
		# element = driver.find_element(By.XPATH,'//*[@id="fixed-menu-container"]/div[2]/a[3]').click()
		# element2 = driver.find_element(By.XPATH,'/html/body/div[8]/div[1]/div/div/div/div/div/div/div/div/div[2]/div/div/div/form/div[2]/div/div/input')
		# element = driver.find_element(By.XPATH,'/html/body/div[8]/div[1]/div/div/div/div/div/div/div/div/div[2]/div/div/div/form/div[1]/div/div/input')	

		# element.send_keys(self.mail)
		# time.sleep(0.5)
		# element2.send_keys(self.password)		
		# # element2.submit()
		# element2 = driver.find_element(By.XPATH,'//*[@id="sign-in-recaptcha"]').click()

		

		# self.webd()
		# driver.quit()
		# while 1:
		# 	start =time.perf_counter()
		# 	# try:

		# 	link =driver.find_element(By.PARTIAL_LINK_TEXT,self.product)

		# 	link.click()
		# 	print ("已搜索到目標")
		# 	end=time.perf_counter()
			# break
			# except:
			# 	print("尚未搜尋到")
			# driver.switch_to.window(driver.window_handles[1])
			# time.sleep(3)

		# print ("搜尋時間"+str(end-start))



			# Select(driver.find_element(By.XPATH,'/html/body/div[8]/div[1]/div/div/div/div[2]/div[3]/div[2]/div[3]/div[1]/div[2]/select')).select_by_value("string:"+self.size)
	
			# quantity = driver.find_element(By.XPATH,'/html/body/div[8]/div[1]/div/div/div/div[2]/div[3]/div[2]/div[3]/div[2]/div[2]/div/input').clear()
			# quantity = driver.find_element(By.XPATH,'/html/body/div[8]/div[1]/div/div/div/div[2]/div[3]/div[2]/div[3]/div[2]/div[2]/div/input').send_keys(self.quantity)
			# # quantity.send_keys(self.quantity)

			# BUY =driver.find_element(By.XPATH,'//*[@id="#btn-variable-buy-now"]/div/span')
			# BUY.click()
			# time.sleep(10)
			# settleaccounts = driver.find_element(By.XPATH,'//*[@id="checkout-container"]/div/div[3]/div[4]/div[2]/section/div[2]/a').click()

			# seven =  driver.find_element(By.XPATH,'//*[@id="seven-eleven-address"]/div/div').click()

			

			# phone =  driver.find_element(By.XPATH,'//*[@id="order-customer-phone"]')
			# phone.send_keys(self.phone)
			
			# lineid =  driver.find_element(By.XPATH,'//*[@id="user-field-598198f2d4e395db79000a21"]')
			# lineid.send_keys(self.lineid)
			
			# recipient =  driver.find_element(By.XPATH,'//*[@id="delivery-form-content"]/div[1]/label/input').click()

	

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

