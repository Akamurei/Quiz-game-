from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        self.quiz = quiz_brain

        self.label = Label(self.window, text=f"Score: {self.quiz.score}", background=THEME_COLOR, foreground="white")
        self.label.grid(row=0, column=1)



        self.canvas = Canvas(self.window, width=300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        correct_img = PhotoImage(file="images/true.png")
        wrong_img = PhotoImage(file="images/false.png")

        self.correct_button = Button(image=correct_img, highlightthickness=0, command=self.true_answer)
        self.correct_button.grid(row=2, column=0)

        self.wrong_button = Button(image=wrong_img, highlightthickness=0, command=self.false_answer)
        self.wrong_button.grid(row=2, column=1)

        self.question_text = self.canvas.create_text(150, 125, text=f"Some text", width=280, font=("Ariel", 20, "italic"), fill=THEME_COLOR)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've completed the quiz")
            self.correct_button.config(state=DISABLED)
            self.wrong_button.config(state=DISABLED)

    def true_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_answer(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="Green")
        else:
            self.canvas.config(bg="Red")
        self.window.after(1000, self.get_next_question)
        self.label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
