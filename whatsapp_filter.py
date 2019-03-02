# -*- coding: utf-8 -*-
from selenium import webdriver
import csv

#list of whatsapp group invite links
links = ["https://chat.whatsapp.com/JCFcDOTQO7aA5etQXeUEyB",
"https://chat.whatsapp.com/55blTpaDk4j791aTpP6usH"]
w, h = 2, len(links);
name = [[0 for x in range(w)] for y in range(h)]
i = 0
driver = webdriver.Chrome()
for x in links:
	driver.get(x)
	name[i][0] = driver.find_element_by_class_name("block__title").text
	name[i][1] = driver.current_url
	i += 1

with open('employee_file2.csv', mode='w', encoding='utf-8') as csv_file:
	fieldnames = ['Name', 'URL']
	writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
	writer.writeheader()
	for x in name:
		if len(x[0]) > 0:
			writer.writerow({'Name': x[0], 'URL': x[1]})

