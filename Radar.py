from Rules import Fine


class Radar:
    def __init__(self):
        self.rules = []
        self.fines= []
        self.rule_counts = {}

    def add_rule(self, rule):
        self.rules.append(rule)
        self.rule_counts[rule.name()] = 0

    def observe(self, observation):
        fine = Fine(observation.plate)

        for rule in self.rules:
            violation = rule.check(observation)
            if violation:
                fine.add_violation(violation)
                self.rule_counts[rule.name()] += 1

        if fine.violations:
            self.fines.append(fine)
            fine.print_fine()

    def getAllFines(self):
        print("All Fines:")
        for fine in self.fines:
            print(f"{fine.plate} : {fine.total_amount()} EGP")
        print()

    def getAllViolatedRules(self):
        print("Violated Rules:")
        for rule, count in self.rule_counts.items():
            print(f"{rule} : {count}")

