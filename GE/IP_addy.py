import requests 

proxies={
    'https':'77.120.152.161:33265',
    'https':'77.120.152.161:33265'
}

url = 'https://httpbin.org/ip'
resp = requests.get(url,proxies = proxies)
print(resp.json)
print(resp.text)

#url = 'https://httpbin.org/ip'

#resp = requests.get(url)

#print(resp.json)
#print (resp.text)