import random
uppercase=['A','D','F','G','H','I','K','L','M','N','O','L']
lowercase=['a','d','c','v','f','h','g','i','e','q','r','b']
specialcharacters=['@','#','$','%','&']
numbers=['1','2','3','4','5','6','7','8','9','10']
passwordgenerator=random.choice(uppercase)+random.choice(lowercase)+random.choice(specialcharacters)+random.choice(numbers)
passwordgenerator=passwordgenerator+passwordgenerator
print ( passwordgenerator)