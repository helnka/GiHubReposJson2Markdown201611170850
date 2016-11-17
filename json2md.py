#!python3
#encoding:utf-8

import json
import csv

username = 'ytyaru'
filePath = "GitHub.{0}.Repositories.json".format(username)
file = open(filePath, 'r', encoding="UTF-8")
data = json.load(file)
file.close()

filePath = "GitHub.{0}.Repositories.md".format(username)
with open(filePath, 'w', encoding="UTF-8") as file:
	writer = csv.writer(file, delimiter='|', lineterminator='\n')
	writer.writerow(['作成日時', '名前', '説明'])
	writer.writerow(['--------', '----', '----'])
	for i in range(0, len(data)):
		url = "https://github.com/{0}/{1}".format(username, data[i]["name"])
		
		desc = ""
		if data[i]["homepage"]:
			desc = "[{0}]({1})".format(data[i]["description"], data[i]["homepage"])
		else:
			desc = data[i]["description"]
		writer.writerow([data[i]["created_at"], "[{0}]({1})".format(data[i]["name"], url), desc])
