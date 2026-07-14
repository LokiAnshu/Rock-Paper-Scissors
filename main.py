import random

# Menu for the player
print('''Choose your turn
> rock
> paper
> scissors
> quit
''')

# Assigning variables for further use
basic_tools = {
    "rock":0,
    "paper":1,
    "scissors":2,
    "quit":3
}
basic_tools2 = ['rock','paper','scissors']

while True:
    player_input = (input("> You: ")).lower()
    if player_input in basic_tools:

        # Converting the player input into the assigned number
        input_number = basic_tools[player_input]
        
        # Computer's turn
        i=random.randint(0,2)
        random_input = basic_tools2[i]
        print("> Computer: " + random_input)

        # Mapping every outcome     
        if input_number==i:
                print('Draw')
        elif input_number==0 and i == 2:
                print('Player wins!')
        elif input_number==1 and i == 0:
                print('Player wins!')
        elif input_number==2 and i == 1:
                print('Player wins!')
        elif input_number==3:
            quit()
        else:
            print('Computer wins :p')
        break            
    else:
        print("Invalid Input")