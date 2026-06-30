class Calc:
    def getDivide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print("Divide by zero")
            return 0
