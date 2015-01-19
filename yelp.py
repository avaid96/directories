import json

def print_business(business):
	print (business['name'])
	print ("Location: "+ business['location']['city'])
	rating= business['rating']
	if rating == 1:
		print (str(rating)+" star.")
	else:
		print (str(rating)+" stars.")

	if 'display_phone' in business:
		print (business['display_phone'])
	print ("\n")

with open("yelp.json", "r") as file:
	yelp=json.load(file)
print ("Welcome to Yelp!"+ str(yelp['total'])+"businesses near you. Displaying the 15 most relevant:")

for business in yelp['businesses']:
	print_business(business)

print ("Evanston or Chicago?")
location=input().lower()

print ("Minimum allowable rating?")
min_rating= float(input())

print ("Keyword?")
keyword=input().lower()

print ("Results:")
for business in yelp['businesses']:
	if (business['location']['city'].lower()==location) and (business['rating'] >= min_rating) and ((keyword in business['name'].lower()) or (keyword in business['snippet_text'].lower()) or (keyword in business['categories'])):
		print_business(business)
