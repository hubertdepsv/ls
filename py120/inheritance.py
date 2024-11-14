class Animal:
    def speak(self):
        return 'bark!'

    def sleep(self):
        return 'sleeping!'

    def run(self):
        return 'running!'

    def jump(self):
        return 'jumping!'

class Cat(Animal):
    pass

class Dog(Animal):
    def fetch(self):
        return 'fetching!'

teddy = Dog()
print(teddy.speak())      # bark!
print(teddy.sleep())      # sleeping!

class Bulldog(Dog):
    def sleep(self):
        return 'snoring!'