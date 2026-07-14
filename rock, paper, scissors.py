import random

print('''Choose your turn
> rock
> paper
> scissor
> quit
''')

basic_tools = {
    "rock":0,
    "paper":1,
    "scissor":2,
    "quit":3
}
basic_tools2 = ['rock','paper','scissor']

while True:
    player_input = input("> You: ") 
    if player_input in basic_tools:
        
        input_number = basic_tools[player_input]

        i=random.randint(0,2)
        random_input = basic_tools2[i]

    
        if input_number==i:
                print("> Computer: " + random_input)
                print('Draw')
        elif input_number==0 and i == 2:
                print("> Computer: " + random_input)
                print('Player wins!')
        elif input_number==1 and i == 0:
                print("> Computer: " + random_input)
                print('Player wins!')
        elif input_number==2 and i == 1:
                print("> Computer: " + random_input)
                print('Player wins!')
        elif input_number==3:
            quit()
        else:
            print("> Computer: " + random_input)
            print('Computer wins :p')
        break            
    else:
        print("Invalid Input")