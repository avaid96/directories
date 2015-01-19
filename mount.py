
import json
with open("mountain.json", "r") as file:
	m=json.load(file)

# print
def print_mountain(mountain):
	for mountain in mountain['mountains']:
		print ("Mountain name "+(mountain['name']))
		mh=(float(mountain['height'])*0.3048)
		print ("Mountain height: "+(mountain['height'])+" feet")
		print ("In m: "+str(mh))
		print ("\n")
# sort
def sort_mountain(mountain):
	namelist=[]
	for mountain in mountain['mountains']:
		namelist+=[mountain['name']]
	namelist=sorted(namelist)
	print(namelist)

# main
print("Display list by height?")
usrin1=input().lower()

if((usrin1=="y") or (usrin1=="yess") or (usrin1=="yes") or (usrin1=="ye")):
	print_mountain(m)

print("Display list alphabetically?")
usrin2=input().lower()

if((usrin2=="y") or (usrin2=="yess") or (usrin2=="yes") or (usrin2=="ye")):
	sort_mountain(m)




