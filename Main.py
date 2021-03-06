#py3.7
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from tkinter import *
from tkinter import messagebox
import time
import datetime as dt
from datetime import *

options = webdriver.ChromeOptions()
options.add_argument('--disable-extensions')
options.add_argument('--profile-directory=Default')
options.add_argument("--incognito")
options.add_argument("--disable-plugins-discovery")
driver = webdriver.Chrome(options=options)
driver.delete_all_cookies()
driver.set_window_size(800,800)
driver.set_window_position(0,0)
# print("Setup complete")

driver.get('https://textfree.us')

# MADE WITH WORKAROUND OF ANGULARJS MESSING UP INPUTS IF INPUTS ARE SENT TOO FAST
def Sendtxt1():
	now = dt.datetime.now()
	try:
		meme = rack14.get()
		# print("starting")
		rack13.delete(0, END)
		# print("cleared")
		rack13.insert(0, now.minute)
		# print("hour")
		rack13.insert(0, ":")
		# print("colon")
		rack13.insert(0, now.hour)
		# print("minute")
		rack13.config(state='disabled')
		# print("Out logged")
		driver.find_element_by_id('startNewConversationButton').click()
		# print("Button found")
		driver.implicitly_wait(1)
		# print("Writing")
		for x in range(len(meme)): 
			driver.find_element_by_id('contactInput').send_keys(meme[x])
		# print("Input Written")
		driver.implicitly_wait(1)
		driver.find_element_by_class_name("emojionearea-editor").click()
		driver.find_element_by_class_name("emojionearea-editor").send_keys("#")
		driver.find_element_by_class_name("emojionearea-editor").send_keys(rack10.get())
		driver.find_element_by_class_name("emojionearea-editor").send_keys(" in @")
		driver.find_element_by_class_name("emojionearea-editor").send_keys(rack12.get())
		driver.find_element_by_class_name("emojionearea-editor").send_keys(" completed on ")
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s-" % now.day)
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s-" % now.month)
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s-" % now.year)
		driver.find_element_by_class_name("emojionearea-editor").send_keys(" ")
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s:" % now.hour)
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s" % now.minute)
		driver.find_element_by_class_name("emojionearea-editor").send_keys(' in ')
		driver.find_element_by_class_name("emojionearea-editor").send_keys(rack11.get())
		driver.find_element_by_class_name("emojionearea-editor").send_keys(' by ')
		driver.find_element_by_class_name("emojionearea-editor").send_keys(rack14.get())
		# print("class found")
		driver.find_element_by_id('sendButton').click()
		# print("Sent sms")
	except:
		errorcatch = input("ERROR")
		pass

def Sendtxt2():
	now = dt.datetime.now()
	try:
		meme = rack24.get()
		# print("starting")
		rack23.delete(0, END)
		# print("cleared")
		rack23.insert(0, now.minute)
		# print("hour")
		rack23.insert(0, ":")
		# print("colon")
		rack23.insert(0, now.hour)
		# print("minute")
		rack23.config(state='disabled')
		# print("Out logged")
		driver.find_element_by_id('startNewConversationButton').click()
		# print("Button found")
		driver.implicitly_wait(1)
		# print("Writing")
		for x in range(len(meme)): 
			driver.find_element_by_id('contactInput').send_keys(meme[x])
		# print("Input Written")
		driver.implicitly_wait(1)
		driver.find_element_by_class_name("emojionearea-editor").click()
		driver.find_element_by_class_name("emojionearea-editor").send_keys("#")
		driver.find_element_by_class_name("emojionearea-editor").send_keys(rack20.get())
		driver.find_element_by_class_name("emojionearea-editor").send_keys(" in @")
		driver.find_element_by_class_name("emojionearea-editor").send_keys(rack22.get())
		driver.find_element_by_class_name("emojionearea-editor").send_keys(" completed on ")
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s-" % now.day)
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s-" % now.month)
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s-" % now.year)
		driver.find_element_by_class_name("emojionearea-editor").send_keys(" ")
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s:" % now.hour)
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s" % now.minute)
		driver.find_element_by_class_name("emojionearea-editor").send_keys(' in ')
		driver.find_element_by_class_name("emojionearea-editor").send_keys(rack21.get())
		driver.find_element_by_class_name("emojionearea-editor").send_keys(' by ')
		driver.find_element_by_class_name("emojionearea-editor").send_keys(rack24.get())
		# print("class found")
		driver.find_element_by_id('sendButton').click()
		# print("Sent sms")
	except:
		errorcatch = input("ERROR")
		pass

def Sendtxt3():
	now = dt.datetime.now()
	try:
		meme = rack34.get()
		# print("starting")
		rack33.delete(0, END)
		# print("cleared")
		rack33.insert(0, now.minute)
		# print("hour")
		rack33.insert(0, ":")
		# print("colon")
		rack33.insert(0, now.hour)
		# print("minute")
		rack33.config(state='disabled')
		# print("Out logged")
		driver.find_element_by_id('startNewConversationButton').click()
		# print("Button found")
		driver.implicitly_wait(1)
		# print("Writing")
		for x in range(len(meme)): 
			driver.find_element_by_id('contactInput').send_keys(meme[x])
		# print("Input Written")
		driver.implicitly_wait(1)
		driver.find_element_by_class_name("emojionearea-editor").click()
		driver.find_element_by_class_name("emojionearea-editor").send_keys("#")
		driver.find_element_by_class_name("emojionearea-editor").send_keys(rack30.get())
		driver.find_element_by_class_name("emojionearea-editor").send_keys(" in @")
		driver.find_element_by_class_name("emojionearea-editor").send_keys(rack32.get())
		driver.find_element_by_class_name("emojionearea-editor").send_keys(" completed on ")
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s-" % now.day)
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s-" % now.month)
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s-" % now.year)
		driver.find_element_by_class_name("emojionearea-editor").send_keys(" ")
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s:" % now.hour)
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s" % now.minute)
		driver.find_element_by_class_name("emojionearea-editor").send_keys(' in ')
		driver.find_element_by_class_name("emojionearea-editor").send_keys(rack31.get())
		driver.find_element_by_class_name("emojionearea-editor").send_keys(' by ')
		driver.find_element_by_class_name("emojionearea-editor").send_keys(rack34.get())
		# print("class found")
		driver.find_element_by_id('sendButton').click()
		# print("Sent sms")
	except:
		errorcatch = input("ERROR")
		pass

def Sendtxt4():
	now = dt.datetime.now()
	try:
		meme = rack44.get()
		# print("starting")
		rack43.delete(0, END)
		# print("cleared")
		rack43.insert(0, now.minute)
		# print("hour")
		rack43.insert(0, ":")
		# print("colon")
		rack43.insert(0, now.hour)
		# print("minute")
		rack43.config(state='disabled')
		# print("Out logged")
		driver.find_element_by_id('startNewConversationButton').click()
		# print("Button found")
		driver.implicitly_wait(1)
		# print("Writing")
		for x in range(len(meme)): 
			driver.find_element_by_id('contactInput').send_keys(meme[x])
		# print("Input Written")
		driver.implicitly_wait(1)
		driver.find_element_by_class_name("emojionearea-editor").click()
		driver.find_element_by_class_name("emojionearea-editor").send_keys("#")
		driver.find_element_by_class_name("emojionearea-editor").send_keys(rack40.get())
		driver.find_element_by_class_name("emojionearea-editor").send_keys(" in @")
		driver.find_element_by_class_name("emojionearea-editor").send_keys(rack42.get())
		driver.find_element_by_class_name("emojionearea-editor").send_keys(" completed on ")
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s-" % now.day)
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s-" % now.month)
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s-" % now.year)
		driver.find_element_by_class_name("emojionearea-editor").send_keys(" ")
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s:" % now.hour)
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s" % now.minute)
		driver.find_element_by_class_name("emojionearea-editor").send_keys(' in ')
		driver.find_element_by_class_name("emojionearea-editor").send_keys(rack41.get())
		driver.find_element_by_class_name("emojionearea-editor").send_keys(' by ')
		driver.find_element_by_class_name("emojionearea-editor").send_keys(rack44.get())
		# print("class found")
		driver.find_element_by_id('sendButton').click()
		# print("Sent sms")
	except:
		errorcatch = input("ERROR")
		pass

def Sendtxt5():
	now = dt.datetime.now()
	try:
		meme = rack54.get()
		# print("starting")
		rack53.delete(0, END)
		# print("cleared")
		rack53.insert(0, now.minute)
		# print("hour")
		rack53.insert(0, ":")
		# print("colon")
		rack53.insert(0, now.hour)
		# print("minute")
		rack53.config(state='disabled')
		# print("Out logged")
		driver.find_element_by_id('startNewConversationButton').click()
		# print("Button found")
		driver.implicitly_wait(1)
		# print("Writing")
		for x in range(len(meme)): 
			driver.find_element_by_id('contactInput').send_keys(meme[x])
		# print("Input Written")
		driver.implicitly_wait(1)
		driver.find_element_by_class_name("emojionearea-editor").click()
		driver.find_element_by_class_name("emojionearea-editor").send_keys("#")
		driver.find_element_by_class_name("emojionearea-editor").send_keys(rack50.get())
		driver.find_element_by_class_name("emojionearea-editor").send_keys(" in @")
		driver.find_element_by_class_name("emojionearea-editor").send_keys(rack52.get())
		driver.find_element_by_class_name("emojionearea-editor").send_keys(" completed on ")
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s-" % now.day)
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s-" % now.month)
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s-" % now.year)
		driver.find_element_by_class_name("emojionearea-editor").send_keys(" ")
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s:" % now.hour)
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s" % now.minute)
		driver.find_element_by_class_name("emojionearea-editor").send_keys(' in ')
		driver.find_element_by_class_name("emojionearea-editor").send_keys(rack51.get())
		driver.find_element_by_class_name("emojionearea-editor").send_keys(' by ')
		driver.find_element_by_class_name("emojionearea-editor").send_keys(rack54.get())
		# print("class found")
		driver.find_element_by_id('sendButton').click()
		# print("Sent sms")
	except:
		errorcatch = input("ERROR")
		pass

def Sendtxt6():
	now = dt.datetime.now()
	try:
		meme = rack64.get()
		# print("starting")
		rack63.delete(0, END)
		# print("cleared")
		rack63.insert(0, now.minute)
		# print("hour")
		rack63.insert(0, ":")
		# print("colon")
		rack63.insert(0, now.hour)
		# print("minute")
		rack63.config(state='disabled')
		# print("Out logged")
		driver.find_element_by_id('startNewConversationButton').click()
		# print("Button found")
		driver.implicitly_wait(1)
		# print("Writing")
		for x in range(len(meme)): 
			driver.find_element_by_id('contactInput').send_keys(meme[x])
		# print("Input Written")
		driver.implicitly_wait(1)
		driver.find_element_by_class_name("emojionearea-editor").click()
		driver.find_element_by_class_name("emojionearea-editor").send_keys("#")
		driver.find_element_by_class_name("emojionearea-editor").send_keys(rack60.get())
		driver.find_element_by_class_name("emojionearea-editor").send_keys(" in @")
		driver.find_element_by_class_name("emojionearea-editor").send_keys(rack62.get())
		driver.find_element_by_class_name("emojionearea-editor").send_keys(" completed on ")
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s-" % now.day)
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s-" % now.month)
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s-" % now.year)
		driver.find_element_by_class_name("emojionearea-editor").send_keys(" ")
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s:" % now.hour)
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s" % now.minute)
		driver.find_element_by_class_name("emojionearea-editor").send_keys(' in ')
		driver.find_element_by_class_name("emojionearea-editor").send_keys(rack61.get())
		driver.find_element_by_class_name("emojionearea-editor").send_keys(' by ')
		driver.find_element_by_class_name("emojionearea-editor").send_keys(rack64.get())
		# print("class found")
		driver.find_element_by_id('sendButton').click()
		# print("Sent sms")
	except:
		errorcatch = input("ERROR")
		pass

def Sendtxt7():
	now = dt.datetime.now()
	try:
		meme = rack74.get()
		# print("starting")
		rack73.delete(0, END)
		# print("cleared")
		rack73.insert(0, now.minute)
		# print("hour")
		rack73.insert(0, ":")
		# print("colon")
		rack73.insert(0, now.hour)
		# print("minute")
		rack73.config(state='disabled')
		# print("Out logged")
		driver.find_element_by_id('startNewConversationButton').click()
		# print("Button found")
		driver.implicitly_wait(1)
		# print("Writing")
		for x in range(len(meme)): 
			driver.find_element_by_id('contactInput').send_keys(meme[x])
		# print("Input Written")
		driver.implicitly_wait(1)
		driver.find_element_by_class_name("emojionearea-editor").click()
		driver.find_element_by_class_name("emojionearea-editor").send_keys("#")
		driver.find_element_by_class_name("emojionearea-editor").send_keys(rack70.get())
		driver.find_element_by_class_name("emojionearea-editor").send_keys(" in @")
		driver.find_element_by_class_name("emojionearea-editor").send_keys(rack72.get())
		driver.find_element_by_class_name("emojionearea-editor").send_keys(" completed on ")
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s-" % now.day)
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s-" % now.month)
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s-" % now.year)
		driver.find_element_by_class_name("emojionearea-editor").send_keys(" ")
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s:" % now.hour)
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s" % now.minute)
		driver.find_element_by_class_name("emojionearea-editor").send_keys(' in ')
		driver.find_element_by_class_name("emojionearea-editor").send_keys(rack71.get())
		driver.find_element_by_class_name("emojionearea-editor").send_keys(' by ')
		driver.find_element_by_class_name("emojionearea-editor").send_keys(rack74.get())
		# print("class found")
		driver.find_element_by_id('sendButton').click()
		# print("Sent sms")
	except:
		errorcatch = input("ERROR")
		pass

def Sendtxt8():
	now = dt.datetime.now()
	try:
		meme = rack84.get()
		# print("starting")
		rack83.delete(0, END)
		# print("cleared")
		rack83.insert(0, now.minute)
		# print("hour")
		rack83.insert(0, ":")
		# print("colon")
		rack83.insert(0, now.hour)
		# print("minute")
		rack83.config(state='disabled')
		# print("Out logged")
		driver.find_element_by_id('startNewConversationButton').click()
		# print("Button found")
		driver.implicitly_wait(1)
		# print("Writing")
		for x in range(len(meme)): 
			driver.find_element_by_id('contactInput').send_keys(meme[x])
		# print("Input Written")
		driver.implicitly_wait(1)
		driver.find_element_by_class_name("emojionearea-editor").click()
		driver.find_element_by_class_name("emojionearea-editor").send_keys("#")
		driver.find_element_by_class_name("emojionearea-editor").send_keys(rack80.get())
		driver.find_element_by_class_name("emojionearea-editor").send_keys(" in @")
		driver.find_element_by_class_name("emojionearea-editor").send_keys(rack82.get())
		driver.find_element_by_class_name("emojionearea-editor").send_keys(" completed on ")
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s-" % now.day)
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s-" % now.month)
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s-" % now.year)
		driver.find_element_by_class_name("emojionearea-editor").send_keys(" ")
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s:" % now.hour)
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s" % now.minute)
		driver.find_element_by_class_name("emojionearea-editor").send_keys(' in ')
		driver.find_element_by_class_name("emojionearea-editor").send_keys(rack81.get())
		driver.find_element_by_class_name("emojionearea-editor").send_keys(' by ')
		driver.find_element_by_class_name("emojionearea-editor").send_keys(rack84.get())
		# print("class found")
		driver.find_element_by_id('sendButton').click()
		# print("Sent sms")
	except:
		errorcatch = input("ERROR")
		pass

def Sendtxt9():
	now = dt.datetime.now()
	try:
		meme = rack94.get()
		# print("starting")
		rack93.delete(0, END)
		# print("cleared")
		rack93.insert(0, now.minute)
		# print("hour")
		rack93.insert(0, ":")
		# print("colon")
		rack93.insert(0, now.hour)
		# print("minute")
		rack93.config(state='disabled')
		# print("Out logged")
		driver.find_element_by_id('startNewConversationButton').click()
		# print("Button found")
		driver.implicitly_wait(1)
		# print("Writing")
		for x in range(len(meme)): 
			driver.find_element_by_id('contactInput').send_keys(meme[x])
		# print("Input Written")
		driver.implicitly_wait(1)
		driver.find_element_by_class_name("emojionearea-editor").click()
		driver.find_element_by_class_name("emojionearea-editor").send_keys("#")
		driver.find_element_by_class_name("emojionearea-editor").send_keys(rack90.get())
		driver.find_element_by_class_name("emojionearea-editor").send_keys(" in @")
		driver.find_element_by_class_name("emojionearea-editor").send_keys(rack92.get())
		driver.find_element_by_class_name("emojionearea-editor").send_keys(" completed on ")
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s-" % now.day)
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s-" % now.month)
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s-" % now.year)
		driver.find_element_by_class_name("emojionearea-editor").send_keys(" ")
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s:" % now.hour)
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s" % now.minute)
		driver.find_element_by_class_name("emojionearea-editor").send_keys(' in ')
		driver.find_element_by_class_name("emojionearea-editor").send_keys(rack91.get())
		driver.find_element_by_class_name("emojionearea-editor").send_keys(' by ')
		driver.find_element_by_class_name("emojionearea-editor").send_keys(rack94.get())
		# print("class found")
		driver.find_element_by_id('sendButton').click()
		# print("Sent sms")
	except:
		errorcatch = input("ERROR")
		pass

def Sendtxt10():
	now = dt.datetime.now()
	try:
		meme = rack104.get()
		# print("starting")
		rack103.delete(0, END)
		# print("cleared")
		rack103.insert(0, now.minute)
		# print("hour")
		rack103.insert(0, ":")
		# print("colon")
		rack103.insert(0, now.hour)
		# print("minute")
		rack103.config(state='disabled')
		# print("Out logged")
		driver.find_element_by_id('startNewConversationButton').click()
		# print("Button found")
		driver.implicitly_wait(1)
		# print("Writing")
		for x in range(len(meme)): 
			driver.find_element_by_id('contactInput').send_keys(meme[x])
		# print("Input Written")
		driver.implicitly_wait(1)
		driver.find_element_by_class_name("emojionearea-editor").click()
		driver.find_element_by_class_name("emojionearea-editor").send_keys("#")
		driver.find_element_by_class_name("emojionearea-editor").send_keys(rack100.get())
		driver.find_element_by_class_name("emojionearea-editor").send_keys(" in @")
		driver.find_element_by_class_name("emojionearea-editor").send_keys(rack102.get())
		driver.find_element_by_class_name("emojionearea-editor").send_keys(" completed on ")
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s-" % now.day)
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s-" % now.month)
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s-" % now.year)
		driver.find_element_by_class_name("emojionearea-editor").send_keys(" ")
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s:" % now.hour)
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s" % now.minute)
		driver.find_element_by_class_name("emojionearea-editor").send_keys(' in ')
		driver.find_element_by_class_name("emojionearea-editor").send_keys(rack101.get())
		driver.find_element_by_class_name("emojionearea-editor").send_keys(' by ')
		driver.find_element_by_class_name("emojionearea-editor").send_keys(rack104.get())
		# print("class found")
		driver.find_element_by_id('sendButton').click()
		# print("Sent sms")
	except:
		errorcatch = input("ERROR")
		pass

def Sendtxt11():
	now = dt.datetime.now()
	try:
		meme = rack114.get()
		# print("starting")
		rack113.delete(0, END)
		# print("cleared")
		rack113.insert(0, now.minute)
		# print("hour")
		rack113.insert(0, ":")
		# print("colon")
		rack113.insert(0, now.hour)
		# print("minute")
		rack113.config(state='disabled')
		# print("Out logged")
		driver.find_element_by_id('startNewConversationButton').click()
		# print("Button found")
		driver.implicitly_wait(1)
		# print("Writing")
		for x in range(len(meme)): 
			driver.find_element_by_id('contactInput').send_keys(meme[x])
		# print("Input Written")
		driver.implicitly_wait(1)
		driver.find_element_by_class_name("emojionearea-editor").click()
		driver.find_element_by_class_name("emojionearea-editor").send_keys("#")
		driver.find_element_by_class_name("emojionearea-editor").send_keys(rack110.get())
		driver.find_element_by_class_name("emojionearea-editor").send_keys(" in @")
		driver.find_element_by_class_name("emojionearea-editor").send_keys(rack112.get())
		driver.find_element_by_class_name("emojionearea-editor").send_keys(" completed on ")
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s-" % now.day)
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s-" % now.month)
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s-" % now.year)
		driver.find_element_by_class_name("emojionearea-editor").send_keys(" ")
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s:" % now.hour)
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s" % now.minute)
		driver.find_element_by_class_name("emojionearea-editor").send_keys(' in ')
		driver.find_element_by_class_name("emojionearea-editor").send_keys(rack111.get())
		driver.find_element_by_class_name("emojionearea-editor").send_keys(' by ')
		driver.find_element_by_class_name("emojionearea-editor").send_keys(rack114.get())
		# print("class found")
		driver.find_element_by_id('sendButton').click()
		# print("Sent sms")
	except:
		errorcatch = input("ERROR")
		pass

def Sendtxt12():
	now = dt.datetime.now()
	try:
		meme = rack124.get()
		# print("starting")
		rack123.delete(0, END)
		# print("cleared")
		rack123.insert(0, now.minute)
		# print("hour")
		rack123.insert(0, ":")
		# print("colon")
		rack123.insert(0, now.hour)
		# print("minute")
		rack123.config(state='disabled')
		# print("Out logged")
		driver.find_element_by_id('startNewConversationButton').click()
		# print("Button found")
		driver.implicitly_wait(1)
		# print("Writing")
		for x in range(len(meme)): 
			driver.find_element_by_id('contactInput').send_keys(meme[x])
		# print("Input Written")
		driver.implicitly_wait(1)
		driver.find_element_by_class_name("emojionearea-editor").click()
		driver.find_element_by_class_name("emojionearea-editor").send_keys("#")
		driver.find_element_by_class_name("emojionearea-editor").send_keys(rack120.get())
		driver.find_element_by_class_name("emojionearea-editor").send_keys(" in @")
		driver.find_element_by_class_name("emojionearea-editor").send_keys(rack122.get())
		driver.find_element_by_class_name("emojionearea-editor").send_keys(" completed on ")
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s-" % now.day)
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s-" % now.month)
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s-" % now.year)
		driver.find_element_by_class_name("emojionearea-editor").send_keys(" ")
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s:" % now.hour)
		driver.find_element_by_class_name("emojionearea-editor").send_keys("%s" % now.minute)
		driver.find_element_by_class_name("emojionearea-editor").send_keys(' in ')
		driver.find_element_by_class_name("emojionearea-editor").send_keys(rack121.get())
		driver.find_element_by_class_name("emojionearea-editor").send_keys(' by ')
		driver.find_element_by_class_name("emojionearea-editor").send_keys(rack124.get())
		# print("class found")
		driver.find_element_by_id('sendButton').click()
		# print("Sent sms")
	except:
		errorcatch = input("ERROR")
		pass

def Clearmsg1():
	rack10.delete(0, END)
	rack11.delete(0, END)
	rack12.delete(0, END)
	try:
		rack13.config(state='normal')
	except:
		pass
	rack13.delete(0, END)
	rack14.delete(0, END)

def Clearmsg2():
	rack20.delete(0, END)
	rack21.delete(0, END)
	rack22.delete(0, END)
	try:
		rack23.config(state='normal')
	except:
		pass
	rack23.delete(0, END)
	rack24.delete(0, END)

def Clearmsg3():
	rack30.delete(0, END)
	rack31.delete(0, END)
	rack32.delete(0, END)
	try:
		rack33.config(state='normal')
	except:
		pass
	rack33.delete(0, END)
	rack34.delete(0, END)

def Clearmsg4():
	rack40.delete(0, END)
	rack41.delete(0, END)
	rack42.delete(0, END)
	try:
		rack43.config(state='normal')
	except:
		pass
	rack43.delete(0, END)
	rack44.delete(0, END)

def Clearmsg5():
	rack50.delete(0, END)
	rack51.delete(0, END)
	rack52.delete(0, END)
	try:
		rack53.config(state='normal')
	except:
		pass
	rack53.delete(0, END)
	rack54.delete(0, END)

def Clearmsg6():
	rack60.delete(0, END)
	rack61.delete(0, END)
	rack62.delete(0, END)
	try:
		rack63.config(state='normal')
	except:
		pass
	rack63.delete(0, END)
	rack64.delete(0, END)

def Clearmsg7():
	rack70.delete(0, END)
	rack71.delete(0, END)
	rack72.delete(0, END)
	try:
		rack73.config(state='normal')
	except:
		pass
	rack73.delete(0, END)
	rack74.delete(0, END)

def Clearmsg8():
	rack80.delete(0, END)
	rack81.delete(0, END)
	rack82.delete(0, END)
	try:
		rack83.config(state='normal')
	except:
		pass
	rack83.delete(0, END)
	rack84.delete(0, END)

def Clearmsg9():
	rack90.delete(0, END)
	rack91.delete(0, END)
	rack92.delete(0, END)
	try:
		rack93.config(state='normal')
	except:
		pass
	rack93.delete(0, END)
	rack94.delete(0, END)

def Clearmsg10():
	rack100.delete(0, END)
	rack101.delete(0, END)
	rack102.delete(0, END)
	try:
		rack103.config(state='normal')
	except:
		pass
	rack103.delete(0, END)
	rack104.delete(0, END)

def Clearmsg11():
	rack110.delete(0, END)
	rack111.delete(0, END)
	rack112.delete(0, END)
	try:
		rack113.config(state='normal')
	except:
		pass
	rack113.delete(0, END)
	rack114.delete(0, END)

def Clearmsg12():
	rack120.delete(0, END)
	rack121.delete(0, END)
	rack122.delete(0, END)
	try:
		rack123.config(state='normal')
	except:
		pass
	rack123.delete(0, END)
	rack124.delete(0, END)

def help_msg():
    messagebox.showinfo("help", "Dates are all listed in day/month/year hour:minute\n\nTo use: Log into textfree.us and leave on the contact page, when you press the SMS button it will send the SMS as if the row was completed with all information from the row to the Phone# on the row and will put the hour:minute in 24 hour clock format into the OUT column then locks the column\n\nwrite the phone number in xxxxxxxxxx no () and no dashes\n\n To reset the board and to unlock the OUT columns you will need to restart the program\n\n The log button takes all information on the panels and writes to a .txt file in the same directory as the program's EXE if there is no txt file there it will create one for it and write to it\nTimer's window TITLE updates with the actual timer so can be minimized and you'll still be able to see the timer in seconds\n\nrequires http://chromedriver.chromium.org/downloads \n\n\n 24-11-2018 https://github.com/momomeomo version 2")
	
def Log():
	now = dt.datetime.now()
	f = open('rackLogs.txt','a+')
	f.write("\n")
	f.write("Log time: ")
	f.write("%s-" % now.day)
	f.write("%s-" % now.month)
	f.write("%s" % now.year)
	f.write("  ")
	f.write("%s:" % now.hour)
	f.write("%s" % now.minute)
	f.write("\n")
	# 10 0
	f.write("Racks:")
	f.write("Rack: %s " % rack10.get())
	f.write("Rack: %s " % rack20.get())
	f.write("Rack: %s " % rack30.get())
	f.write("Rack: %s " % rack40.get())
	f.write("Rack: %s " % rack50.get())
	f.write("Rack: %s " % rack60.get())
	f.write("Rack: %s " % rack70.get())
	f.write("Rack: %s " % rack80.get())
	f.write("Rack: %s " % rack90.get())
	f.write("Rack: %s " % rack100.get())
	f.write("Rack: %s " % rack110.get())
	f.write("Rack: %s " % rack120.get())
	f.write("\n")
	# 10 1
	f.write("Location: ")
	f.write("%s " % rack11.get())
	f.write("%s " % rack21.get())
	f.write("%s " % rack31.get())
	f.write("%s " % rack41.get()) 
	f.write("%s " % rack51.get()) 
	f.write("%s " % rack61.get()) 
	f.write("%s " % rack71.get()) 
	f.write("%s " % rack81.get()) 
	f.write("%s " % rack91.get()) 
	f.write("%s " % rack101.get())
	f.write("%s " % rack111.get())
	f.write("%s " % rack121.get())
	f.write("\n")
	# 10 2
	f.write("IN time: ")
	f.write("%s " % rack12.get())
	f.write("%s " % rack22.get())
	f.write("%s " % rack32.get())
	f.write("%s " % rack42.get())
	f.write("%s " % rack52.get())
	f.write("%s " % rack62.get())
	f.write("%s " % rack72.get())
	f.write("%s " % rack82.get())
	f.write("%s " % rack92.get())
	f.write("%s " % rack102.get())
	f.write("%s " % rack112.get())
	f.write("%s " % rack122.get())
	f.write("\n")
	# 10 3
	f.write("OUT time: ")
	f.write("%s " % rack13.get())
	f.write("%s " % rack23.get())
	f.write("%s " % rack33.get())
	f.write("%s " % rack43.get())
	f.write("%s " % rack53.get())
	f.write("%s " % rack63.get())
	f.write("%s " % rack73.get())
	f.write("%s " % rack83.get())
	f.write("%s " % rack93.get())
	f.write("%s " % rack103.get())
	f.write("%s " % rack113.get())
	f.write("%s " % rack123.get())
	f.write("\n")
	# 10 4
	f.write("Phone#: ")
	f.write("#%s " % rack14.get())
	f.write("#%s " % rack24.get())
	f.write("#%s " % rack34.get())
	f.write("#%s " % rack44.get())
	f.write("#%s " % rack54.get())
	f.write("#%s " % rack64.get())
	f.write("#%s " % rack74.get())
	f.write("#%s " % rack84.get())
	f.write("#%s " % rack94.get())
	f.write("#%s " % rack104.get())
	f.write("#%s " % rack114.get())
	f.write("#%s " % rack124.get())

def on_closing():
	driver.quit()
	main.quit()
	main.destroy()


main = Tk()



main.protocol("WM_DELETE_WINDOW", on_closing)
main.title("Main")
main.resizable(0, 0)

#Timer
# create the time display label, give it a large font
# label auto-adjusts to the font
# time_str = tkinter.StringVar()
# label_font = ('helvetica', 40)
# label(main, textvariable=time_str, font=label_font, bg='white', fg='blue', relief='raised', bd=3).pack(fill='x', padx=5, pady=5)

# Labels
# Label(main, text="NEXT RACK OUT IN ", font="-weight bold",).grid(row=1, column=2, columnspan=3)
Label(main, text="Rack#", font="-weight bold").grid(row=2, column=2)
Label(main, text="Location", font="-weight bold").grid(row=2, column=3)
Label(main, text="IN\nTime", font="-weight bold").grid(row=2, column=4)
Label(main, text="OUT\nTime", font="-weight bold").grid(row=2, column=5)
Label(main, text="Phone#", font="-weight bold").grid(row=2, column=6)
Label(main, text="Out", font="-weight bold").grid(row=2, column=7)
Label(main, text=" ").grid(row=15, column=8)
Label(main, text=" ").grid(row=15, column=9)
Label(main, text=" ").grid(row=15, column=10)
Label(main, text=" ").grid(row=15, column=11)

		# Fields
		#	Rack#
rack10 = Entry(main, width=8, justify='center')
rack10.grid(row=3, column=2, pady=4, padx=2)
rack20 = Entry(main, width=8, justify='center')
rack20.grid(row=4, column=2, pady=4, padx=2)
rack30 = Entry(main, width=8, justify='center')
rack30.grid(row=5, column=2, pady=4, padx=2)
rack40 = Entry(main, width=8, justify='center')
rack40.grid(row=6, column=2, pady=4, padx=2)
rack50 = Entry(main, width=8, justify='center')       
rack50.grid(row=7, column=2, pady=4, padx=2)
rack60 = Entry(main, width=8, justify='center')        
rack60.grid(row=8, column=2, pady=4, padx=2)
rack70 = Entry(main, width=8, justify='center')        
rack70.grid(row=9, column=2, pady=4, padx=2)
rack80 = Entry(main, width=8, justify='center')
rack80.grid(row=10, column=2, pady=4, padx=2)
rack90 = Entry(main, width=8, justify='center')         
rack90.grid(row=11, column=2, pady=4, padx=2)
rack100 = Entry(main, width=8, justify='center')
rack100.grid(row=12, column=2, pady=4, padx=2)
rack110 = Entry(main, width=8, justify='center')        
rack110.grid(row=13, column=2, pady=4, padx=2)
rack120 = Entry(main, width=8, justify='center')          
rack120.grid(row=14, column=2, pady=4, padx=2)

		#	Location
rack11 = Entry(main)
rack11.grid(row=3, column=3, pady=4, padx=2)
rack21 = Entry(main)      
rack21.grid(row=4, column=3, pady=4, padx=2)
rack31 = Entry(main)      
rack31.grid(row=5, column=3, pady=4, padx=2)
rack41 = Entry(main)      
rack41.grid(row=6, column=3, pady=4, padx=2)
rack51 = Entry(main)      
rack51.grid(row=7, column=3, pady=4, padx=2)
rack61 = Entry(main)       
rack61.grid(row=8, column=3, pady=4, padx=2)
rack71 = Entry(main)      
rack71.grid(row=9, column=3, pady=4, padx=2)
rack81 = Entry(main)
rack81.grid(row=10, column=3, pady=4, padx=2)
rack91 = Entry(main)       
rack91.grid(row=11, column=3, pady=4, padx=2)
rack101 = Entry(main)
rack101.grid(row=12, column=3, pady=4, padx=2)
rack111 = Entry(main)         
rack111.grid(row=13, column=3, pady=4, padx=2)
rack121 = Entry(main)         
rack121.grid(row=14, column=3, pady=4, padx=2)

		#	IN time
rack12 = Entry(main)
rack12.grid(row=3, column=4, pady=4, padx=2)
rack22 = Entry(main)         
rack22.grid(row=4, column=4, pady=4, padx=2)
rack32 = Entry(main)         
rack32.grid(row=5, column=4, pady=4, padx=2)
rack42 = Entry(main)         
rack42.grid(row=6, column=4, pady=4, padx=2)
rack52 = Entry(main)         
rack52.grid(row=7, column=4, pady=4, padx=2)
rack62 = Entry(main)         
rack62.grid(row=8, column=4, pady=4, padx=2)
rack72 = Entry(main)         
rack72.grid(row=9, column=4, pady=4, padx=2)
rack82 = Entry(main)
rack82.grid(row=10, column=4, pady=4, padx=2)
rack92 = Entry(main)
rack92.grid(row=11, column=4, pady=4, padx=2)
rack102 = Entry(main)
rack102.grid(row=12, column=4, pady=4, padx=2)
rack112 = Entry(main)
rack112.grid(row=13, column=4, pady=4, padx=2)
rack122 = Entry(main)
rack122.grid(row=14, column=4, pady=4, padx=2)

		#	OUT time
rack13 = Entry(main)
rack13.grid(row=3, column=5, pady=4, padx=2)
rack23 = Entry(main)       
rack23.grid(row=4, column=5, pady=4, padx=2)
rack33 = Entry(main)        
rack33.grid(row=5, column=5, pady=4, padx=2)
rack43 = Entry(main)       
rack43.grid(row=6, column=5, pady=4, padx=2)
rack53 = Entry(main)        
rack53.grid(row=7, column=5, pady=4, padx=2)
rack63 = Entry(main)		
rack63.grid(row=8, column=5, pady=4, padx=2)
rack73 = Entry(main)	
rack73.grid(row=9, column=5, pady=4, padx=2)
rack83 = Entry(main)		
rack83.grid(row=10, column=5, pady=4, padx=2)
rack93 = Entry(main)			
rack93.grid(row=11, column=5, pady=4, padx=2)
rack103 = Entry(main)			
rack103.grid(row=12, column=5, pady=4, padx=2)
rack113 = Entry(main)			
rack113.grid(row=13, column=5, pady=4, padx=2)
rack123 = Entry(main)			
rack123.grid(row=14, column=5, pady=4, padx=2)

		#	Phone#
rack14 = Entry(main)
rack14.grid(row=3, column=6, pady=4, padx=2)
rack24 = Entry(main)         
rack24.grid(row=4, column=6, pady=4, padx=2)
rack34 = Entry(main)         
rack34.grid(row=5, column=6, pady=4, padx=2)
rack44 = Entry(main)         
rack44.grid(row=6, column=6, pady=4, padx=2)
rack54 = Entry(main)         
rack54.grid(row=7, column=6, pady=4, padx=2)
rack64 = Entry(main)         
rack64.grid(row=8, column=6, pady=4, padx=2)
rack74 = Entry(main)        
rack74.grid(row=9, column=6, pady=4, padx=2)
rack84 = Entry(main)
rack84.grid(row=10, column=6, pady=4, padx=2)
rack94 = Entry(main)         
rack94.grid(row=11, column=6, pady=4, padx=2)
rack104 = Entry(main)
rack104.grid(row=12, column=6, pady=4, padx=2)
rack114 = Entry(main)          
rack114.grid(row=13, column=6, pady=4, padx=2)
rack124 = Entry(main)          
rack124.grid(row=14, column=6, pady=4, padx=2)

		#	Out
Button(main, text="SMS", command=Sendtxt1).grid(row=3, column=7)
Button(main, text="SMS", command=Sendtxt2).grid(row=4, column=7)
Button(main, text="SMS", command=Sendtxt3).grid(row=5, column=7)
Button(main, text="SMS", command=Sendtxt4).grid(row=6, column=7)
Button(main, text="SMS", command=Sendtxt5).grid(row=7, column=7)
Button(main, text="SMS", command=Sendtxt6).grid(row=8, column=7)
Button(main, text="SMS", command=Sendtxt7).grid(row=9, column=7)
Button(main, text="SMS", command=Sendtxt8).grid(row=10, column=7)
Button(main, text="SMS", command=Sendtxt9).grid(row=11, column=7)
Button(main, text="SMS", command=Sendtxt10).grid(row=12, column=7)
Button(main, text="SMS", command=Sendtxt11).grid(row=13, column=7)
Button(main, text="SMS", command=Sendtxt12).grid(row=14, column=7)

#Clear
Button(main, text="Clear", command=Clearmsg1).grid(row=3, column=1)
Button(main, text="Clear", command=Clearmsg2).grid(row=4, column=1)
Button(main, text="Clear", command=Clearmsg3).grid(row=5, column=1)
Button(main, text="Clear", command=Clearmsg4).grid(row=6, column=1)
Button(main, text="Clear", command=Clearmsg5).grid(row=7, column=1)
Button(main, text="Clear", command=Clearmsg6).grid(row=8, column=1)
Button(main, text="Clear", command=Clearmsg7).grid(row=9, column=1)
Button(main, text="Clear", command=Clearmsg8).grid(row=10, column=1)
Button(main, text="Clear", command=Clearmsg9).grid(row=11, column=1)
Button(main, text="Clear", command=Clearmsg10).grid(row=12, column=1)
Button(main, text="Clear", command=Clearmsg11).grid(row=13, column=1)
Button(main, text="Clear", command=Clearmsg12).grid(row=14, column=1)

		# Buttons
Button(main, text="Help", command=help_msg).grid(row=1, column=0, pady=4)
Button(main, text="Log", command=Log).grid(row=1, column=1, pady=4)



mainloop()
