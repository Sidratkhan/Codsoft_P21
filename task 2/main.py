import tkinter as tk
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.geometry("300x400")
        master.configure(bg="white")

        self.result_var = tk.StringVar()

        # Entry widget to display the result
        self.result_entry = tk.Entry(master, textvariable=self.result_var, font=('Arial', 20), justify='right', bd=10)
        self.result_entry.grid(row=0, column=0, columnspan=4, sticky='nsew')

        # Buttons
        button_texts = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C', '√', '←'
        ]

        row_val = 1
        col_val = 0
        for text in button_texts:
            tk.Button(master, text=text, command=lambda t=text: self.on_button_click(t), font=('Arial', 16), bd=5,
                      bg="white", fg="black", relief="ridge", width=3, height=2).grid(row=row_val, column=col_val, sticky='nsew')
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Configure rows and columns to expand with window resizing
        for i in range(1, 6):
            master.grid_rowconfigure(i, weight=1)
            master.grid_columnconfigure(i, weight=1)

    def on_button_click(self, text):
        current_input = self.result_var.get()

        if text == '=':
            try:
                result = eval(current_input)
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        elif text == 'C':
            self.result_var.set('')
        elif text == '√':
            try:
                result = math.sqrt(float(current_input))
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        elif text == '←':
            self.result_var.set(current_input[:-1] if current_input else '')
        else:
            self.result_var.set(current_input + text)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
