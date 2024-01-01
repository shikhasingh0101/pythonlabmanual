class InputNumbers:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def get_numbers(self):
        self.num1 = float(input("Enter the first number: "))
        self.num2 = float(input("Enter the second number: "))


class AddNumbers(InputNumbers):
    def add(self):
        result = self.num1 + self.num2
        print("The sum of {} and {} is: {}".format(self.num1, self.num2, result))
        
        
addition_obj = AddNumbers()
addition_obj.get_numbers()
addition_obj.add()
