#Christine is buying fish

fish_list = ["kakatwa", "makro", "karang", "bourswa", "bekin"]
fish_basket = []

for x in range(len(fish_list)):
    print("[" + str(x) +"]" + fish_list[x])

answer = "yes"
while answer=="yes":
    print("which fish do you want? ")
    select = input("Enter the number of the fish you want ")

    fish_basket.append(fish_list[int(select)])
    answer = input("would you like to make another selection? ")

for fish in fish_basket:
    print("I have brought home " + fish)
    