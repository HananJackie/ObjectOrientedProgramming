from overrides import overrides


class Vehicle:

  def __init__(self, brand: str, base_daily_rate: float):
    self.brand = brand
    self.base_daily_rate = base_daily_rate

  def get_daily_rate(self) -> float:
    return self.base_daily_rate

  def get_details(self) -> str:
    return f"Brand: {self.brand}, Base Rate: ${self.base_daily_rate:.2f}"


class Car(Vehicle):

  def __init__(self, brand: str, base_daily_rate: float, num_seats: int):
    super().__init__(brand, base_daily_rate)
    self.num_seats = num_seats

  @overrides
  def get_daily_rate(self) -> float:
    return self.base_daily_rate + (self.num_seats * 10)

  @overrides
  def get_details(self) -> str:
    base_info = super().get_details()
    return f"{base_info}, Seats: {self.num_seats}, Total Daily Rate: ${self.get_daily_rate():.2f}"


class ElectricScooter(Vehicle):

  def __init__(self, brand: str, base_daily_rate: float, battery_percentage: int):
    super().__init__(brand, base_daily_rate)
    self.battery_percentage = battery_percentage

  @overrides
  def get_details(self) -> str:
    base_info = super().get_details()
    return f"{base_info}, Battery: {self.battery_percentage}%"


# Polymorphic demonstration
def print_fleet_summary(fleet_list: list):
  print("--- Fleet Rental Summary ---")
  for vehicle in fleet_list:
    # Polymorphism in action: calls the correct override version automatically
    print(vehicle.get_details())


# --- Execution Example ---
if __name__ == "__main__":
  fleet = [
      Vehicle("Generic Fleet Co.", 30.00),
      Car("Toyota", 50.00, num_seats=5),
      ElectricScooter("Bird", 15.00, battery_percentage=85),
      Car("Ford", 70.00, num_seats=7),
  ]

  print_fleet_summary(fleet)