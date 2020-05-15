#This exercise takes a first and last name from a user and then puts them together in a new variable

#First I prompt the user to start the "Hello Machine"
start = str(input("Welcome to the hello machine, do you want to enter a name? Please enter Y or N"))
#I start a while loop) to begin taking name input
while start == "Y":
    #while True:
    first_name = input("Please enter the first name")
    last_name = input("please enter your second name")
    full_name = first_name + " " + last_name
    print(f"Hi there {full_name}")
    start = input("Welcome to the hello machine, do you want to enter another name? Please enter Y or N")
print(f"Thank you for stopping by the Hello Machine. See you next time!")





