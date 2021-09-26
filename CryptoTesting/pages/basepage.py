# -*- coding: utf-8 -*- 
"""
@Author:    mzhang
@File:      basepage.py
@Date:      2021/09/24
@Desc:
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime

class basepage(object):
	single_search_mapping = {
		"id": "find_element_by_id",
		"xpath": "find_element_by_xpath"
	}
	multi_search_mapping = {
		"id": "find_elements_by_id",
		"xpath": "find_elements_by_xpath"
	}

	def __init__(self, driver=None, wait_time = 10):
		if driver:
			self.driver = driver
		else:
			options = webdriver.ChromeOptions()
			options.add_argument('-ignore-certificate-errors')
			options.add_argument('-ignore -ssl-errors')
			self.driver = webdriver.Chrome(chrome_options = options)
		self.driver.implicitly_wait(wait_time)

	def open_url(self, url):
		self.driver.get(url)
		self.driver.maximize_window()

	def find_single_element(self, search_type, search_condition):
		search_method = getattr(self.driver, self.single_search_mapping[search_type])
		return search_method(search_condition)

	def find_multi_elements(self, search_type, search_condition):
		search_method = getattr(self.driver, self.multi_search_mapping[search_type])
		return search_method(search_condition)

	def click(self, element):
		element.click()

	def input_text(self, element, text):
		element.clear()
		element.send_keys(text)

	def get_title(self):
		return self.driver.title

	def quit(self):
		self.driver.quit()

	def close(self):
		self.driver.close()


class mainpage(basepage):
	def category_navigate(self, category):
		category_link = self.find_single_element("xpath", f"//div[@class='market-title-box']//div[.='{category}']")
		if category_link:
			self.click(category_link)

	def trade_navigate(self, trade):
		trade_button = self.find_single_element("xpath", f"//div[@class='trade-list']//table//div[.='{trade}']//ancestor::tr//button[.='Trade']")
		if trade_button:
			self.click(trade_button)

