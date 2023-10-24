from datetime import date

date.today()

print(date.today())
#print("Today's date is: " + date.today()) é errado

print("agora são " + str(date.today()))

parsecs = 11
lightyears = parsecs * 3.26
print(str(parsecs) + " parsecs is " + str(lightyears) + " lightyears")