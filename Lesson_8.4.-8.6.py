import time


class Warehouse:
    __capacity = 7
    __current_balance = 0
    map = {}

    @staticmethod
    def get(key):
        del Warehouse.map[key]
        Warehouse.__current_balance = Warehouse.__current_balance - 1
        print(f"Оборудование с серийным номером {key} удачно взято из хранилища")

    @staticmethod
    def put(key, value):
        if Warehouse.__current_balance < Warehouse.__capacity:
            Warehouse.map.update({key: value})
            print(f"Оборудование с серийным номером {key} удачно принято в хранилище")
            Warehouse.__current_balance = Warehouse.__current_balance + 1
        else:
            print(
                f"Хранилище заполнено, необходимо его разгрузить! Оборудование с серийным номером {key} "
                f"не может быть принято в хранилище!")

    @staticmethod
    def warehouse_info():
        print("\nОборудование доступное на складе:\n")
        for tags in Warehouse.map.values():
            print(tags)
            time.sleep(1)


class OfficeEquipment:
    __serial_number = int
    __manufacturer = str
    __model = str
    __voltage = int
    __price = int
    __can_scan = bool

    def __init__(self, serial_number, manufacturer, model, voltage, price, can_scan):
        if type(serial_number) == int and type(voltage) == int and type(price) == int and type(manufacturer) == str \
                and type(model) == str and type(can_scan) == bool:
            self.__serial_number = serial_number
            self.__manufacturer = manufacturer
            self.__model = model
            self.__voltage = voltage
            self.__price = price
            self.__can_scan = can_scan
        else:
            pass

    def __getattr__(self):
        return self.__serial_number

    def put_on(self):
        # Warehouse.map.update({self.__getattr__(): self})
        check = bool
        for key in Warehouse.map.keys():
            if key == self.__serial_number:
                check = False
            else:
                check = True
        if not check:
            print(f"Оборудование с серийным номером {self.__serial_number} уже присутствует на складе")
        elif self.__can_scan == False or self.__can_scan == True:
            Warehouse.put(self.__getattr__(), self)
        else:
            print("Данное оборудование имеет не правильный тип, принятие в хранилище не возможно!")

    def get_off(self):
        Warehouse.get(self.__getattr__())

    def __str__(self):
        return f"Серийный номер {self.__serial_number}, производитель {self.__manufacturer} " \
               f"модель {self.__model} с ценой {self.__price} рублей находится на складе"


class Printers(OfficeEquipment):
    __cartridge_type = str
    __color_print = bool
    __print_resolution = str

    def __init__(self, serial_number, manufacturer, model, voltage, price, can_scan, cartridge_type, color_print,
                 print_resolutions):
        super().__init__(serial_number, manufacturer, model, voltage, price, can_scan)
        self.__cartridge_type = cartridge_type
        self.__color_print = color_print
        self.__print_resolution = print_resolutions


class Scanners(OfficeEquipment):
    __scan_resolution = str

    def __init__(self, serial_number, manufacturer, model, voltage, price, can_scan, scan_resolution):
        super().__init__(serial_number, manufacturer, model, voltage, price, can_scan)
        self.__scan_resolution = scan_resolution


class Xerox(OfficeEquipment):
    __cartridge_type = str
    __color_print = bool
    __scan_resolution = str

    def __init__(self, serial_number, manufacturer, model, voltage, price, can_scan, cartridge_type, color_print,
                 scan_resolution):
        super().__init__(serial_number, manufacturer, model, voltage, price, can_scan)
        self.__cartridge_type = cartridge_type
        self.__color_print = color_print
        self.__scan_resolution = scan_resolution


xerox1 = Xerox(123123, 235, "z300", 220, 4900, True, "color", True, "1280x1024")
xerox2 = Xerox(123124, "HP", "z302", 220, 5300, True, "color", True, "1280x1024")
xerox3 = Xerox(123125, "HP", "z400", 220, 6100, True, "color", True, "1280x1024")
xerox4 = Xerox(123199, "HP", "z405", 220, 13300, True, "color", True, "2900x1024")
scan1 = Scanners(132253, "Samsung", "p43p34", 220, 3200, True, "2000x4000")
scan2 = Scanners(132253, "Samsung", "n5n7n1", 220, 2900, True, "1280x1024")
scan3 = Scanners(435234, "Samsung", "m1m2k3", 220, 4300, True, "4000x6000")
scan4 = Scanners(435271, "Samsung", "m1m2k3", 220, 4300, False, "4000x6000")
printer1 = Printers(435987, "Xerox", "h59sw", 220, 2100, True, "powder", True, "1280x1024")
printer2 = Printers(123234, "Xerox", "jo04p", 220, 2300, True, "jet", False, "1280x1024")
printer3 = Printers(476834, "Xerox", "huz124", 220, 8900, True, "powder", True, "4000x6000")

xerox1.put_on()
time.sleep(2)
xerox2.put_on()
time.sleep(2)
xerox3.put_on()
time.sleep(2)
xerox4.put_on()
time.sleep(2)
scan1.put_on()
time.sleep(2)
scan2.put_on()
time.sleep(2)
scan3.put_on()
time.sleep(2)
scan4.put_on()
time.sleep(2)
printer1.put_on()
time.sleep(2)
printer2.put_on()
time.sleep(2)
printer3.put_on()
time.sleep(2)
scan1.get_off()
time.sleep(2)
scan1.put_on()
time.sleep(2)

Warehouse.warehouse_info()
