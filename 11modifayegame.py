import tkinter as tk
from tkinter import messagebox
import random

def start_game(mode):
    global game_mode
    game_mode = mode
    start_frame.pack_forget()
    game_frame.pack()
    reset_game()

def check_winner():
    global winner
    for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                  [0, 3, 6], [1, 4, 7], [2, 5, 8],
                  [0, 4, 8], [2, 4, 6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="red")
            buttons[combo[2]].config(bg="yellow")
            winner = True
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            reset_game()
            return
    if all(button["text"] != "" for button in buttons) and not winner:
        messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
        reset_game()

def get_board_state():
    return [btn["text"] for btn in buttons]

def check_winner_board(board, player):
    for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                  [0, 3, 6], [1, 4, 7], [2, 5, 8],
                  [0, 4, 8], [2, 4, 6]]:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def is_draw(board):
    return all(cell != "" for cell in board)

def empty_cells(board):
    return [i for i, cell in enumerate(board) if cell == ""]

def minimax(board, is_maximizing, depth=0):
    if check_winner_board(board, "O"):
        return 10 - depth, None
    if check_winner_board(board, "X"):
        return -10 + depth, None
    if is_draw(board):
        return 0, None

    if is_maximizing:
        best_score = float("-inf")
        best_move = None
        for move in empty_cells(board):
            board[move] = "O"
            score, _ = minimax(board, False, depth + 1)
            board[move] = ""
            if score > best_score:
                best_score = score
                best_move = move
        return best_score, best_move
    else:
        best_score = float("inf")
        best_move = None
        for move in empty_cells(board):
            board[move] = "X"
            score, _ = minimax(board, True, depth + 1)
            board[move] = ""
            if score < best_score:
                best_score = score
                best_move = move
        return best_score, best_move

def button_click(index):
    global current_player, winner
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()
        if not winner:
            toggle_player()
            if game_mode == "computer" and current_player == "O":
                root.after(500, computer_move)

def computer_move():
    global winner
    if not winner:
        board = get_board_state()
        _, best_move = minimax(board, True)
        if best_move is not None:
            buttons[best_move]["text"] = "O"
            check_winner()
            if not winner:
                toggle_player()

def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player {current_player}'s turn")

def reset_game():
    global current_player, winner
    for button in buttons:
        button.config(text="", bg="SystemButtonFace")
    current_player = "X"
    winner = False
    label.config(text=f"Player {current_player}'s turn")
    if game_mode == "computer" and current_player == "O":
        root.after(500, computer_move)

# GUI Setup
root = tk.Tk()
root.title("TIC-TAC-TOE")
game_mode = None
current_player = "X"
winner = False

# Start Screen
start_frame = tk.Frame(root)
tk.Label(start_frame, text="Choose Game Mode", font=("normal", 18)).pack(pady=10)
tk.Button(start_frame, text="Player vs Player", font=("normal", 14),
          command=lambda: start_game("player")).pack(pady=5)
tk.Button(start_frame, text="Player vs Computer", font=("normal", 14),
          command=lambda: start_game("computer")).pack(pady=5)
start_frame.pack()

# Game Screen
game_frame = tk.Frame(root)
buttons = [tk.Button(game_frame, text="", font=("normal", 25), width=6, height=2,
                     command=lambda i=i: button_click(i)) for i in range(9)]
for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)

label = tk.Label(game_frame, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)
reset_button = tk.Button(game_frame, text="Restart Game", font=("normal", 16), command=reset_game)
reset_button.grid(row=4, column=0, columnspan=3)

root.mainloop()
