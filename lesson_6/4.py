class Car:

    def __init__(self, speed, colour, name, is_police):
        self.speed = speed
        self. colour = colour
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"{self.name} started"

    def stop(self):
        return f'{self.name} stopped'

    def turn_right(self):
        return f'{self.name} turned right'

    def turn_left(self):
        return f'{self.name} turned left'

    def show_speed(self):
        return f'Current speed of {self.name} is {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of town car {self.name} is {self.speed}')

        if self.speed > 40:
            return f'Speed of {self.name} is higher than allow for town car'
        else:
            return f'Speed of {self.name} is normal for town car'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of work car {self.name} is {self.speed}')

        if self.speed > 60:
            return f'Speed of {self.name} is higher than allow for work car'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is from police department'
        else:
            return f'{self.name} is not from police department'


ferrari = SportCar(100, 'Red', 'Ferrari', False)
volkswagen = TownCar(80, 'White', 'Volkswagen', False)
lanos = WorkCar(70, 'Grey', 'Lanos', False)
skoda = PoliceCar(120, 'Blue',  'Skoda', True)
print(lanos.turn_left())
print(f'When {volkswagen.turn_right()}, {ferrari.stop()}')
print(f'{lanos.show_speed()}')
print(f'{lanos.name} is {lanos.colour}')
print(f'Is {ferrari.name} a police car? {ferrari.is_police}')
print(f'Is {lanos.name}  a police car? {lanos.is_police}')
print(ferrari.show_speed())
print(volkswagen.show_speed())
print(skoda.police())
print(skoda.show_speed())
