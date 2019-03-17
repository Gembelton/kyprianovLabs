class Aeroflot():
    def __init__(self, namePunkt, raceNumber, aeroType):
        self.namePunkt = namePunkt
        self.raceNumber = raceNumber
        self.aeroType = aeroType

    def printInfo(self):
        print("\n", self.namePunkt, "\n", self.raceNumber, "\n", self.aeroType)
