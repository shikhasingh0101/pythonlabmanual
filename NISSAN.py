# NISSAN.py

class NISSAN:
    def __init__(self, model,colour):
        self.model = model
        self.colour = colour

    def display_model(self):
        print(f"NISSAN Model: {self.model}")
        print(f"NISSAN colour: {self.colour}")

    def start_engine(self):
        print("NISSAN Engine started")
