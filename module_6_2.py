class Vehicle():
    owner = []
    __model = []
    __engine_power = []
    __color = []
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def get_model(self, model):
        self.model = str(model)
        __model = self.model
        print(f'Модель: {__model}')

    def get_horsepower(self, power):
        self.power = int(power)
        __engine_power = self.power
        print(f'Мощность двигателя: {__engine_power}')

    def get_color(self, color):
        self.color = str(color)
        __color = self.color
        print(f'Цвет: {__color}')

    def print_info(self):
        print(f'Модель: {self.model}')
        print(f'Мощность двигателя: {self.power}')
        print(f'Цвет: {self.color}')
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        self.new_color = str(new_color)
        new_color_ = new_color.lower()
        if new_color_ in Vehicle.__COLOR_VARIANTS:
            self.color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):

    def __init__(self, owner, model, color, power):
        self.owner = owner
        self.model = model
        self.power = power
        self.color = color


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
