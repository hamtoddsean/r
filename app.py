import requests,os,json,time,csv
headers={'User-Agent':'Mozilla/5.0 (Android 4.0; Mobile; rv:55.0) Gecko/57.0 Firefox/57.0'}
tmv=2
fd=1
clist=[]
pathh='fuler.json'

url1='http://api.hitbtc.com/api/2/public/ticker/BTCUSD'
url='http://api.hitbtc.com/api/2/public/ticker/ETHUSD'
for ki in range(700):
  time.sleep(1)
  if tmv==2:
    rr = requests.get(url)
    ts=rr.json()
    tt=json.dumps(ts)
    print(ts)
    with open(pathh,'a') as dou:
      douu=csv.writer(dou)
      douu.writerow([tt])


