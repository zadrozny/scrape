# Scrapes Meetup group member ID's and time of last visit

import re 
import time
from config import myemail, mypassword, meetup_url
from lxml import html
from random import randrange # Vary the time between scrapes
from selenium import webdriver


def main():
	driver = webdriver.Firefox() # PhantomJS doesn't always work
	driver.get("https://secure.meetup.com/login/")

	username = driver.find_element_by_id('email')
	username.send_keys(myemail)

	password = driver.find_element_by_id('password')
	password.send_keys(mypassword)
	password.submit()

	with open('scrape_members_output.txt', 'a') as f:
		
		start = 6120
		last = 6160 # Change to 6120 later 
		offset = 20 # Members per page
		for n in range(start, last, offset):
			
			url = (meetup_url + '/members/?offset=' 
					+ str(n) + '&desc=0&sort=name')

			driver.get(url)
			page = driver.page_source.encode('utf-8')
			tree = html.fromstring(page)


			member_ids = re.findall('id="member_(\d*)"', page)

			for i in member_ids:
				path = '//*[@id="memberInfo_'+i+'"]/div[2]/ul/li[2]/span/text()'
				date = tree.xpath(path) # Date of last visit 
				if date: 
					date = date[0].strip('\n\n')
				else:
					date = "Not found"

				path = '//*[@id="memberInfo_'+i+'"]/div[2]/h4/a/text()'
				name = tree.xpath(path)
				if name:
					name = name[0].encode('utf-8')
				else:
					name = "Not found"
				
				f.write(str(i) + ', ' + name + ', ' + date + '\n')


			time.sleep(randrange(2, 7)) # Don't abuse!

		driver.close()


if __name__ == '__main__':
	main()