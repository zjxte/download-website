import requests
url = 'https://www.logicerp.com/tutorials/2019/01/01/how-to-allow-access-to-sql-server-on-network/'
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
    }
r = requests.get(url=url, headers=headers)
# print(r.text)

with open('SQL.html', 'w', encoding='utf-8') as f:
    f.write(r.text)
