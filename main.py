

import tkinter as tk
from tkinter import messagebox

# -----------------------------------  LOGIC PART  ---------------------------------
current_player = 'X'
board = [" " for _ in range(9)]

def check_win():
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # Columns
        (0, 4, 8), (2, 4, 6)]            # Digonals

    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != " ":
            return True
    return False

def is_draw():
    return " " not in board

def on_button_click(i):
    global current_player
    if board[i] == " ":
        board[i] = current_player
        buttons[i].config(text=current_player,fg="#63e9e4" if current_player == "X" else "#f0a824")
        if check_win():
            messagebox.showinfo("Tic Tac Toe", f"Player {current_player} wins!")
            reset_game()
        elif is_draw():
            messagebox.showinfo("Tic Tac Toe", "Draw!")
            reset_game()
        else:
            toggle_turn()


def toggle_turn():
    global current_player
    current_player = "O" if current_player == "X" else "X"
    status_bar.config(text=f"{current_player} Turn")

# Created Function for resetting the game 
def reset_game():
    global board, current_player
    board = [" " for _ in range(9)]
    current_player = "X"
    for button in buttons:
        button.config(text=" ", state=tk.NORMAL)
    status_bar.config(text=f"{current_player} Turn")

# -----------------------------------  GUI PART  ---------------------------------
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("618x700")
root.iconbitmap("tictactoe.ico")
root.config(bg="#1f3741")
frame1 = tk.Frame(root)
label = tk.Label(frame1,text="Start Game or Select player",font=("Helvetica",14,"bold"),fg="#a7bec8",bg="#1f3741",pady=20)
label.pack()
frame1.pack()
frame2 = tk.Frame(root)
frame2.pack(pady=10)
frame3 = tk.Frame(root)
frame3.pack()
frame4 = tk.Frame(root)
frame4.pack(pady=20)

# Created buttons for the Tic Tac Toe board
buttons = []
for i in range(9):
    button = tk.Button(frame2, text='', font=('normal', 40), bg="#1a2a31",width=5, height=2, command=lambda i=i: on_button_click(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Created a Status Bar
status_bar = tk.Label(frame3,text=f"{current_player} Turn",anchor="center",font=("sans-sarif",14),fg="#a7bec8",bg="#1a2a31",padx=20,relief="sunken")
status_bar.pack()

# Created a reset button
reset_button = tk.Button(frame4, text="Reset", font=("sans-sarif",14),fg="#000000",bg="#a7bec8",padx=20 ,command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3)

root.mainloop()        