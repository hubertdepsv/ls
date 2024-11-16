class Transform:
    def __init__(self, content):
        self.content = content
    
    def uppercase(self):
        return self.content.upper()
    
    @classmethod
    def lowercase(cls, new_content):
        return new_content.lower()

my_data = Transform('abc')
print(my_data.uppercase())              # ABC
print(Transform.lowercase('XYZ'))       # xyz