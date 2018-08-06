import random

def main():
    numOfDie = int(input("How many dice would you like to roll (each die has 6 sides)? "))

    while True:
        results = []
        total = 0

        for i in range(numOfDie):   #Rolls the dice
            dieResult = random.randint(1,6)
            total += dieResult
            results.append(str(dieResult))  #lazy way of making list type string

        print("You have rolled a " + ', '.join(results))
        print("The total is " + str(total))

        if input("Would you like to roll again? ").lower() == "no":
            break

main()