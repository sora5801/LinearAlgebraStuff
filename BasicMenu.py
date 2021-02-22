

# Creator: Matthew Fu
"Date Created: 10/13/2020"
"Purpose: This program will be a basic menu program that is stored with the important information that I want. "

importantInformation = {}  # The information that is most important to me.
HelpfulCommands = {"A": "Assembly information", "B": "Bioinformatics stuff", "C": "Calculate Probabilities",
                   "F" : "Finance Stuff", "G" : "Graph theory stuff",
                   "L" : "Linear Algebra stuff", "M" : "Machine learning Stuff", "P": "Physics Stuff",
                   "T" : "Topology stuff"
                   }  # This is a dictionary of helpful commands
while True:
    userInput = input("Input something. Input 'HelpfulCommands' for some suggestions\n")
    if userInput == "HelpfulCommands" or userInput == "HC" or userInput == "helpfulCommands" or userInput == "helpfulcommands" or userInput == "hc":
        for item in HelpfulCommands.items():
            print(item)
    elif userInput == "A" or userInput == "a":
        print("Here are some assembly stuff")
    elif userInput == "C" or userInput == "c":
        print("What are the probabilities that you want to calculate?")
    elif userInput == "L" or userInput == "l":
        print("Here some linear Algebra stuff")
    elif userInput == "M" or userInput == "m":
        print("Here are some Machine Learning stuff")
    elif userInput == "P" or userInput == "p":
        print("Here are some physics stuff")
    elif userInput == "exit" or userInput == "Exit":
        print("Goodbye!")
        break
    else:
        print("Invalid input")


