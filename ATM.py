import tkinter as tk
from tkinter import messagebox

class ATM:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM")
        self.root.geometry("350x450")
        self.root.config(bg="#2C3E50")

        self.balance = 10000
        self.pin = "1234"
        self.attempts = 3

        self.login_screen()

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def login_screen(self):
        self.clear()

        tk.Label(
            self.root,
            text="ATM MACHINE",
            font=("Arial", 18, "bold"),
            bg="#2C3E50",
            fg="white"
        ).pack(pady=30)

        tk.Label(
            self.root,
            text="Enter PIN",
            font=("Arial", 12),
            bg="#2C3E50",
            fg="white"
        ).pack()

        self.pin_entry = tk.Entry(
            self.root,
            show="*",
            font=("Arial", 14),
            justify="center"
        )
        self.pin_entry.pack(pady=10)

        tk.Button(
            self.root,
            text="Login",
            command=self.check_pin,
            bg="#27AE60",
            fg="white",
            width=15
        ).pack(pady=10)

        self.msg = tk.Label(self.root, bg="#2C3E50", fg="red")
        self.msg.pack()

    def check_pin(self):
        if self.pin_entry.get() == self.pin:
            self.menu()
        else:
            self.attempts -= 1
            if self.attempts == 0:
                messagebox.showerror("Error", "Account Locked")
                self.root.destroy()
            else:
                self.msg.config(
                    text=f"Wrong PIN! {self.attempts} attempts left"
                )

    def menu(self):
        self.clear()

        buttons = [
            ("Check Balance", self.show_balance, "#9B59B6"),
            ("Deposit", self.deposit_screen, "#1ABC9C"),
            ("Withdraw", self.withdraw_screen, "#E67E22"),
            ("Exit", self.exit_atm, "#E74C3C")
        ]

        tk.Label(
            self.root,
            text="MAIN MENU",
            font=("Arial", 18, "bold"),
            bg="#2C3E50",
            fg="white"
        ).pack(pady=20)

        for text, cmd, color in buttons:
            tk.Button(
                self.root,
                text=text,
                command=cmd,
                bg=color,
                fg="white",
                width=20,
                height=2
            ).pack(pady=10)

    def show_balance(self):
        messagebox.showinfo(
            "Balance",
            f"Current Balance: ₹{self.balance}"
        )

    def transaction_screen(self, title, action):
        self.clear()

        tk.Label(
            self.root,
            text=title,
            font=("Arial", 16, "bold"),
            bg="#2C3E50",
            fg="white"
        ).pack(pady=20)

        self.amount_entry = tk.Entry(
            self.root,
            font=("Arial", 14),
            justify="center"
        )
        self.amount_entry.pack(pady=10)

        tk.Button(
            self.root,
            text="Submit",
            command=action,
            bg="#27AE60",
            fg="white",
            width=15
        ).pack(pady=10)

        tk.Button(
            self.root,
            text="Back",
            command=self.menu,
            width=10
        ).pack()

    def deposit_screen(self):
        self.transaction_screen("Deposit Money", self.deposit)

    def withdraw_screen(self):
        self.transaction_screen("Withdraw Money", self.withdraw)

    def deposit(self):
        try:
            amount = float(self.amount_entry.get())
            if amount > 0:
                self.balance += amount
                messagebox.showinfo("Success", "Money Deposited")
                self.menu()
            else:
                messagebox.showerror("Error", "Invalid Amount")
        except:
            messagebox.showerror("Error", "Enter Numbers Only")

    def withdraw(self):
        try:
            amount = float(self.amount_entry.get())

            if amount <= 0:
                messagebox.showerror("Error", "Invalid Amount")

            elif amount > self.balance:
                messagebox.showerror("Error", "Insufficient Balance")

            else:
                self.balance -= amount
                messagebox.showinfo("Success", "Money Withdrawn")
                self.menu()

        except:
            messagebox.showerror("Error", "Enter Numbers Only")

    def exit_atm(self):
        self.root.destroy()

root = tk.Tk()
ATM(root)
root.mainloop()