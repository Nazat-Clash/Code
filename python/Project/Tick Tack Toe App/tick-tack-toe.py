import random
import os
import time

def board(box):
    num = 1
    for row in box:
        print("\t"+" | ".join(row))
        num += 1
        if num <= 3:
            print("\t"+"-" * 9)


def empty_space(box):
    return any(" " in row for row in box)

def check_win(box):
    # Check diagonals
    if box[0][0] == box[1][1] == box[2][2] != " " or box[2][0] == box[1][1] == box[0][2] != " ":
        return 'win'
    # Check rows and columns
    for index in range(3):
        if box[index][0] == box[index][1] == box[index][2] != " " or box[0][index] == box[1][index] == box[2][index] != " ":
            return 'win'
    if not empty_space(box):
        return 'Tie'
    return 'nothing'

def write_file(current_choice = None, Tie = False):
    file_name = 'rounds.txt'
    try:
        with open(file_name, 'r') as file:
            round_number = len(file.readlines())
    except FileNotFoundError:
        round_number = 1 # Start from the beginning
    
    # Write the result to the file
    with open('rounds.txt', 'a') as file:
        if Tie:
            file.write(f"Round {round_number}: Tie\n")
        else:
            file.write(f"Round {round_number}: {current_choice} Wins\n")

box = [[" ", " ", " "] for _ in range(3)]

positive_answers = [
    "yes", "yeah", "yep", "yup", "sure", "certainly", 
    "definitely", "absolutely", "affirmative", "indeed", 
    "of course", "for sure", "right", "correct", "ok", 
    "okay", "agreed", "roger", "aye", "uh-huh", 
    "yessir", "yea", "undoubtedly", "by all means", 
    "naturally", "exactly", "you bet", "without a doubt", 
    "totally", "positively", "fine", "all right", "very well", 
    "unquestionably", "indubitably", "gladly", "willingly", 
    "just so", "righto", "affirmatively", "irrefutably", 
    "unreservedly", "decidedly", "unmistakably", "aye aye", 
    "beyond doubt", "gladly", "with pleasure", "by all means", 
    "assuredly", "yeppers", "yupper", "okay dokey", "right on", 
    "alright", "very well", "as you say", "certainly so", 
    "definitely so", "naturally so", "most assuredly", 
    "to be sure", "verily", "yea verily", "uh-huh", "ye", 
    "okay then", "fine by me", "you betcha", "count on it", 
    "totally", "without fail", "you got it", "I'm in", 
    "sounds good", "sounds right", "that’s right", "I agree", 
    "so it is", "precisely", "just so", "amen", "hallelujah",
    "exactly right", "true", "very true", "absolutely right", 
    "you’re right", "I accept", "I consent", "I concur", 
    "positive", "indeed yes", "no doubt", "beyond question", 
    "beyond any doubt", "most certainly", "without reservation", 
    "most definitely", "in truth", "without a question", 
    "beyond shadow of doubt", "as a matter of fact", 
    "in fact", "decidedly yes", "definitively yes", 
    "categorically yes", "clearly yes", "obviously yes", 
    "evidently yes", "undeniably yes", "undoubtedly yes", "y"
]

current_choice = random.choice(['X', 'O'])

play_again = False

while True:
    os.system('clear')
    print("Current Player:", current_choice)
    board(box)

    try:
        p_row = int(input("Please enter row number (1-3): "))
        if p_row not in (1, 2, 3):
            print("Error: Invalid row number. Row number should be between 1 and 3.")
            time.sleep(0.75)
            continue
        
        p_col = int(input("Please enter column number (1-3): "))
        if p_col not in (1, 2, 3):
            print("Error: Invalid column number. Column number should be between 1 and 3.")
            time.sleep(0.7)
            continue
        
        if box[p_row - 1][p_col - 1] == " ":
            box[p_row - 1][p_col - 1] = current_choice
            os.system('clear')
            board(box)

            result = check_win(box)
            if result == 'win':
                time.sleep(0.7)
                print(f"{current_choice} Wins!")
                write_file(current_choice)
                play_again = True
            elif result == 'Tie':
                time.sleep(0.7)
                print("It's a tie!")
                write_file(Tie = True)
                play_again = True
            else:
                result = check_win(box)
                current_choice = 'X' if current_choice == 'O' else 'O'
        else:
            print("Error: Space is already occupied.")
            time.sleep(0.7)
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(0.75)
    except KeyboardInterrupt:
        print("\nGame interrupted.")
        break
    if play_again:
        play_again = False
        time.sleep(1)
        box = [[" " for _ in range(3)] for _ in range(3)]
        current_choice = random.choice(['X', 'O'])
        if choice := input("Want to play again?: ").lower() in positive_answers:
            continue
        else:
            break