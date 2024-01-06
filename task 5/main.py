import tkinter as tk
from tkinter import messagebox
import random

class QuizGameGUI:
    def __init__(self, master, questions):
        self.master = master
        self.questions = questions
        self.current_question_index = 0
        self.score = 0

        master.title("Quiz Game")
        master.geometry("600x400")
        master.configure(bg="#d3ffd3")

        self.question_number_label = tk.Label(master, text="", font=('Arial', 18, 'bold'), bg="#d3ffd3", fg="#003366", pady=10)
        self.question_number_label.pack()

        self.question_label = tk.Label(master, text="", font=('Arial', 20, 'italic'), bg="#d3ffd3", fg="#003366", padx=20, pady=10)
        self.question_label.pack()

        self.radio_var = tk.StringVar()
        self.radio_buttons = []
        for i in range(4):
            radio_button = tk.Radiobutton(master, text="", variable=self.radio_var, value="", font=('Arial', 14),
                                          bg="#d3ffd3", fg="#003366", activebackground="#d3ffd3", selectcolor="#d3ffd3")
            self.radio_buttons.append(radio_button)
            radio_button.pack(anchor='w')

        self.next_button = tk.Button(master, text="Next", command=self.next_question, font=('Arial', 14, 'bold'),
                                     bg="#008000", fg="black", padx=10, pady=5, bd=5, relief="raised")
        self.next_button.pack()

        self.show_question()

    def show_question(self):
        question_data = self.questions[self.current_question_index]
        self.question_number_label.config(text=f"Question {self.current_question_index + 1}/{len(self.questions)}")
        self.question_label.config(text=question_data['question'])
        choices = question_data.get('choices', [])
        random.shuffle(choices)

        for i in range(4):
            if i < len(choices):
                self.radio_buttons[i].config(text=choices[i], value=choices[i], state='normal')
            else:
                self.radio_buttons[i].config(text="", value="", state='disabled')

    def next_question(self):
        user_answer = self.radio_var.get()
        correct_answer = self.questions[self.current_question_index]['answer']

        if user_answer == correct_answer:
            self.score += 1

        self.current_question_index += 1

        if self.current_question_index < len(self.questions):
            self.show_question()
            self.radio_var.set("")
        else:
            self.display_final_results()

    def display_final_results(self):
        messagebox.showinfo("Quiz Completed", f"Quiz completed!\nYour final score is: {self.score}/{len(self.questions)}")
        self.master.destroy()

if __name__ == "__main__":
    # Define your quiz questions here
    quiz_questions = [
        {
            'question': 'What is the capital of France?',
            'choices': ['Paris', 'Berlin', 'Rome', 'Madrid'],
            'answer': 'Paris'
        },
        {
            'question': 'Which planet is known as the Red Planet?',
            'choices': ['Venus', 'Mars', 'Jupiter', 'Saturn'],
            'answer': 'Mars'
        },
        {
            'question': 'What is the largest mammal in the world?',
            'choices': ['Elephant', 'Giraffe', 'Blue Whale', 'Hippopotamus'],
            'answer': 'Blue Whale'
        },
        # Add more questions as needed
    ]

    root = tk.Tk()
    game = QuizGameGUI(root, quiz_questions)
    root.mainloop()
