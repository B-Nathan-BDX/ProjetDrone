import tkinter as tk
from tkinter import messagebox
import cv2, time

class DroneControlInterface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Interface de Contrôle du Drone")
        self.geometry("900x600")
        self.configure(bg="white")

        self.is_on = False  # État initial du drone

        # Affichage caméra simulé
        self.create_camera_display()

        # Boutons de contrôle manuel avec joystick
        self.create_manual_controls()

        # Bouton d'arrêt d'urgence
        self.create_emergency_button()

        # Indicateur de niveau de batterie
        self.create_battery_indicator()

        # Bouton Marche/Arrêt
        self.create_on_off_button()

    def create_camera_display(self):
        camera_frame = tk.LabelFrame(self, text="Caméra", bg="black", fg="white", font=("Arial", 14))
        camera_frame.place(x=50, y=50, width=800, height=300)
        camera_label = tk.Label(camera_frame, text="[Flux vidéo en direct]", font=("Arial", 16), bg="black", fg="white")
        camera_label.pack(expand=True)

    def create_manual_controls(self):
        manual_frame = tk.Frame(self)
        manual_frame.place(x=50, y=380, width=800, height=150)

        joystick_frame = tk.Frame(manual_frame)
        joystick_frame.grid(row=0, column=0, padx=20)

        # Joystick buttons
        tk.Button(joystick_frame, text="⬆", command=lambda: self.manual_control("Avancer"), font=("Arial", 20), width=3).grid(row=0, column=1)
        tk.Button(joystick_frame, text="⬅", command=lambda: self.manual_control("Gauche"), font=("Arial", 20), width=3).grid(row=1, column=0)
        tk.Button(joystick_frame, text="⬇", command=lambda: self.manual_control("Reculer"), font=("Arial", 20), width=3).grid(row=1, column=1)
        tk.Button(joystick_frame, text="➡", command=lambda: self.manual_control("Droite"), font=("Arial", 20), width=3).grid(row=1, column=2)

        # Rotation and altitude buttons
        tk.Button(manual_frame, text="⟲ Rotation Gauche", command=lambda: self.manual_control("Rotation Gauche"), font=("Arial", 14)).grid(row=0, column=1, padx=10)
        tk.Button(manual_frame, text="⟳ Rotation Droite", command=lambda: self.manual_control("Rotation Droite"), font=("Arial", 14)).grid(row=1, column=1, padx=10)
        tk.Button(manual_frame, text="↑ Monter", command=lambda: self.manual_control("Monter"), font=("Arial", 14)).grid(row=0, column=2, padx=10)
        tk.Button(manual_frame, text="↓ Descendre", command=lambda: self.manual_control("Descendre"), font=("Arial", 14)).grid(row=1, column=2, padx=10)

    def create_emergency_button(self):
        tk.Button(self, text="Arrêt d'urgence", command=self.emergency_stop, font=("Arial", 12), bg="red", fg="white", width=14).place(x=714, y=18)

    def create_battery_indicator(self):
        battery_label = tk.Label(self, text="Niveau Batterie : 85%", font=("Arial", 12), bg="white", relief=tk.SOLID)
        battery_label.place(x=50, y=20)

    def create_on_off_button(self):
        self.on_off_button = tk.Button(self, text="Off", command=self.toggle_on_off, font=("Arial", 12), bg="red", fg="white", width=15)
        self.on_off_button.place(x=370, y=20)

    def toggle_on_off(self):
        self.is_on = not self.is_on
        if self.is_on:
            self.on_off_button.config(text="On", bg="green")
        else:
            self.on_off_button.config(text="Off", bg="red")

    # Méthodes de contrôle
    def manual_control(self, action):
        messagebox.showinfo("Contrôle Manuel", f"Commande : {action}")

    def emergency_stop(self):
        messagebox.showwarning("Arrêt d'urgence", "Le drone s'arrête immédiatement !")

if __name__ == "__main__":
    app = DroneControlInterface()
    app.mainloop()
