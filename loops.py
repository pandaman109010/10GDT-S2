#loops and indents
#authur: panda
#date: 20/09/24
#v2
#TODO:
    #get user imput (name)
    #ask for two numbers
    #add the unbers together

#ask user imput
name = input("whats your name? ")
print(f"hi {name}.") #f stands for format

#ask for two numbers
num_1 = int(input("what is your fav number "))
num_2 = int(input("give me another one "))

#add numbers together
sum = num_1 + num_2
print(f"they equal = {sum}.")
x = 1

#for loops repeat for a set unber of times
for mane_of_loop in range(5):
    print (x+1)

#while loop. runs untill contisions are met
keep_going = ""
while keep_going == "":
    print("looping")

    keep_going = input("more. if so press enter")


