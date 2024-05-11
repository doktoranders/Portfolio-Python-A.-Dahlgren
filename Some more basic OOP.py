class Shape: 
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        return self.width * self.height

class Rectangle(Shape):
    def __init__(self, w, h):
        super().__init__(w, h)

    def perimeter(self):
        return 2 * (self.width + self.height)

w = int(input('Enter the width: '))
h = int(input('Enter the height: '))

r = Rectangle(w, h)
print('The area is', r.area()) 
print('The perimeter is', r.perimeter())