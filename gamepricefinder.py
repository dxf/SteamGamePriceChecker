import requests
chunkone = "https://store.steampowered.com/api/appdetails/?appids="
chunkthree = "&cc=EE&l=english&v=1"
headers = {'user-agent': 'my-app/0.0.1'}
with open('apps.txt','r') as apps:
    apps = list(apps)
final_list = []
for i in apps:
    final_list.append(i.strip())
for app in final_list:
    finalurl = chunkone + app + chunkthree
    print(finalurl)
    r = requests.get(finalurl,headers=headers)
    r = r.json()
    name = r[app]["data"]["name"]
    price = r[app]["data"]["price_overview"]["final"]
    with open('prices.csv','a') as prices:
        prices.write(f'{name},{price},{app}\n')