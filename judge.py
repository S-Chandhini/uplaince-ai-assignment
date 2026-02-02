import tkinter as tk
from tkinter import messagebox
import random


class GameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("RPS Bomb Arena")
        self.root.geometry("400x450")

        # Game State
        self.user_has_bomb = True
        self.bot_has_bomb = True
        self.moves = ["rock", "paper", "scissors"]

        # UI Elements
        self.status_label = tk.Label(
            root, text="WELCOME TO THE ARENA", font=("Arial", 14, "bold"))
        self.status_label.pack(pady=10)

        self.bomb_frame = tk.Frame(root)
        self.bomb_frame.pack(pady=10)

        self.u_bomb_label = tk.Label(
            self.bomb_frame, text="YOUR BOMB: READY", fg="green")
        self.u_bomb_label.grid(row=0, column=0, padx=20)

        self.b_bomb_label = tk.Label(
            self.bomb_frame, text="BOT BOMB: READY", fg="green")
        self.b_bomb_label.grid(row=0, column=1, padx=20)

        self.result_text = tk.Label(
            root, text="Make your move...", font=("Arial", 12), fg="blue")
        self.result_text.pack(pady=20)

        # Buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Rock", width=10, command=lambda: self.play(
            "rock")).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(btn_frame, text="Paper", width=10, command=lambda: self.play(
            "paper")).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(btn_frame, text="Scissors", width=10, command=lambda: self.play(
            "scissors")).grid(row=1, column=0, padx=5, pady=5)

        self.bomb_btn = tk.Button(btn_frame, text="BOMB", width=10,
                                  bg="red", fg="white", command=lambda: self.play("bomb"))
        self.bomb_btn.grid(row=1, column=1, padx=5, pady=5)

    def play(self, user_choice):
        # Bot Logic
        pool = self.moves.copy()
        if self.bot_has_bomb:
            pool.append("bomb")
        bot_choice = random.choice(pool)

        # Logic for Winner
        winner_msg = ""

        if user_choice == bot_choice:
            winner_msg = "its a draw match"
            if user_choice == "bomb":
                self.user_has_bomb = False
                self.bot_has_bomb = False
        elif user_choice == "bomb":
            winner_msg = "user won"
            self.user_has_bomb = False
        elif bot_choice == "bomb":
            winner_msg = "bot won"
            self.bot_has_bomb = False
        elif (user_choice == "rock" and bot_choice == "scissors") or \
             (user_choice == "paper" and bot_choice == "rock") or \
             (user_choice == "scissors" and bot_choice == "paper"):
            winner_msg = "user won"
        else:
            winner_msg = "bot won"

        # Update UI
        self.update_ui(user_choice, bot_choice, winner_msg)

        # Ask to play again
        if messagebox.askyesno("Round Over", f"Bot chose: {bot_choice}\nResult: {winner_msg}\n\nPlay another round?"):
            pass
        else:
            self.root.quit()

    def update_ui(self, u, b, res):
        self.result_text.config(text=f"You: {u} | Bot: {b}\n\n{res}")

        if not self.user_has_bomb:
            self.u_bomb_label.config(text="YOUR BOMB: EMPTY", fg="red")
            self.bomb_btn.config(state="disabled")  # Deactivate button

        if not self.bot_has_bomb:
            self.b_bomb_label.config(text="BOT BOMB: EMPTY", fg="red")


if __name__ == "__main__":
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()
