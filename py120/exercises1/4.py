class Cat:
    def __init__(self, name):
        self._name = name
        print(f"Hello! My name is {name}!")

    def greet(self):
        print(f"Hello! My name is {self._name}!")
    
kitty = Cat("Sophie")
kitty.greet()