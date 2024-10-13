import random
mobil=input('enter number')
mobillen=len(mobil)
if ((mobillen==11) and (mobil.isdigit()== True)):
	i=mobil[-4:]
	randomnum=random.randint(1111,9999)
password=i+str(randomnum)
print(password)
#elixez9:)
