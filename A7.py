import json


with open("C:/web/doc.txt") as f:
 data=f.read()

data=data.splitlines()
lst=[]
for i in range(len(data)):
 lst.append(json.loads(data[i]))

print("Πιό από τα διαθέσιμα κλειδιά σας ενδιαφέρει;")
print(lst[0].keys())
answer=input()

ValuesOfWantedKey=[]
for i in range(len(lst)):
 ValuesOfWantedKey.append(lst[i][answer])



if isinstance(ValuesOfWantedKey[0], int):
 ValuesSorted=sorted(ValuesOfWantedKey)
 MinValue=ValuesSorted[0]
 MaxValue=ValuesSorted[-1]
else:
 ValuesSorted=sorted(ValuesOfWantedKey,key=len)
 MinValue=ValuesSorted[0]
 MaxValue=ValuesSorted[-1]

Popular=max(ValuesSorted, key=ValuesSorted.count)
if ValuesSorted.count(Popular)==1:
 print("Δεν υπάρχει δημοφιλέστερη τιμή καθώς όλες εμφανίζοντε μία φορα.")
else:
 print("Η δημοφιλέστερη τιμή είναι η: ",Popular)

print("Η μικρότερη τιμή του",answer,"είναι η τιμή: ",MinValue)
print("Η μεγαλύτερη τιμή του",answer,"είναι η τιμή: ",MaxValue)