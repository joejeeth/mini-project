from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_l: QuizBrain):
        self.quiz = quiz_l
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        # labels
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", pady=20, padx=20)
        self.score_label.grid(row=0, column=1)

        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question = self.canvas.create_text(150, 125, text="Question here", font=("Arial", 20, "italic"),
                                                fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # buttons
        self.true = PhotoImage(file="./images/true.png")
        self.false = PhotoImage(file="./images/false.png")

        self.true_button = Button(image=self.true, padx=20, highlightthickness=0, command=self.check_true)
        self.true_button.grid(row=3, column=0)

        self.false_button = Button(image=self.false, highlightthickness=0, command=self.check_false)
        self.false_button.grid(row=3, column=1, padx=20)

        self.get_question()

        self.window.mainloop()

    def get_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q, font=("Arial", 15, "italic"), width=280)

        else:
            self.canvas.itemconfig(self.question, text="Game Over", font=("Arial", 15, "italic"), width=280)
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def check_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, result):
        if result:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_question)

