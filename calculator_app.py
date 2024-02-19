"""module to run calculator application"""
from calculator_ui import CalculatorUI
from controller import CalculatorController
from model import CalculatorModel

if __name__ == "__main__":
    model = CalculatorModel()
    view = CalculatorUI()
    controller = CalculatorController(model, view)
    view.mainloop()
