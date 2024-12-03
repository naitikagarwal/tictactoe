a =[1, 2, 3, 4, 5, 6, 7, 8, 9]

def print_board():
    print(f"{a[0]} | {a[1]} | {a[2]}")
    print("--|---|---")
    print(f"{a[3]} | {a[4]} | {a[5]}")
    print("--|---|---")
    print(f"{a[6]} | {a[7]} | {a[8]}")

def turn(player):
    while True:
        entry = int(input(f"{player}'s turn\nEnter place Value: "))
        if entry in a:
            a[entry - 1] = player
            break
        else:
            print("Please enter the valid place value")

def check_winner(player):
    winPossibility = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]
    ]
    
    for x in winPossibility:
        if a[x[0]] == a[x[1]] == a[x[2]] == player:
            print(f"Congratulations! Player {current_player} wins!")
            return True
    return False



print_board()
current_player = "X"

for i in range(9):
    turn(current_player)
    print_board()


    if check_winner(current_player):
            break
    current_player = "O" if current_player == "X" else "X"
else:
    print("It’s a tie!")
