"""Module for CalculatorModel"""
from math import exp, log, log2, sqrt


class CalculatorModel:
    """Model class for the calculator"""

    def __init__(self):
        """Initialize the model with an empty history list."""
        self.history = []

    def evaluate_expression(self, expression):
        """Evaluate the given mathematical expression."""
        try:
            # Replace specific functions with their respective math functions
            expression = expression.replace("exp", "exp_func")
            expression = expression.replace("ln", "ln_func")
            expression = expression.replace("log2", "log2_func")
            expression = expression.replace("sqrt", "sqrt_func")
            expression = expression.replace("^", "**")

            # Define custom functions for exp, log, log2, and sqrt
            def exp_func(x_value):
                return exp(x_value)

            def ln_func(x_value):
                return log(x_value)

            def log2_func(x_value):
                return log2(x_value)

            def sqrt_func(x_value):
                return sqrt(x_value)

            result = eval(expression)
            self.history.append((expression, result))
            return result
        except Exception as error_message:
            print("Invalid expression:", error_message)
            return None  # Return None when there's an error
