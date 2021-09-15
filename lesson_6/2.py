class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width
    def mass(self):
        return self._width * self._length

class MassCount(Road):
    def __init__(self, _length, _width, volume):
        super().__init__(_length, _width)
        self.volume = volume


a = MassCount(25, 10000, 125)
print(a.mass())
