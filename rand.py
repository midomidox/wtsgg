import json
import random
import string
import time
import requests
from bs4 import BeautifulSoup


def main():
	cookies = {'wa_lang_pref': 'it'}
	headers = {
    'Accept': '*/*',
    'Host': 'chat.whatsapp.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15',
    'Accept-Language': 'it-it',
    'Accept-Encoding': '*/*',
    'Connection': 'keep-alive',
}
	url = "https://chat.whatsapp.com/" + ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(22))
	r = requests.get(url,cookies=cookies, headers=headers )
	soup = BeautifulSoup(r.text, "html.parser")
	gentoo = soup.findAll("h2",{"class": "_2yzk"})[0]
	url_photo = soup.find("span", {"class": "_2z9j"})
	print("STATUS {} | URL {}".format(r.status_code, url))
	if len(gentoo.text) == 0:
		print("BAD LINK\n")
		pass
	else:
		output_end =  "\nGOOD LINK!!! | GROUP NAME => {}".format(gentoo.text)
		print(output_end + "\n")
		output_start = "{} | {} | {}".format(gentoo.text, url, str(url_photo).split("background-image: url(")[1].split(')"></span>')[0].replace("amp;", ""))
		file_object = open('stats_log.txt', 'a')
		file_object.write(output_start + "\n")


dump_access = int(input("Amount of requests: "))
for i in range(dump_access):
	main()
