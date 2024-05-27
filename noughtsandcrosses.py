import random
import os.path
import json
random.seed()

def draw_board(displayboard):
    for row in displayboard:
        print("|".join(row))
    print("-------------")

def welcome(displayboard):
    print("Welcome to Noughts and Crosses!")
    draw_board(displayboard)

def initialise_board(displayboard):
    for i in range(3):
        for j in range(3):
            displayboard[i][j] = ' '
    return displayboard

def get_player_move(displayboard):
    row = int(input("Enter row for your move (0, 1, 2): "))
    col = int(input("Enter column for your move (0, 1, 2): "))
    while displayboard[row][col] != ' ':
        print("The cell is already occupied. Try again.")
        row = int(input("Enter row for your move (0, 1, 2): "))
        col = int(input("Enter column for your move (0, 1, 2): "))
    displayboard[row][col] = 'X'
    return row, col

def choose_computer_move(displayboard):
    row = random.randint(0, 2)
    col = random.randint(0, 2)
    while displayboard[row][col] != ' ':
        row = random.randint(0, 2)
        col = random.randint(0, 2)
    displayboard[row][col] = 'O'
    return row, col

def check_for_win(displayboard, mark):
    for i in range(3):
        if displayboard[i][0] == mark and displayboard[i][1] == mark and displayboard[i][2] == mark:
            return True
    for j in range(3):
        if displayboard[0][j] == mark and displayboard[1][j] == mark and displayboard[2][j] == mark:
            return True
    if displayboard[0][0] == mark and displayboard[1][1] == mark and displayboard[2][2] == mark:
        return True
    if displayboard[0][2] == mark and displayboard[1][1] == mark and displayboard[2][0] == mark:
        return True
    return False 

def check_for_draw(displayboard):
    for i in range(3):
        for j in range(3):
            if displayboard[i][j] == ' ':
                return False
    return True

def play_game(displayboard):
    initialise_board(displayboard)
    welcome(displayboard)
    while True:
        row, col = get_player_move(displayboard)
        draw_board(displayboard)
        if check_for_win(displayboard, 'X'):
            return 1
        if check_for_draw(displayboard):
            return 0
        row, col = choose_computer_move(displayboard)
        draw_board(displayboard)
        if check_for_win(displayboard, 'O'):
            return -1
        if check_for_draw(displayboard):
            return 0

def menu():
    choice = input("Enter 1 to play, 2 to save score, 3 to load leaderboard, q to quit: ")
    return choice

def load_scores():
    leaders = {}
    try:
        with open("leaderboard.txt", "r") as file:
            for line in file:
                name, score = line.strip().split(" ")
                leaders[name] = int(score)
    except FileNotFoundError:
        pass
    return leaders

def save_score(score):
    name = input("Enter your name: ")
    with open("leaderboard.txt", "a") as file:
        file.write(f"{name} {score}\n")

def display_leaderboard(leaders):
    print("LEADERBOARD:")
    for name, score in sorted(leaders.items(), key=lambda x: x[1], reverse=True):
        print(f"{name}: {score}")