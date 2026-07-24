from Radar import Radar
from Rules import Observation, SeatbeltRule, SpeedRule


class Main:
    @staticmethod
    def main():
        radar = Radar()

        radar.add_rule(SpeedRule("Truck", 60))
        radar.add_rule(SpeedRule("Private", 80))
        radar.add_rule(SeatbeltRule())

        radar.observe(Observation("ABC1234", "2025-06-01", "Private", 94, False))

        radar.observe(Observation("TRK5678", "2025-06-01", "Truck", 70, True))

        radar.observe(Observation("CAR1111", "2025-06-01", "Private", 75, True))

        radar.getAllFines()
        radar.getAllViolatedRules()


if __name__ == "__main__":
    Main.main()