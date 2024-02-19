"""module to run calculator application"""
from view import CalculatorView
from controller import CalculatorController
from model import CalculatorModel

if __name__ == "__main__":
    model = CalculatorModel()
    view = CalculatorView()
    controller = CalculatorController(model, view)
    view.mainloop()
