class Car:
    def __init__(self, driver):
        self.driver = driver

    def drive(self):
        print(f"Car is being driven by {self.driver.name}")


class CarProxy:
    """
        Should take the same init variables as Car
    """

    def __init__(self, driver):
        self._car = Car(driver)
        self.min_drive_age = 18

    def drive(self):
        if self._car.driver.age < self.min_drive_age:
            print(
                f"{self._car.driver.name} cannot drive as age({self._car.driver.age}) < {self.min_drive_age}"
            )


class Driver:
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == "__main__":
    driver = Driver("Elon Musk", 12)
    model_3 = Car(driver)
    model_3.drive()

    driver = Driver("Raj Kiran", 16)
    model_s = CarProxy(driver)
    model_s.drive()
