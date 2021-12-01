class Road:
    _length = int
    _width = int

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_calculation(self):
        return int(self._length * self._width * 25 * 5 / 100)


first_road = Road(2, 5000)

print(f"{first_road.mass_calculation()} т")
