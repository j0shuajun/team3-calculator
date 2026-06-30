class Calc:
    def get_divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print("Divide by zero")
            return 0
