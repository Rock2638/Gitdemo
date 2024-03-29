#Guess my number

#state my choice
mynumber=7

#state condition needed to try again 
answer = "Y"

#keeping track of thr number of tries 
mycounter=0

#Keep playing game if answer is yes
while answer.upper() == "Y":

#Ask player for number
    x=int(input("state a number between 1 and 10 "))

#compare number to my number
    if x==mynumber:
        print("your number is equal to my number")

    if x!=mynumber:
        print("wrong mate!")

    if x<mynumber:
        print("your number is less than my number")

    if x>mynumber:
        print("your number is greater than my number")

#Adding up number of tries
    mycounter=mycounter+1
    answer = input("do you want to contintue? [Y/N]")

print("You have played this game " + str(mycounter) +" times")