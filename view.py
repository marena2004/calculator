import tkinter as tk
from tkinter import ttk


class CalculatorView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.input_display = tk.Entry(self, font=('arial', 20), fg="yellow", bg='black', justify="right")
        self.input_display.grid(row=0, column=0, columnspan=5, sticky="ew", padx=10, pady=10)

        self.create_buttons()

        # Define button actions
        self.button_actions = {
            "=": self.calculate_result,
            "DEL": self.delete_last,
            "CLR": self.clear_display,
            "History": self.show_history,
            "^": lambda: self.input_display.insert(tk.END, "^"),
            "exp": lambda: self.insert_with_parentheses("exp"),
            "ln": lambda: self.insert_with_parentheses("ln"),
            "log2": lambda: self.insert_with_parentheses("log2"),
            "sqrt": lambda: self.insert_with_parentheses("sqrt"),
            "mod": lambda: self.input_display.insert(tk.END, "%")
        }

        # Configure row and column weights to allow resizing
        self.grid_rowconfigure(0, weight=1)
        for i in range(7):  # 7 rows
            self.grid_rowconfigure(i + 1, weight=1)
        for i in range(5):  # 5 columns
            self.grid_columnconfigure(i, weight=1)

    def create_buttons(self):
        buttons = [
            ("exp", 1, 0), ("ln", 1, 1), ("mod", 1, 2), ("log2", 1, 3), ("sqrt", 1, 4),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("/", 2, 3), ("(", 2, 4),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("*", 3, 3), (")", 3, 4),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("-", 4, 3), ("^", 4, 4),
            ("0", 5, 0), (".", 5, 1), ("=", 5, 2), ("+", 5, 3), ("DEL", 5, 4),
            ("CLR", 6, 0), ("History", 6, 1)
        ]

        for btn_text, row, col in buttons:
            btn = ttk.Button(self, text=btn_text, style="Calculator.TButton", width=10,
                             command=lambda text=btn_text: self.on_button_click(text))
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

    def on_button_click(self, text):
        action = self.button_actions.get(text)
        if action:
            action()
        else:
            self.input_display.insert(tk.END, text)

    def calculate_result(self):
        result = self.controller.evaluate_expression(self.input_display.get())
        if result is not None:
            self.input_display.delete(0, tk.END)
            self.input_display.insert(tk.END, str(result))
        else:
            self.input_display.delete(0, tk.END)
            self.input_display.insert(tk.END, "Error")

    def delete_last(self):
        self.input_display.delete(len(self.input_display.get()) - 1)

    def clear_display(self):
        self.input_display.delete(0, tk.END)

    def show_history(self):
        history_window = tk.Toplevel(self)
        history_window.title("History")
        history_text = tk.Text(history_window, height=10, width=50)
        history_text.pack()

        for expression, result in self.controller.model.history:
            history_text.insert(tk.END, f"{expression} = {result}\n")

    def insert_with_parentheses(self, func_name):
        self.input_display.insert(tk.END, f"{func_name}(")

    def set_controller(self, controller):
        self.controller = controller

