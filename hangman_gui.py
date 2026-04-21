import tkinter as tk
from tkinter import messagebox
import random

class HangmanGamePro:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Hangman Pro | Studio Syeda")
        self.root.geometry("650x700")
        self.root.configure(bg="#1a252f")
        
        # Colors
        self.bg_color = "#1a252f"
        self.primary_color = "#3498db"
        self.accent_color = "#e67e22"
        self.text_color = "#ecf0f1"
        
        # Game State
        self.words = ["PYTHON", "SOFTWARE", "CODING", "ENGINEER", "DEVELOPER"]
        self.target_word = random.choice(self.words)
        self.guessed_word = ["_"] * len(self.target_word)
        self.attempts_left = 6
        self.guessed_letters = []

        self.setup_ui()

    def setup_ui(self):
        # Header
        tk.Label(self.root, text="HANGMAN PRO", font=("Segoe UI", 32, "bold"), bg=self.bg_color, fg=self.text_color).pack(pady=(40,5))
        tk.Label(self.root, text="Built with Python Automation", font=("Segoe UI", 10), bg=self.bg_color, fg=self.primary_color).pack(pady=(0,20))

        # Drawing Area
        self.canvas = tk.Canvas(self.root, width=220, height=260, bg=self.bg_color, highlightthickness=0)
        self.canvas.pack()
        self.draw_gallows()

        # Word Labels
        self.word_label = tk.Label(self.root, text=" ".join(self.guessed_word), font=("Courier New", 42, "bold"), bg=self.bg_color, fg=self.primary_color)
        self.word_label.pack(pady=20)

        # Input Frame
        input_frame = tk.Frame(self.root, bg=self.bg_color)
        input_frame.pack(pady=10)

        # Entry (Fixed: Focus and Clear)
        self.entry = tk.Entry(input_frame, font=("Arial", 22), width=5, justify="center", bg="#34495e", fg="white", insertbackground="white", relief="flat")
        self.entry.pack(side="left", padx=15)
        self.entry.focus_set()
        
        # Enter Key Binding
        self.root.bind('<Return>', lambda event: self.make_guess())

        # Button
        self.btn = tk.Button(input_frame, text="GUESS", command=self.make_guess, bg=self.accent_color, fg="white", font=("Segoe UI", 12, "bold"), relief="flat", cursor="hand2", padx=25, pady=8)
        self.btn.pack(side="left")

        # Status
        self.status_label = tk.Label(self.root, text=f"Attempts Left: {self.attempts_left}", bg=self.bg_color, fg="#bdc3c7", font=("Segoe UI", 16))
        self.status_label.pack(pady=20)

    def draw_gallows(self):
        self.canvas.create_line(30, 240, 190, 240, fill="white", width=4) 
        self.canvas.create_line(60, 240, 60, 30, fill="white", width=4)  
        self.canvas.create_line(60, 30, 160, 30, fill="white", width=4)  
        self.canvas.create_line(160, 30, 160, 60, fill="white", width=4) 

    def update_drawing(self):
        parts = [
            lambda: self.canvas.create_oval(140, 60, 180, 100, outline="white", width=4), # Head
            lambda: self.canvas.create_line(160, 100, 160, 170, fill="white", width=4),   # Body
            lambda: self.canvas.create_line(160, 110, 130, 140, fill="white", width=4),  # L-Arm
            lambda: self.canvas.create_line(160, 110, 190, 140, fill="white", width=4),  # R-Arm
            lambda: self.canvas.create_line(160, 170, 130, 210, fill="white", width=4),  # L-Leg
            lambda: self.canvas.create_line(160, 170, 190, 210, fill="white", width=4)   # R-Leg
        ]
        err = 6 - self.attempts_left
        if 0 < err <= 6: parts[err-1]()

    def make_guess(self):
        input_text = self.entry.get().upper().strip()
        self.entry.delete(0, tk.END) # Clear box after every guess

        if not input_text or len(input_text) != 1 or not input_text.isalpha():
            messagebox.showwarning("Warning", "Please enter exactly ONE letter.")
            return

        if input_text in self.guessed_letters:
            messagebox.showinfo("Wait", f"'{input_text}' already tried!")
            return

        self.guessed_letters.append(input_text)

        if input_text in self.target_word:
            for i, char in enumerate(self.target_word):
                if char == input_text:
                    self.guessed_word[i] = input_text
            self.word_label.config(text=" ".join(self.guessed_word))
        else:
            self.attempts_left -= 1
            self.status_label.config(text=f"Attempts Left: {self.attempts_left}")
            self.update_drawing()

        # Check Win/Loss
        if "_" not in self.guessed_word:
            messagebox.showinfo("Win!", f"Winner! Word was: {self.target_word}")
            self.root.destroy()
        elif self.attempts_left == 0:
            messagebox.showerror("Lost", f"Game Over! Word was: {self.target_word}")
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    HangmanGamePro(root)
    root.mainloop()