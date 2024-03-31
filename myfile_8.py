#import the random and string modules
import random
import string

# Use the string module's custom method: ".ascii_letters"
print(string.ascii_letters)

# Use the random module's custom method randint
for x in range(10):
    print(random.randint(0,10)) 
