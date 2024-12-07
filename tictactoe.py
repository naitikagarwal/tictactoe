a =[1, 2, 3, 4, 5, 6, 7, 8, 9]

def print_board():
    print(f"{a[0]} | {a[1]} | {a[2]}")
    print("--|---|---")
    print(f"{a[3]} | {a[4]} | {a[5]}")
    print("--|---|---")
    print(f"{a[6]} | {a[7]} | {a[8]}\n")

#computer --> "O"

def turn(player):
    if player == "O":  
        finalMove = minimax(True)["index"]
        a[finalMove] = player
        print("Compter moves :", finalMove+1)
    else: 
        while True:
            entry = int(input(f"{player}'s turn\nEnter place Value: "))
            if entry in a:
                a[entry - 1] = player
                break
            else:
                print("Please enter a valid place value")

def winnerLogic(player):
    win_possibility = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    return any(a[x[0]] == a[x[1]] == a[x[2]] == player for x in win_possibility)
    #return true if any player is winning

def checkWinner(player):
    if winnerLogic(player):
        print(f"Congratulations! Player {player} wins!")
        return True
    return False

def check_tie():
    return all(isinstance(x, str) for x in a)  
    #it will return true if all digit is replaced with str

def minimax(is_maximizing):
    if winnerLogic("O"):
        return {"score": 1}
    elif winnerLogic("X"):
        return {"score": -1}
    elif check_tie():
        return {"score": 0}
    
    moves = []
    for i in range(9):
        if isinstance(a[i], int):
            move = {}
            move["index"] = i
            a[i] = "O" if is_maximizing else "X"
            # print_board()

            result = minimax(not is_maximizing)
            move["score"] = result["score"]


            a[i] = i + 1

            moves.append(move)
            # print(moves)

    if is_maximizing:
        finalMove = max(moves, key=lambda x: x["score"])
    else:
        finalMove = min(moves, key=lambda x: x["score"])

    return finalMove

print_board()
current_player = "X"

for i in range(9):
    turn(current_player)
    print_board()


    if checkWinner(current_player):
            break
    current_player = "O" if current_player == "X" else "X"
else:
    print("It’s a tie!")
