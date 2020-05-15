import requests

"""
'ConnectTimeout', 'ConnectionError', 'DependencyWarning', 'FileModeWarning', 'HTTPError', 'NullHandler', 
'PreparedRequest', 'ReadTimeout', 'Request', 'RequestException', 'RequestsDependencyWarning', 'Response', 
'Session', 'Timeout', 'TooManyRedirects', 'URLRequired'
'adapters', 'api', 'auth', 'certs', 'chardet', 'check_compatibility', 'codes', 'compat', 'cookies', 'delete',
 'exceptions', 'get', 'head', 'hooks', 'logging', 'models', 'options', 'packages', 'patch', 'post', 'put', 
 'request', 'session', 'sessions', 'status_codes', 'structures', 'urllib3', 'utils', 'warnings'
"""

url = "https://music.163.com/#/song?id=26830207"
url2 = "https://music.163.com/#/song?id=1440443944"
user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
header = {'user-agent':user_agent}

# get
res = requests.get(url,headers = header)
print(res.status_code)
print(res.headers)
content_type = res.headers['Content-Type']
print(content_type)
print(res.content[:500])
print(res.text[:500])
print(res.encoding)
print(res.cookies)

print('-'*33)
# post
res2 = requests.post(url2,headers = header)
print(res2.status_code)
# header 
# res3 = requests.head(url)
# print(res3.status_code)

