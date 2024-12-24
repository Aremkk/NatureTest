import tkinter as tk
from tkinter import messagebox
import random


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Тест по природоведению")
        self.questions = self.load_questions()
        self.current_question_index = 0
        self.correct_answers = 0
        self.selected_answer = None
        self.create_start_screen()

    def load_questions(self):
        return [
            {"question": "Кто является самым быстрым животным на планете?",
             "options": ["Гепард", "Лев", "Сокол", "Лошадь"], "correct": "Гепард"},
            {"question": "Какое дерево является символом России?", "options": ["Берёза", "Дуб", "Клён", "Сосна"],
             "correct": "Берёза"},
            {"question": "Сколько океанов на Земле?", "options": ["3", "4", "5", "6"], "correct": "5"},
            {"question": "Какой газ необходим для дыхания?",
             "options": ["Азот", "Кислород", "Углекислый газ", "Водород"], "correct": "Кислород"},
            {"question": "Как называется наука о животных?", "options": ["Ботаника", "Зоология", "География", "Физика"],
             "correct": "Зоология"},
            {"question": "Что является основным источником энергии для Земли?",
             "options": ["Солнце", "Луна", "Звёзды", "Вулканы"], "correct": "Солнце"},
            {"question": "Что такое фотосинтез?",
             "options": ["Процесс дыхания растений", "Процесс образования пищи растениями",
                         "Процесс размножения животных", "Процесс образования гор"],
             "correct": "Процесс образования пищи растениями"},
            {"question": "Какой орган отвечает за зрение у человека?", "options": ["Сердце", "Лёгкие", "Глаз", "Мозг"],
             "correct": "Глаз"},
            {"question": "Какой континент самый большой по площади?",
             "options": ["Африка", "Европа", "Азия", "Северная Америка"], "correct": "Азия"},
            {"question": "Какие животные считаются лучшими строителями?",
             "options": ["Бобры", "Муравьи", "Медведи", "Орлы"], "correct": "Бобры"},
        ]

    def select_random_questions(self):
        return random.sample(self.questions, 5)

    def create_start_screen(self):
        self.start_label = tk.Label(self.root, text="Тест по природоведению", font=("Arial", 20))
        self.start_label.pack(pady=50)
        self.start_button = tk.Button(self.root, text="Начать тест", command=self.start_test)
        self.start_button.pack()

    def start_test(self):
        self.random_questions = self.select_random_questions()
        self.start_label.destroy()
        self.start_button.destroy()
        self.current_question_index = 0
        self.correct_answers = 0
        self.show_question(self.current_question_index)

    def show_question(self, question_index):
        self.clear_window()
        if question_index < len(self.random_questions):
            question_data = self.random_questions[question_index]
            self.question_label = tk.Label(self.root,
                                           text=f"Вопрос {question_index + 1}/{len(self.random_questions)}:\n{question_data['question']}",
                                           font=("Arial", 14))
            self.question_label.pack(pady=20)

            self.answer_buttons = []
            for option in question_data['options']:
                button = tk.Button(self.root, text=option, command=lambda ans=option: self.check_answer(ans))
                button.pack(pady=5)
                self.answer_buttons.append(button)

        self.next_button = tk.Button(self.root, text="Следующий вопрос", command=self.next_question, state="disabled")
        self.next_button.pack(pady=10)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def check_answer(self, selected_answer):
        question_data = self.random_questions[self.current_question_index]
        if selected_answer == question_data['correct']:
            self.correct_answers += 1
            messagebox.showinfo("Ответ", "Правильно!")
        else:
            messagebox.showerror("Ответ", f"Неправильно! Правильный ответ: {question_data['correct']}")

        for button in self.answer_buttons:
            button.config(state="disabled")

        self.next_button.config(state="normal")

    def next_question(self):
        self.current_question_index += 1
        if self.current_question_index < len(self.random_questions):
            self.show_question(self.current_question_index)
        else:
            self.show_results()

    def show_results(self):
        self.clear_window()
        score = self.correct_answers
        max_score = len(self.random_questions)
        percent = round((score / max_score) * 100)
        grade = ""
        if percent >= 90:
            grade = "Отлично!"
        elif percent >= 70:
            grade = "Хорошо!"
        elif percent >= 50:
            grade = "Удовлетворительно!"
        else:
            grade = "Плохо!"

        result_label = tk.Label(self.root,
                                text=f"Тест завершен!\nПравильных ответов: {self.correct_answers}/{len(self.random_questions)}\nОценка: {grade}",
                                font=("Arial", 16))
        result_label.pack(pady=50)
        restart_button = tk.Button(self.root, text="Начать заново", command=self.start_test)
        restart_button.pack()
        quit_button = tk.Button(self.root, text="Завершить", command=self.root.quit)
        quit_button.pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
