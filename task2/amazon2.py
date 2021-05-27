from lxml import html
import requests
from selenium import webdriver
from pprint import pprint 
import json

op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(options=op)

driver.get('https://www.amazon.com/b?node=21439846011&pf_rd_r=ZVNS4ZA3XZNZ1ZS5143V&pf_rd_p=caa6e87b-5c64-4215-9d4a-b29f6b0c1f24&pd_rd_r=952fd1dc-0474-4028-aa95-a2dc355d539b&pd_rd_w=OYngR&pd_rd_wg=qag1T&ref_=pd_gw_unk')
#laptops
lap = driver.find_element_by_xpath('//a[@aria-label="Laptops"]')
lap_link = lap.get_attribute("href")

#mobile phones
phone = driver.find_element_by_xpath('//a[@aria-label="Mobile Phones"]')
phone_link = phone.get_attribute('href')

#shoes
shoe = driver.find_element_by_xpath('//a[@aria-label="Shoes"]')
shoe_link = shoe.get_attribute('href')


def extractor(link):
	res = []
	driver.get(link)
	author = driver.find_elements_by_xpath('//span[@class="a-profile-name"]')
	for i in author:
		res.append({'author':str(i.text)})
	date = driver.find_elements_by_xpath('//span[@data-hook="review-date"]')
	for i in range(len(res)):
		# res[i]['date'] = str(date[i].text)
		d = ''
		for word in str(date[i].text).split()[-3:]:
			d+=word+' '
		res[i]['date'] = d
	star = []
	us_star = driver.find_elements_by_xpath('//i[@data-hook="review-star-rating"]')
	for i in us_star:
		star.append(str(i.get_attribute('class'))[-15])
	int_star = driver.find_elements_by_xpath('//i[@data-hook="cmps-review-star-rating"]')
	for i in int_star:
		star.append(str(i.get_attribute('class'))[-15])
	for i in range(len(res)):
		res[i]['star'] = str(star[i])
	# lap_item2 = driver.find_element_by_xpath('//span[@data-component-id="2"]/a').get_attribute('href')
	# lap_item3 = driver.find_element_by_xpath('//span[@data-component-id="3"]/a')
	return res

#laptops
driver.get(lap_link)
lap_item_links = driver.find_elements_by_xpath('//span[@data-component-type="s-product-image"]/a')
lap_link_list = []
for i in lap_item_links:
	lap_link_list.append(i.get_attribute('href'))

for i in range(3):
	lap_item_link = lap_link_list[i]
	json_text = json.dumps(extractor(lap_item_link), indent=4)
	f = open('laptop%s.json'%(i+1), 'w')
	f.write(json_text)
	f.close()

#phones
driver.get(phone_link)
phones_item_links = driver.find_elements_by_xpath('//span[@data-component-type="s-product-image"]/a')
phones_link_list = []
for i in phones_item_links:
	phones_link_list.append(i.get_attribute('href'))

for i in range(3):
	phone_item_link = phones_link_list[i]
	json_text = json.dumps(extractor(phone_item_link), indent=4)
	f = open('phone%s.json'%(i+1), 'w')
	f.write(json_text)
	f.close()

#shoes
driver.get(shoe_link)
shoe_item_links = driver.find_elements_by_xpath('//span[@data-component-type="s-product-image"]/a')
shoe_link_list = []
for i in shoe_item_links:
	shoe_link_list.append(i.get_attribute('href'))

for i in range(3):
	shoe_item_link = shoe_link_list[i]
	json_text = json.dumps(extractor(shoe_item_link), indent=4)
	f = open('shoe%s.json'%(i+1), 'w')
	f.write(json_text)
	f.close()	






