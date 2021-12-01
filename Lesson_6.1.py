import time


class TrafficLight:
    _color = str

    def running(self):
        self._color = "Красный"
        print(f"Текущий цвет светофора {self._color}")
        time.sleep(7)


        self._color = "Желтый"
        print(f"Текущий цвет светофора {self._color}")
        time.sleep(2)


        self._color = "Зеленый"
        print(f"Текущий цвет светофора {self._color}")
        time.sleep(5)


       # lite.running() - если раскомментировать, будет работать постоянно


lite = TrafficLight()
lite.running()