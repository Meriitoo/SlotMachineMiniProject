import tkinter as tk
import random
import time

class SlotMachine:
    def __init__(self, root):
        self.root = root
        self.root.title("Slot Machine Game")

        self.icons = ["🍒", "🔔", "🍫", "🎰"]

        self.balance = 1000  # Starting balance
        self.bet_amount = 10
        self.is_spinning = False

        # Create and pack widgets
        self.balance_label = tk.Label(root, text=f"Balance: {self.balance} Euro", font=("Arial", 16))
        self.balance_label.pack(pady=10)

        self.slot_icons = [tk.StringVar() for _ in range(3)]

        self.slot_frame = tk.Frame(root)
        self.slot_frame.pack()

        for i in range(3):
            slot_label = tk.Label(self.slot_frame, textvariable=self.slot_icons[i], font=("Arial", 48))
            slot_label.grid(row=0, column=i, padx=10)

        self.spin_button = tk.Button(root, text="Spin", command=self.spin, font=("Arial", 14))
        self.spin_button.pack(pady=20)

        self.quit_button = tk.Button(root, text="Quit", command=root.quit, font=("Arial", 14))
        self.quit_button.pack(pady=10)

    def spin(self):
        if self.balance >= self.bet_amount and not self.is_spinning:
            self.balance -= self.bet_amount
            self.update_balance()
            self.is_spinning = True

            # Simulate spinning with delay
            spins = [random.choice(self.icons) for _ in range(3)]
            for _ in range(5):
                self.update_icons(spins)
                self.root.update()
                time.sleep(0.2)

            result = [random.choice(self.icons) for _ in range(3)]
            self.update_icons(result)

            if self.check_jackpot(result):
                self.balance += self.bet_amount * 10
                self.update_balance("Jackpot! You won 10x your bet!")
            elif result[0] == result[1] or result[1] == result[2]:
                self.balance += self.bet_amount * 2
                self.update_balance("Congratulations! You won 2x your bet!")
            else:
                self.update_balance("Better luck next time!")

            self.is_spinning = False

    def update_balance(self, message=None):
        self.balance_label.config(text=f"Balance: {self.balance} Euro")
        if message:
            self.show_result(message)

    def update_icons(self, icons):
        for i in range(3):
            self.slot_icons[i].set(icons[i])

    def show_result(self, message):
        result_label = tk.Label(self.root, text=message, font=("Arial", 16))
        result_label.pack(pady=10)
        self.root.after(2000, lambda: result_label.pack_forget())  # Remove result message after 2 seconds

    def check_jackpot(self, icons):
        return all(icon == icons[0] for icon in icons)


if __name__ == "__main__":
    root = tk.Tk()
    slot_machine = SlotMachine(root)
    root.mainloop()
