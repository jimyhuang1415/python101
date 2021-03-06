import requests
from bs4 import BeautifulSoup
from selenium import webdriver

page = '2'
url = 'http://class.ruten.com.tw/category/sub00.php?c=00110002&p=' + page

headers = {
	'user-agenr': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

res = requests.get('http://class.ruten.com.tw/category/sub00.php?c=002100010047&p=1', headers=headers);

#print(res.text.encode('latin1').decode('big5'))

browser = webdriver.PhantomJS()
browser.maximize_window()

browser.get(url)

#print(browser.page_source)

soup = BeautifulSoup(browser.page_source, 'html.parser')
result = soup.select('.results-listing')[0]

#print(result)
print('item-name-anchor')
items = result.select('.media-body')

data = []

for item in items:
	print(item.select('.item-name-text')[0].text)
	print(item.select('.item-name-anchor')[0]['href'])
	print(item.select('.rt-text-price')[0].text)

	data.append({
		'name': item.select('.item-name-text')[0].text,
		'link': item.select('.item-name-anchor')[0]['href'],
		'price': item.select('.rt-text-price')[0].text
	})

with open('./ruten.txt', 'w') as f:
	f.write(str(data))