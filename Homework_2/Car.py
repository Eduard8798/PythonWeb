class Car:
    def __init__(self, model="", year=0, manufacturer="", engine_volume=0.0, color="", price=0.0):
        """
        Конструктор класу для ініціалізації атрибутів.
        """
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_volume = engine_volume
        self.color = color
        self.price = price

    def input_data(self):
        """
        Метод для введення даних автомобіля з клавіатури.
        """
        self.model = input("Enter the car model: ")
        self.year = int(input("Enter the year of manufacture: "))
        self.manufacturer = input("Enter the manufacturer: ")
        self.engine_volume = float(input("Enter the engine volume (e.g., 2.0): "))
        self.color = input("Enter the car color: ")
        self.price = float(input("Enter the price of the car: "))

    def display_data(self):
        """
        Метод для виведення даних автомобіля.
        """
        print("\nCar Information:")
        print(f"Model: {self.model}")
        print(f"Year of Manufacture: {self.year}")
        print(f"Manufacturer: {self.manufacturer}")
        print(f"Engine Volume: {self.engine_volume} L")
        print(f"Color: {self.color}")
        print(f"Price: ${self.price:,.2f}")

    def update_price(self, new_price):
        """
        Метод для оновлення ціни автомобіля.
        """
        self.price = new_price
        print(f"The price has been updated to ${self.price:,.2f}")

    def paint_car(self, new_color):
        """
        Метод для зміни кольору автомобіля.
        """
        old_color = self.color
        self.color = new_color
        print(f"The car color has been changed from {old_color} to {new_color}.")
