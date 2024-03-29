#A few loops

# Loop through a range of numbers(0 to 9)
for x in range(10):
    print(x)
    

# Loop through a range of numbers(5 to 14)
for x in range(5,15):
    print(x)


#iterate through letters in a string
word = "Seychelles"
for letters in word:
    print(letters)
     

#iterate through a list
zoo =['cow', 'dog', 'elephant', 'zebra']
for animal in zoo:
    print(animal)


#loop while a condition is being met
run = "y"
while run=="y":
    print("this is cool")
    run = input("To run again. Enter 'y': ")
    