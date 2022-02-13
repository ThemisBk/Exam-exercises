import requests,math
r = requests.get('https://drand.cloudflare.com/public/latest', headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = r.json()

round=data['round']
List=[]

for i in range(round-19,round+1):
 url='https://drand.cloudflare.com/public/'
 url=url+str(i)
 List.append(url)

Randomness=[]
for i in range(20):
 r = requests.get(List[i], headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
 data=r.json()
 Randomness.append(data['randomness'])

Variable="".join(Randomness)
 

NewList=[]
for i in range(len(Variable)):
 NewList.append(Variable[i])



Count0=NewList.count("0")
Count1=NewList.count("1")
Count2=NewList.count("2")
Count3=NewList.count("3")
Count4=NewList.count("4")
Count5=NewList.count("5")
Count6=NewList.count("6")
Count7=NewList.count("7")
Count8=NewList.count("8")
Count9=NewList.count("9")
CountA=NewList.count("a")
CountB=NewList.count("b")
CountC=NewList.count("c")
CountD=NewList.count("d")
CountE=NewList.count("e")
CountF=NewList.count("f")
TotalDigits=len(NewList)
Entropy0=Count0/TotalDigits*math.log(1/(Count0/TotalDigits),2)
Entropy1=Count1/TotalDigits*math.log(1/(Count1/TotalDigits),2)
Entropy2=Count2/TotalDigits*math.log(1/(Count2/TotalDigits),2)
Entropy3=Count3/TotalDigits*math.log(1/(Count3/TotalDigits),2)
Entropy4=Count4/TotalDigits*math.log(1/(Count4/TotalDigits),2)
Entropy5=Count5/TotalDigits*math.log(1/(Count5/TotalDigits),2)
Entropy6=Count6/TotalDigits*math.log(1/(Count6/TotalDigits),2)
Entropy7=Count7/TotalDigits*math.log(1/(Count7/TotalDigits),2)
Entropy8=Count8/TotalDigits*math.log(1/(Count8/TotalDigits),2)
Entropy9=Count9/TotalDigits*math.log(1/(Count9/TotalDigits),2)
EntropyA=CountA/TotalDigits*math.log(1/(CountA/TotalDigits),2)
EntropyB=CountB/TotalDigits*math.log(1/(CountB/TotalDigits),2)
EntropyC=CountC/TotalDigits*math.log(1/(CountC/TotalDigits),2)
EntropyD=CountD/TotalDigits*math.log(1/(CountD/TotalDigits),2)
EntropyE=CountE/TotalDigits*math.log(1/(CountE/TotalDigits),2)
EntropyF=CountF/TotalDigits*math.log(1/(CountF/TotalDigits),2)
Entropy=Entropy0+Entropy1+Entropy2+Entropy3+Entropy4+Entropy5+Entropy6+Entropy7+Entropy8+Entropy9+EntropyA+EntropyB+EntropyC+EntropyD+EntropyE+EntropyF
print("Η εντροπία του κειμένου είναι => ",Entropy)













 


