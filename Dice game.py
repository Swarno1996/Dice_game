import random

def roll():
    return random.randint(1 , 6)

while True:
    players = input ('Enter the number of player (2-4): ')
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            print (f'The game is between {players} players')
            break 
        else:
            print('The player number must be between 2 and 4')
    else:
        print ('Enter a valid number')



total_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < total_score:
    for player in range(players):
        print(f"\nIt is player {player + 1}'s turn")
        current_score = 0

        while True:
            next_roll = input ('Do you want to roll. If so press y: ') 
            if next_roll.lower() != 'y':
                break

            value = roll ()
            print (f'You have rolled {value}')
                   
            if value == 1:
                print ('You have rolled a 1, your turn ends')
                break
            else:
                current_score += value
                print (f'Your score is {current_score}')

        player_scores[player] += current_score
        print (f'The total score is {player_scores[player]}')

        if player_scores[player] >= total_score:
            print (f'The player {player +1} has won')
            break  

print ("Final_score:", player_scores)
    












