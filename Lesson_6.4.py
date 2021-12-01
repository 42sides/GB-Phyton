class Car:
    speed = int
    color = str
    name = str
    is_police = bool

    def __init__(self, inc_speed, inc_color, inc_name):
        self.speed = inc_speed
        self.color = inc_color
        self.name = inc_name
        if isinstance(self, PoliceCar):
            self.is_police = True
        else:
            self.is_police = False

    def go(self):
        if isinstance(self, TownCar):
            print("TownCar is go")
        elif isinstance(self, SportCar):
            print("SportCar is go")
        elif isinstance(self, WorkCar):
            print("WorkCar is go")
        elif isinstance(self, PoliceCar):
            print("PoliceCar is go")
        else:
            print("Anything car is go")

    def stop(self):
        if isinstance(self, TownCar):
            print("TownCar is stop")
        elif isinstance(self, SportCar):
            print("SportCar is stop")
        elif isinstance(self, WorkCar):
            print("WorkCar is stop")
        elif isinstance(self, PoliceCar):
            print("PoliceCar is stop")
        else:
            print("Anything car is stop")

    def turn(self, direction):
        if isinstance(self, TownCar):
            print(f"TownCar is turn {direction}")
        elif isinstance(self, SportCar):
            print(f"SportCar is turn {direction}")
        elif isinstance(self, WorkCar):
            print(f"WorkCar is turn {direction}")
        elif isinstance(self, PoliceCar):
            print(f"PoliceCar is turn {direction}")
        else:
            print(f"Anything is turn {direction}")

    def show_speed(self):
        print(f"Скорость автомобиля {self.speed}\n")

    def get_car_info(self):
        z = str
        if self.is_police:
            z = "Автомобиль является полицейским"
        else:
            z = "Автомобиль не является полицейским"
        print(
            f"Машина марка/модель {self.name}, цвет которой {self.color} двигается по дороге со скоростью {self.speed}"
            f" км/ч {z}")
        self.show_speed()


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Вы превышаете максимальную скорость в 60 км/ч. Текущая скорость = {self.speed}\n")
        else:
            print(f"Текущая скорость не превышает максимальную в 60 км/ч. Текущая скорость = {self.speed}\n")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Вы превышаете максимальную скорость в 40 км/ч. Текущая скорость = {self.speed}\n")
        else:
            print(f"Текущая скорость не превышает максимальную в 40 км/ч. Текущая скорость = {self.speed}\n")


class PoliceCar(Car):
    pass


car1 = Car(130, "red", "Dodge Viper")
car2 = TownCar(80, "white", "Skoda Octavia")
car3 = SportCar(170, "black", "Lamborgini Diablo")
car4 = WorkCar(90, "braun", "Daewoo Matiz")
car5 = PoliceCar(100, "black", "Lamborgini Diablo")

car1.get_car_info()
car2.get_car_info()
car3.get_car_info()
car4.get_car_info()
car5.get_car_info()

car1.go()
car1.turn("left")
car2.stop()
car3.go()
car4.stop()
car5.turn("right")
