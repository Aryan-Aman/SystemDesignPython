"""Strategy Design Pattern (Vehicle Example)

Problem (without Strategy):
- If we create subclasses like `OffRoadVehicle`, `PassengerVehicle`, `SportVehicle` and
  each overrides `drive()`, we often duplicate logic.
- Adding a new driving behavior (e.g., SnowDrive, EcoDrive) forces changes across many
  classes or creates more subclasses (class explosion).
- Switching behavior at runtime is hard with inheritance (a passenger car can't easily
  switch to off-road behavior temporarily).

Solution (Strategy):
- Extract the varying behavior into a `DriveStrategy`.
- Vehicles *compose* a strategy instead of hardcoding drive logic in the vehicle class.
- Add new behaviors by adding new strategies, without modifying existing vehicle classes.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


# Strategy
class DriveStrategy(ABC):
    @abstractmethod
    def drive(self) -> str:
        raise NotImplementedError


class NormalDrive(DriveStrategy):
    def drive(self) -> str:
        return "Driving normally"


class SportsDrive(DriveStrategy):
    def drive(self) -> str:
        return "Driving with sports tuning"


class OffRoadDrive(DriveStrategy):
    def drive(self) -> str:
        return "Driving with off-road control"


# Context
class Vehicle:
    def __init__(self, drive_strategy: DriveStrategy):
        self._drive_strategy = drive_strategy

    def drive(self) -> str:
        return self._drive_strategy.drive()

    def set_drive_strategy(self, drive_strategy: DriveStrategy) -> None:
        self._drive_strategy = drive_strategy


# Concrete vehicles (configured with a strategy)
class PassengerVehicle(Vehicle):
    def __init__(self):
        super().__init__(NormalDrive())


class SportVehicle(Vehicle):
    def __init__(self):
        super().__init__(SportsDrive())


class OffRoadVehicle(Vehicle):
    def __init__(self):
        super().__init__(OffRoadDrive())


def demo() -> None:
    print("--- Strategy Pattern Demo ---")

    passenger = PassengerVehicle()
    sport = SportVehicle()
    offroad = OffRoadVehicle()

    print("PassengerVehicle:", passenger.drive())
    print("SportVehicle:", sport.drive())
    print("OffRoadVehicle:", offroad.drive())

    # Runtime behavior change (easy with Strategy)
    print("\nPassengerVehicle switching to OffRoadDrive at runtime...")
    passenger.set_drive_strategy(OffRoadDrive())
    print("PassengerVehicle:", passenger.drive())


if __name__ == "__main__":
    demo()
