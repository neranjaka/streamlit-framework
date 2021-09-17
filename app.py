import requests
#r = requests.get('https://github.com/neranjaka', auth=('user', 'pass'))


#print(r.status_code)

#print(r.headers['content-type'])

#print(r.encoding)

#print(r.text)


#print(r.json())


# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=1RKMGQVQE9C9S5RN'
r = requests.get(url)
data = r.json()

print(data)

print("Hello World!!!")
