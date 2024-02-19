"""module for CalculatorController"""


class CalculatorController:
    """Controller class for the calculator."""

    def __init__(self, model, view):
        """Initialize the controller with references to the model and view."""
        self.model = model
        self.view = view
        self.view.set_controller(self)

    def evaluate_expression(self, expression):
        """Evaluate the given mathematical expression using the model."""
        return self.model.evaluate_expression(expression)

    def clear_history(self):
        """Clear the history of recent calculations in the model."""
        self.model.history = []
