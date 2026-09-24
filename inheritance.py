from overrides import overrides


class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def honk(self):
        print('Tut, tut!')

class Bicycle(Vehicle):
    def __init__(self, brand, model_name):
        super().__init__(brand)
        self.model_name = model_name

    @overrides
    def honk(self):
        super().honk()
        print('Tzing, tzing!')


if __name__ == "__main__":
    vehicle_obj = Vehicle('Ford')
    bicycle_obj = Bicycle('Ford', 'Cycle')

    print(vehicle_obj.brand)
    print(bicycle_obj.brand)
    print(bicycle_obj.model_name)

    vehicle_obj.honk()
    bicycle_obj.honk()


