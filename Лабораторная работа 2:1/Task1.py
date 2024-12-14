
class Vehicle:
    def __init__(self, speed: float, seats: int):
        """Инициализирует объект Vehicle.

        Args:
            speed (float): Начальная скорость транспортного средства. Должна быть неотрицательной.
            seats (int): Количество мест в транспортном средстве. Должно быть неотрицательным.

        Raises:
            ValueError: Если speed или seats отрицательны.

        >>> v = Vehicle(speed=60, seats=5)
        >>> v.speed
        60.0
        """
        if speed < 0:
            raise ValueError("Скорость не может быть отрицательной.")
        if seats < 0:
            raise ValueError("Количество мест не может быть отрицательным.")
        self.speed = speed
        self.seats = seats

    def accelerate(self, increment: float) -> None:
        """Увеличивает скорость транспортного средства.

        Args:
            increment (float): Величина увеличения скорости. Должна быть неотрицательной.

        Raises:
            ValueError: Если increment отрицателен.

        >>> v = Vehicle(speed=60, seats=5)
        >>> v.accelerate(10)
        >>> v.speed
        70.0
        """
        if increment < 0:
            raise ValueError("Приращение скорости не может быть отрицательным.")
        self.speed += increment

    def brake(self, decrement: float) -> None:
        """Уменьшает скорость транспортного средства.

        Args:
            decrement (float): Величина уменьшения скорости. Должна быть неотрицательной.

        Raises:
            ValueError: Если decrement отрицателен.

        >>> v = Vehicle(speed=70, seats=5)
        >>> v.brake(20)
        >>> v.speed
        50.0
        """
        if decrement < 0:
            raise ValueError("Уменьшение скорости не может быть отрицательным.")
        self.speed = max(0, self.speed - decrement)

    def start(self) -> None:
        """Запускает двигатель транспортного средства.

        >>> v = Vehicle(speed=0, seats=5)
        >>> v.start() # нет реальной реализации.
        """
        ...

    def stop(self) -> None:
        """Останавливает двигатель транспортного средства.

        >>> v = Vehicle(speed=0, seats=5)
        >>> v.stop() #  нет реальной реализации.
        """
        ...


class Plant:
    """Представляет собой растение."""
    def __init__(self, height: float, color: str, plant_type: str):
        """Инициализирует объект Plant.

        Args:
            height (float): Высота растения. Должна быть неотрицательной.
            color (str): Цвет растения.
            plant_type (str): Тип растения.

        Raises:
            ValueError: Если height отрицателен.

        >>> p = Plant(height=2.5, color="зелёный", plant_type="Дуб")
        >>> p.height
        2.5
        """
        if height < 0:
            raise ValueError("Высота не может быть отрицательной.")
        self.height = height
        self.color = color
        self.plant_type = plant_type

    def grow(self, increment: float) -> None:
        """Увеличивает высоту растения.

        Args:
            increment (float): Величина увеличения высоты. Должна быть неотрицательной.

        Raises:
            ValueError: Если increment отрицателен.

        >>> p = Plant(height=2.5, color="зелёный", plant_type="Дуб")
        >>> p.grow(0.5)
        >>> p.height
        3.0
        """
        if increment < 0:
            raise ValueError("Приращение высоты не может быть отрицательным.")
        self.height += increment

    def describe(self) -> str:
        """Возвращает описание растения.

        Returns:
            str: Описание растения.

        >>> p = Plant(height=3, color="зелёный", plant_type="Дуб")
        >>> p.describe()
        'Это Дуб высотой 3.0 метра, зелёного цвета.'
        """
        return f"Это {self.plant_type} высотой {self.height:.1f} метра, {self.color} цвета."

    def water(self, amount: float) -> None:
        """Поливает растение.

        Args:
            amount (float): Количество воды. Должно быть неотрицательным.

        Raises:
            ValueError: Если amount отрицателен.

        >>> p = Plant(height=3, color="зелёный", plant_type="Дуб")
        >>> p.water(10) #  нет реальной реализации.
        """
        if amount < 0:
            raise ValueError("Количество воды не может быть отрицательным.")
        ...

    def fertilize(self, fertilizer_type: str) -> None:
        """Удобряет растение.

        Args:
            fertilizer_type (str): Тип удобрения.

        >>> p = Plant(height=3, color="зелёный", plant_type="Дуб")
        >>> p.fertilize("NPK") # нет реальной реализации.
        """
        ...



class BankAccount:
    """Представляет собой банковский счёт."""
    def __init__(self, balance: float, account_number: str, owner: str):
        """Инициализирует объект BankAccount.

        Args:
            balance (float): Начальный баланс счёта. Должен быть неотрицательным.
            account_number (str): Номер счёта.
            owner (str): Владелец счёта.

        Raises:
            ValueError: Если balance отрицателен.

        >>> ba = BankAccount(balance=1000.0, account_number="12345", owner="Иван Иванов")
        >>> ba.balance
        1000.0
        """
        if balance < 0:
            raise ValueError("Баланс не может быть отрицательным.")
        self.balance = balance
        self.account_number = account_number
        self.owner = owner

    def deposit(self, amount: float) -> None:
        """Вносит деньги на счёт.

        Args:
            amount (float): Сумма вклада. Должна быть неотрицательной.

        Raises:
            ValueError: Если amount отрицателен.

        >>> ba = BankAccount(balance=1000.0, account_number="12345", owner="Иван Иванов")
        >>> ba.deposit(500.0)
        >>> ba.balance
        1500.0
        """
        if amount < 0:
            raise ValueError("Сумма вклада не может быть отрицательной.")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """Снимает деньги со счёта.

        Args:
            amount (float): Сумма снятия. Должна быть неотрицательной и не превышать баланс.

        Raises:
            ValueError: Если amount отрицателен или превышает баланс.

        >>> ba = BankAccount(balance=1500.0, account_number="12345", owner="Иван Иванов")
        >>> ba.withdraw(200.0)
        >>> ba.balance
        1300.0
        """
        if amount < 0:
            raise ValueError("Сумма снятия не может быть отрицательной.")
        if amount > self.balance:
            raise ValueError("Недостаточно средств.")
        self.balance -= amount

    def transfer(self, amount: float, target_account: str) -> None:
        """Переводит деньги на другой счёт.

        Args:
            amount (float): Сумма перевода. Должна быть неотрицательной и не превышать баланс.
            target_account (str): Номер целевого счёта.

        Raises:
            ValueError: Если amount отрицателен или превышает баланс.

        >>> ba = BankAccount(balance=1300.0, account_number="12345", owner="Иван Иванов")
        >>> ba.transfer(100, "67890") # Этот doctest пройдёт, потому что нет реальной реализации.
        """
        if amount < 0:
            raise ValueError("Сумма перевода не может быть отрицательной.")
        if amount > self.balance:
            raise ValueError("Недостаточно средств.")
        ...

    def get_statement(self, period: str) -> list:
        """Получает выписку по счёту за указанный период.

        Args:
            period (str): Период для выписки (например, "месяц", "год").

        Returns:
            list: Список транзакций.

        >>> ba = BankAccount(balance=1300.0, account_number="12345", owner="Иван Иванов")
        >>> ba.get_statement("месяц") # нет реальной реализации.
        []
        """
        ...

if __name__ == "__main__":
    import doctest
    doctest.testmod()
