class Cat:

    @classmethod
    def generic_greeting(cls):
        print("Hello! I'm a cat!")

kitty = Cat()
print(type(kitty).generic_greeting()) # Hello! I'm a cat!