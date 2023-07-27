import random

def play():
    user = input("Input 'r' for rock, 'p' for paper, or 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer: 
        return f"It's a tie. Computer chose {computer}"
    
    if is_win(user, computer):
        return f"You won! computer chose {computer}"
    
    return f"You lost, computer chose {computer}"


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'rock'):
        return True
    


for i in range(5):
    print(play())