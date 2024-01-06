import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        master.title("Password Generator")
        master.geometry("400x300")
        master.configure(bg="white")

        # Heading
        self.heading_label = tk.Label(master, text="Password Generator", font=('Arial', 18, 'bold'), bg="white", fg="black")
        self.heading_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Username
        self.username_label = tk.Label(master, text="Enter Username:", font=('Arial', 14), bg="white", fg="black")
        self.username_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        self.username_entry = tk.Entry(master, font=('Arial', 14), bg="white", fg="black")
        self.username_entry.grid(row=1, column=1, padx=10, pady=10, sticky='w')

        # Password Length
        self.length_label = tk.Label(master, text="Enter Password Length:", font=('Arial', 14), bg="white", fg="black")
        self.length_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')

        self.length_entry = tk.Entry(master, font=('Arial', 14), bg="white", fg="black")
        self.length_entry.grid(row=2, column=1, padx=10, pady=10, sticky='w')

        # Generated Password
        self.generated_password_label = tk.Label(master, text="Generated Password:", font=('Arial', 14), bg="white", fg="black")
        self.generated_password_label.grid(row=3, column=0, padx=10, pady=10, sticky='w')

        self.generated_password_entry = tk.Entry(master, font=('Arial', 14), bg="white", fg="green")
        self.generated_password_entry.grid(row=3, column=1, padx=10, pady=10, sticky='w')

        # Buttons
        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password,
                                         font=('Arial', 14), bg="green", fg="black")
        self.generate_button.grid(row=4, column=0, columnspan=2, pady=20)

        self.accept_button = tk.Button(master, text="Accept", command=self.accept_password,
                                       font=('Arial', 14), bg="green", fg="black")
        self.accept_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.reset_button = tk.Button(master, text="Reset", command=self.reset_fields,
                                      font=('Arial', 14), bg="green", fg="black")
        self.reset_button.grid(row=6, column=0, columnspan=2, pady=10)

    def generate_password(self):
        length_str = self.length_entry.get()

        try:
            length = int(length_str)
            if length <= 0:
                raise ValueError("Password length must be a positive integer.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid password length.")
            return

        characters = string.ascii_letters + string.digits + "@#$%^&*?/!"
        generated_password = ''.join(random.choice(characters) for _ in range(length))

        self.generated_password_entry.delete(0, tk.END)
        self.generated_password_entry.insert(0, generated_password)

    def accept_password(self):
        username = self.username_entry.get()
        generated_password = self.generated_password_entry.get()

        if not username or not generated_password:
            messagebox.showerror("Error", "Please enter a username and generate a password.")
        else:
            messagebox.showinfo("Accepted", f"Username: {username}\nPassword: {generated_password}")

    def reset_fields(self):
        self.username_entry.delete(0, tk.END)
        self.length_entry.delete(0, tk.END)
        self.generated_password_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    password_generator = PasswordGenerator(root)
    root.mainloop()
