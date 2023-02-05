import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

number = input("Enter a phone number preceded with '+91' format : ")
print()

pnumber = phonenumbers.parse(number, "CH")
country = geocoder.description_for_number(pnumber, "en")
print("Country : ", country)

print("----------------------------------------")

num_operator = phonenumbers.parse(number, "RO")
Operator = carrier.name_for_number(num_operator, "en")
print("Number Operator Company: ", Operator)
