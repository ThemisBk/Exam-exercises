import requests
r = requests.get('https://drand.cloudflare.com/public/latest', headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = r.json()


round=data['round']
List=[]

for i in range(round-99,round+1):
 url='https://drand.cloudflare.com/public/'
 url=url+str(i)
 List.append(url)

Randomness=[]
for i in range(100):
 r = requests.get(List[i], headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
 data=r.json()
 Randomness.append(data['randomness'])



for i in range(len(Randomness)):
 Randomness[i]=''.join(format(ord(x), 'b') for x in Randomness[i])

Randomness="".join(Randomness)




MaxLenght0=0
Count=0
for i in range(len(Randomness)):
   if Randomness[i]=="0":
    Count+=1
    if Count>MaxLenght0:
     MaxLenght0=Count
   else:
      Count=0



MaxLenght1=0
Count=0
for i in range(len(Randomness)):
   if Randomness[i]=="1":
    Count+=1
    if Count>MaxLenght1:
     MaxLenght1=Count
   else:
    Count=0

print("Η μεγαλύτερη ακολουθία με συνεχόμενα μηδενικά και άσσους είναι αντίστοιχα:", MaxLenght0 , "και", MaxLenght1)