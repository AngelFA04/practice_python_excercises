def menu():
    print("""
             SELECT ONE CHOICE:
             1 - Rock
             2 - Paper
             3 - Scissors
          """)


def ask_player_moves():
    menu()

    choices = {'1': 'ROCK', '2': 'PAPER', '3': 'SCISSORS'}

    move_p1 = choices.get(input('Turn player 1: '))
    move_p2 = choices.get(input('Turn player 2: '))

    return move_p1.upper(), move_p2.upper()


def select_winner(m1, m2):
    winner = None
    # winners = [('ROCK', 'SCISSORS'),('SCISSORS', 'PAPER'),('PAPER', 'ROCK')]

    if m2 == 'ROCK' and m1 == 'PAPER':
        winner = 'Player 1'
    elif m2 == 'PAPER' and m1 == 'ROCK':
        winner = 'Player 2'

    elif m1 == 'SCISSORS' and m2 == 'PAPER':
        winner = 'Player 1'

    elif m2 == 'SCISSORS' and m1 == 'PAPER':
        winner = 'Player 2'

    elif m1 == 'ROCK' and m2 == 'SCISSORS':
        winner = 'Player 1'

    elif m2 == 'ROCK' and m1 == 'SCISSORS':
        winner = 'Player 2'

    return winner


if __name__ == "__main__":
    winner = None
    while not winner:
        m1, m2 = ask_player_moves()
        winner = select_winner(m1, m2)

    print(f'The winner is {winner}')
