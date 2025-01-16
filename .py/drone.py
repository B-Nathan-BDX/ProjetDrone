class Drone:
    def __init__(self):
        print("drone initialise")
        self._vol = False
        self.batterie = 100

    @property
    def vol(self):
        return self._vol
    
    @property
    def batterie(self):
        return self.batterie
    
    def takeoff(self):
        if not self._vol:
            self._vol=True
            print("le drone decole")
        else :
            print("le drone vol deja")

    def land(self):
        if self._vol:
            self._vol=False
            print("le drone atterri")
        else:
            print("le drone a deja atterri")

    def avancer (self, distance):
        if self._vol:
            print(f"le drone avance de {distance}cm")
        else :
            print ("le drone est au sol")
    
    def reculer (self, distance):
        if self._vol:
            print(f"le drone recule de {distance}cm")
        else:
            print ("le drone est au sol")

    def gauche (self, distance):
        if self._vol:
            print(f"le drone vas a gauche de {distance}cm")
        else:
            print ("le drone est au sol")

    def droite (self, distance):
        if self._vol:
            print(f"le drone vas a droite  de {distance}cm")
        else:
            print ("le drone est au sol")

    def monter (self, altitude):
        if self._vol:
            print(f"le drone monte de {altitude}cm")
        else:
            print ("le drone est au sol")

    def descendre (self, altitude):
        if self._vol:
            print(f"le drone descend de {altitude}cm")
        else:
            print ("le drone est au sol")

    def clockwise (self, degree):
        if self._vol:
            print(f"le drone tourne dans le sens des aiguilles d'une montre de {degree} degree")
        else:
            print ("le drone est au sol")

    def counter_clockwise (self, degree):
        if self._vol:
            print(f"le drone tourne dans le sens inverse des aiguilles d'une montre de {degree} degree")
        else:
            print ("le drone est au sol")
            