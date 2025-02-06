class commande_vocale:
    def __init__(self):
        self._command = None

    @property
    def command(self):
        return self.command
    
    def interpret_command(self, command):
        self._command = command
        print(f"commande vocale interprété : {command}")

class commande_gestuelle:
    def __init__(self):
        self._main_gauche_leve = False
        self._main_droite_leve = False
        self._deux_mains_leve = False

    @property
    def main_gauche_leve(self):
        return self._main_gauche_leve

    @property
    def main_droite_leve(self):
        return self._main_droite_leve
    
    @property
    def deux_mains_leve(self):
        return self._deux_mains_leve

    def detection_geste(self, main_gauche, main_droite, mains_leve):
        
        self._main_gauche_leve = main_gauche
        self._main_droite_leve = main_droite
        self._deux_mains_leve = mains_leve

        print("geste detecte:")
        if main_gauche:
            print(" - main gauche leve")
        if main_droite:
            print(" - main droite leve")
        if mains_leve:
            print(" - deux mains leve")
