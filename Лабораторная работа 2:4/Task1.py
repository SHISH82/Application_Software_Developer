from typing import Optional

class Transport:
    """
    Базовый класс для всех транспортных средств.

    Атрибуты:
        name (str): Название транспортного средства.
        max_speed (float): Максимальная скорость.
        capacity (int): Вместимость (количество пассажиров или груза).
    """

    def __init__(self, name: str, max_speed: float, capacity: int) -> None:
        """
        Конструктор базового класса Transport.

        Аргументы:
            name (str): Название транспортного средства.
            max_speed (float): Максимальная скорость.
            capacity (int): Вместимость.
        """
        self.name = name
        self.max_speed = max_speed
        self.capacity = capacity

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.
        """
        return f"Transport: {self.name}, Max Speed: {self.max_speed} km/h, Capacity: {self.capacity}"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление объекта.
        """
        return f"Transport(name={self.name}, max_speed={self.max_speed}, capacity={self.capacity})"

    def move(self) -> str:
        """
        Метод для движения транспортного средства.

        Возвращает:
            str: Сообщение о движении.
        """
        return f"{self.name} is moving at {self.max_speed} km/h."


class Car(Transport):
    """
    Дочерний класс для легковых автомобилей.

    Атрибуты:
        name (str): Название автомобиля.
        max_speed (float): Максимальная скорость.
        capacity (int): Вместимость (количество пассажиров).
        fuel_type (str): Тип топлива.
    """

    def __init__(self, name: str, max_speed: float, capacity: int, fuel_type: str) -> None:
        """
        Конструктор класса Car.

        Аргументы:
            name (str): Название автомобиля.
            max_speed (float): Максимальная скорость.
            capacity (int): Вместимость.
            fuel_type (str): Тип топлива.
        """
        super().__init__(name, max_speed, capacity)
        self.fuel_type = fuel_type

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.
        """
        return f"Car: {self.name}, Max Speed: {self.max_speed} km/h, Capacity: {self.capacity}, Fuel: {self.fuel_type}"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление объекта.
        """
        return f"Car(name={self.name}, max_speed={self.max_speed}, capacity={self.capacity}, fuel_type={self.fuel_type})"

    def refuel(self) -> str:
        """
        Метод для заправки автомобиля.

        Возвращает:
            str: Сообщение о заправке.
        """
        return f"{self.name} is refueling with {self.fuel_type}."

    def move(self) -> str:
        """
        Перегрузка метода move для автомобиля.
        Добавлено уточнение о типе топлива.

        Возвращает:
            str: Сообщение о движении с указанием топлива.
        """
        return f"{self.name} is moving at {self.max_speed} km/h using {self.fuel_type}."


class Truck(Transport):
    """
    Дочерний класс для грузовых автомобилей.

    Атрибуты:
        name (str): Название грузовика.
        max_speed (float): Максимальная скорость.
        capacity (int): Вместимость (грузоподъемность).
        cargo_type (str): Тип груза.
    """

    def __init__(self, name: str, max_speed: float, capacity: int, cargo_type: str) -> None:
        """
        Конструктор класса Truck.

        Аргументы:
            name (str): Название грузовика.
            max_speed (float): Максимальная скорость.
            capacity (int): Вместимость.
            cargo_type (str): Тип груза.
        """
        super().__init__(name, max_speed, capacity)
        self.cargo_type = cargo_type

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.
        """
        return f"Truck: {self.name}, Max Speed: {self.max_speed} km/h, Capacity: {self.capacity}, Cargo: {self.cargo_type}"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление объекта.
        """
        return f"Truck(name={self.name}, max_speed={self.max_speed}, capacity={self.capacity}, cargo_type={self.cargo_type})"

    def load_cargo(self) -> str:
        """
        Метод для загрузки груза.

        Возвращает:
            str: Сообщение о загрузке.
        """
        return f"{self.name} is loading {self.cargo_type}."

    def move(self) -> str:
        """
        Перегрузка метода move для грузовика.
        Добавлено уточнение о типе груза.

        Возвращает:
            str: Сообщение о движении с указанием груза.
        """
        return f"{self.name} is moving at {self.max_speed} km/h with {self.cargo_type}."


if __name__ == "__main__":

    car = Car(name="Nissan", max_speed=180.0, capacity=5, fuel_type="petrol")
    truck = Truck(name="Volvo", max_speed=120.0, capacity=7, cargo_type="petrol")

    print(car)
    print(repr(car))
    print(car.move())
    print(car.refuel())

    print(truck)
    print(repr(truck))
    print(truck.move())
    print(truck.load_cargo())
