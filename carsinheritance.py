class Vehicle:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model
    def speak(self):
        raise NotImplementedError("Child classes must implement this")

