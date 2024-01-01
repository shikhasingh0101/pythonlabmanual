# BMW.py

class BMW:
    def __init__(self, model,colour):
        self.model = model
        self.colour = colour

    def display_model(self):
        print(f"BMW Model: {self.model}")
        print(f"BMW colour: {self.colour}")

    def start_engine(self):
        print("BMW Engine started")
