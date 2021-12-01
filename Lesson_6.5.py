class Stationary:
    title = str

    def __init__(self, picture_name):
        self.title = picture_name

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationary):
    def draw(self):
        print(f"Я закрашиваю картину, название которой {self.title} ручкой")


class Pencil(Stationary):
    def draw(self):
        print(f"Я создаю контур картине, название которой {self.title} карандашом")


class Handle(Stationary):
    def draw(self):
        print(f"Я раскрашиваю картину, название которой {self.title} маркером")


author_1 = Stationary("(Осеняя пора)")
author_2 = Pen("(Зимний лес)")
author_3 = Pencil("(Студенная пора)")
author_4 = Handle("(Мишки в лесу)")

author_1.draw()
author_2.draw()
author_3.draw()
author_4.draw()
