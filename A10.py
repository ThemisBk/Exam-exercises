with open('C:/web/two_cities_ascii.txt') as f:
  data=f.read()


List=[]
for i in data:
 List.append(i)




for i in range(len(List)):
 List[i]=' '.join(format(ord(x), 'b') for x in List[i])   

for i in range(len(List)):
 if len(List[i])==6:
  List[i]="0"+List[i]
 elif len(List[i])==4:
  List[i]="000"+List[i]


for i in range(len(List)):
 List[i]=str(List[i])[:2]+str(List[i])[5:]



string="".join(List)

n=16
NewList=([string[i:i+n] for i in range(0, len(string), n)])


for i in range(len(NewList)):
 NewList[i]=int(NewList[i],2)
 

 
Zigoi=0
D3=0
D5=0
D7=0
for i in range(len(NewList)):
 if NewList[i]%2==0:
  Zigoi=Zigoi+1
 if NewList[i]%3==0:
  D3=D3+1
 if NewList[i]%5==0:
  D5=D5+1
 if NewList[i]%7==0:
  D7=D7+1

                  
print("Το ποσοστό των ζυγών αριθμών είναι=>",Zigoi/len(NewList)*100,"%")
print("Το ποσοστό των αριθμών που διαιρούνται με το 3 είναι=>",D3/len(NewList)*100,"%")
print("Το ποσοστό των αριθμών που διαιρούνται με το 5 είναι=>",D5/len(NewList)*100,"%")
print("Το ποσοστό των αριθμών που διαιρούνται με το 7 είναι=>",D7/len(NewList)*100,"%")
