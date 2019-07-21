import requests

url_to_parse = 'http://adv.pharmsource.com/includes/getFile.cfm?type=a&id={}&CFID=193268&CFTOKEN=56323237'

response = requests.get(url_to_parse.format(19097))
print(response.status_code)
print(response._content)