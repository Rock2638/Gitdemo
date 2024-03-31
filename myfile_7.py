#store the file path associated with the file
file= '../Resources/input.txt'

#open the file in read mode and store content in variable text
with open(file, 'r') as text:

 #this stores a reference to a file stream
    print(text)

#store all the text in a variable called lines
    lines=text.read()

#print the contents of the text file
    print(lines) 