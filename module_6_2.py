class Vehicle():
    owner = str()
    __model = str()
    __engine_power = int()
    __color = str()
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, power):
        self.owner = owner
        self.__color = color
        self.__model = model
        self.__engine_power = power

    def get_model(self, __model):
        print(f'Модель: {__model}')

    def get_horsepower(self, __engine_power):
        print(f'Мощность двигателя: {__engine_power}')

    def get_color(self, __color):
        print(f'Цвет: {__color}')

    def print_info(self):
        print(f'Модель: {self.__model}')
        print(f'Мощность двигателя: {self.__engine_power}')
        print(f'Цвет: {self.__color}')
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        self.new_color = str(new_color)
        new_color_ = new_color.lower()
        if new_color_ in Vehicle.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    pass


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
