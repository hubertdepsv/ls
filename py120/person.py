class Person:
    def __init__(self, first, last):
        if not (first.isalpha() or last.isalpha()) or len(first) == 0 or len(last) == 0:
            raise ValueError('Name must be alphabetic')
        self._first = first
        self._last = last

    @property
    def name(self):
        return ' '.join([self._first.capitalize(), self._last.capitalize()])
    
    @name.setter
    def name(self, name_tuple):
        if not (name_tuple[0].isalpha() or name_tuple[1].isalpha()) or len(name_tuple[0]) == 0 or len(name_tuple[1]) == 0:
            raise ValueError('Name must be alphabetic')
        self._first = name_tuple[0]
        self._last = name_tuple[1]
        # throw errors if they're not alphabetical

# actor = Person('Mark', 'Sinclair')
# print(actor.name)              # Mark Sinclair
# actor.name = ('Vin', 'Diesel')
# print(actor.name)              # Vin Diesel
# actor.name = ('', 'Diesel')
# # ValueError: Name must be alphabetic.

character = Person('annIE', 'HAll')
print(character.name)          # Annie Hall
character = Person('Da5id', 'Meier')
# ValueError: Name must be alphabetic.

friend = Person('Lynn', 'Blake')
print(friend.name)             # Lynn Blake
friend.name = ('Lynn', 'Blake-John')
# ValueError: Name must be alphabetic.