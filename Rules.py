from abc import ABC, abstractmethod


class Observation:
    def __init__(self, plate, date, car_type, speed, seatbelt):
        self.plate = plate
        self.date = date
        self.car_type = car_type
        self.speed = speed
        self.seatbelt = seatbelt


class Violation:
    def __init__(self, message, fee):
        self.message = message
        self.fee = fee


class Fine:
    def __init__(self, plate):
        self.plate = plate
        self.violations = []

    def add_violation(self, violation):
        self.violations.append(violation)

    def total_amount(self):
        return sum(v.fee for v in self.violations)

    def print_fine(self):
        print(f"Traffic for car {self.plate}")
        print(f"Total amount: {self.total_amount()} EGP")
        print("Violations:")
        for v in self.violations:
            print(f"- {v.message} : {v.fee} EGP")
        print()


class Rule(ABC):
    @abstractmethod
    def check(self, observation):
        pass

    @abstractmethod
    def name(self):
        pass


class SpeedRule(Rule):
    def __init__(self, car_type, max_speed):
        self.car_type = car_type
        self.max_speed = max_speed

    def check(self, observation):
        if observation.car_type == self.car_type:
            if observation.speed > self.max_speed:
                return Violation(
                    f"speed of {observation.speed} exceeded max allowed {self.max_speed}",
                    300,
                )
        return None

    def name(self):
        return f"{self.car_type} Speed Limit"


class SeatbeltRule(Rule):
    def check(self, observation):
        if not observation.seatbelt:
            return Violation("Seatbelt not fastened", 100)
        return None

    def name(self):
        return "Seatbelt Rule"

