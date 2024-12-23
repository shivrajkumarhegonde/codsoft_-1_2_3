import tkinter as tk
from tkinter import messagebox
import math
import time


class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe Simple Game By Shiv")
        self.window.geometry("400x500")
        self.window.configure(bg="#2c3e50")  # Dark background

        # Game state variables
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = "O"  # Human starts as "O"

        # Header Label
        self.header_label = tk.Label(
            self.window,
            text="Tic-Tac-Toe By Shiv",
            font=("Arial", 24, "bold"),
            bg="#2c3e50",
            fg="#ecf0f1"
        )
        self.header_label.pack(pady=20)

        # Create Board
        self.board_frame = tk.Frame(self.window, bg="#2c3e50")
        self.board_frame.pack(pady=20)
        self.create_board()

        # Footer Label
        self.footer_label = tk.Label(
            self.window,
            text="You are 'O'. AI is 'X'. Good luck!",
            font=("Arial", 12),
            bg="#2c3e50",
            fg="#ecf0f1"
        )
        self.footer_label.pack(pady=20)

    def create_board(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(
                    self.board_frame,
                    text=" ",
                    font=("Arial", 20, "bold"),
                    height=2,
                    width=5,
                    bg="#3498db",  # Blue color
                    fg="#ecf0f1",  # White text
                    activebackground="#2980b9",  # Darker blue when clicked
                    activeforeground="#ecf0f1",
                    command=lambda i=i, j=j: self.make_move(i, j)
                )
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons[i][j] = button

    def make_move(self, row, col):
        if self.board[row][col] == " " and self.current_player == "O":
            self.board[row][col] = "O"
            self.buttons[row][col].config(text="O", state="disabled", disabledforeground="#2ecc71")
            if self.check_winner():
                self.end_game("You win!")
                return
            if self.is_draw():
                self.end_game("It's a draw!")
                return
            self.current_player = "X"
            # Delay the AI's move
            self.window.after(1000, self.ai_move)  # 1-second delay

    def ai_move(self):
        best_move = self.find_best_move()
        if best_move:
            row, col = best_move
            self.board[row][col] = "X"
            self.buttons[row][col].config(text="X", state="disabled", disabledforeground="#e74c3c")
        if self.check_winner():
            self.end_game("AI wins!")
            return
        if self.is_draw():
            self.end_game("It's a draw!")
            return
        self.current_player = "O"

    def check_winner(self):
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] != " ":
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] != " ":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != " ":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != " ":
            return True
        return False

    def is_draw(self):
        return all(cell != " " for row in self.board for cell in row)

    def minimax(self, board, depth, is_maximizing, alpha, beta):
        winner = self.get_winner(board)
        if winner == "X":
            return 10 - depth
        if winner == "O":
            return depth - 10
        if self.is_draw():
            return 0

        if is_maximizing:
            max_eval = -math.inf
            for i in range(3):
                for j in range(3):
                    if board[i][j] == " ":
                        board[i][j] = "X"
                        eval = self.minimax(board, depth + 1, False, alpha, beta)
                        board[i][j] = " "
                        max_eval = max(max_eval, eval)
                        alpha = max(alpha, eval)
                        if beta <= alpha:
                            break
            return max_eval
        else:
            min_eval = math.inf
            for i in range(3):
                for j in range(3):
                    if board[i][j] == " ":
                        board[i][j] = "O"
                        eval = self.minimax(board, depth + 1, True, alpha, beta)
                        board[i][j] = " "
                        min_eval = min(min_eval, eval)
                        beta = min(beta, eval)
                        if beta <= alpha:
                            break
            return min_eval

    def find_best_move(self):
        best_val = -math.inf
        best_move = None
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    self.board[i][j] = "X"
                    move_val = self.minimax(self.board, 0, False, -math.inf, math.inf)
                    self.board[i][j] = " "
                    if move_val > best_val:
                        best_val = move_val
                        best_move = (i, j)
        return best_move

    def get_winner(self, board):
        for row in board:
            if row[0] == row[1] == row[2] and row[0] != " ":
                return row[0]
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
                return board[0][col]
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
            return board[0][2]
        return None

    def end_game(self, message):
        messagebox.showinfo("Game Over", message)
        self.window.destroy()

    def run(self):
        self.window.mainloop()


# Run the game
if __name__ == "__main__":
    game = TicTacToe()
    game.run()
