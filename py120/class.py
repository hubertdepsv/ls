class Car:

    def __init__(self, model, year, color):
        self._model = model
        self._year = year
        self._color = color
        self.speed = 0

    def engine_start(self):
        print('The engine is on!')

    def engine_off(self):
        self._speed = 0
        print("Let's park this baby!")
        print('The engine is off!')

    def speed_up(self, number):
        self.speed += number
        print(f'You accelerated {number} mph.')

    def brake(self, number):
        self.speed -= number
        print(f'You decelerated {number} mph.')

    def get_speed(self):
        print(f'Your speed is {self.speed} mph.')
    
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, new_color):
        self._color = new_color

    def spray_car_with_new_color(self, new_color):
        self.color = new_color

    @classmethod
    def calculate_print_avg_gas_mileage(cls, distance, fuel):
        print(f"{distance / fuel} miles per gallon")


lumina = Car('chevy lumina', 1997, 'white')
lumina.engine_start() # The engine is on!
lumina.get_speed()    # Your speed is 0 mph.
lumina.speed_up(20)   # You accelerated 20 mph.
lumina.get_speed()    # Your speed is 20 mph.
lumina.speed_up(30)   # You accelerated 30 mph.
lumina.get_speed()    # Your speed is 50 mph.
lumina.brake(15)      # You decelerated 15 mph.
lumina.get_speed()    # Your speed is 35 mph.
lumina.brake(30)      # You decelerated 30 mph.
lumina.get_speed()    # Your speed is 5 mph.
lumina.engine_off()   # Let's park this baby!
                      # The engine is off
lumina.get_speed()    # Your speed is 0 mph.
print(lumina.color)        # white
lumina.color = 'red'
print(lumina.color)       # red