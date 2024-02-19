"""module for CalculatorModel"""
from math import exp, log, log2, sqrt


class CalculatorModel:
    def __init__(self):
        self.history = []

    def evaluate_expression(self, expression):
        try:
            # Replace specific functions with their respective math functions
            expression = expression.replace("exp", "exp_func")
            expression = expression.replace("log", "log_func")
            expression = expression.replace("log2", "log2_func")
            expression = expression.replace("sqrt", "sqrt_func")
            expression = expression.replace("^", "**")  # Handle the power operator

            # Define custom functions for exp, log, log2, and sqrt
            def exp_func(x):
                return exp(x)

            def log_func(x):
                return log(x)

            def log2_func(x):
                return log2(x)

            def sqrt_func(x):
                return sqrt(x)

            result = eval(expression)
            self.history.append((expression, result))
            return result
        except Exception as e:
            print("Invalid expression:", e)
            return None  # Return None when there's an error
