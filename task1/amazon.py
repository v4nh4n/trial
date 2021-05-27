from lxml import html
import requests
from selenium import webdriver
from pprint import pprint 
import json

op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(options=op)

res = []
x = []  

driver.get("https://www.amazon.com/AmazonBasics-Velvet-Suit-Hangers-50-Pack/dp/B00FXNAAW2/ref=sr_1_13?dchild=1&keywords=amazonbasics&pd_rd_r=50e10e28-e421-4697-aadf-f61021911cb7&pd_rd_w=IQ1rT&pd_rd_wg=xxxvD&pf_rd_p=9349ffb9-3aaa-476f-8532-6a4a5c3da3e7&pf_rd_r=1ZDBAJP7AFJCN0BNJT2K&qid=1621683026&sr=8-13&th=1")
el = driver.find_elements_by_class_name("a-profile-name")
el_list = [] 
for i in el:
	# print(i.text)
	el_list.append(i.text)
x.append(el_list)

dates = driver.find_elements_by_css_selector("span[data-hook='review-date']")
dates_list = []
for i in dates:
	# print(i.text)
	date = ""
	for word in str(i.text).split()[-3:]:
		date+=word+" "
	dates_list.append(date)
x.append(dates_list)

stars_usa = driver.find_elements_by_css_selector("div[class='a-row']>a[class='a-link-normal']")
stars_usa_list = []
for i in stars_usa:
	# print(i.get_attribute('title'))
	stars_usa_list.append(str(i.get_attribute('title'))[0])

stars_int = driver.find_elements_by_xpath('//*[@data-hook="cmps-review-star-rating"]')
stars_int_list = []
for i in stars_int:
	# print(i.get_attribute('class'))
	stars_int_list.append(str(i.get_attribute('class'))[-15])

stars = stars_usa_list +stars_int_list
x.append(stars)


# print(x)

for i in range(len(x[0])):
	d = {}
	d['author']=x[0][i]
	d['date']=x[1][i]
	d['stars']=x[2][i]
	res.append(d)
pprint(res)

j = json.dumps(res, indent=4)
print(j)

f = open('data.json', 'w')
f.write(j)
f.close()



# [0][0]
# [1][0]
# [2][0]
# [3][0]


