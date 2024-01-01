# AUDI.py

class AUDI:
    def __init__(self, model,colour):
        self.model = model
        self.colour = colour

    def display_model(self):
        print(f"AUDI Model: {self.model}")
        print(f"AUDI colour: {self.colour}")

    def start_engine(self):
        print("AUDI Engine started")
