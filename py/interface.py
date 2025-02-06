import tkinter as tk
from tkinter import messagebox

import cv2
import PIL.Image, PIL.ImageTk
import time

class tkCamera(tk.Frame):

    def __init__(self, window, video_source=0):
        super().__init__(window)
        
        self.window = window
        
        #self.window.title(window_title)
        self.video_source = video_source
        self.vid = MyVideoCapture(self.video_source)

        self.canvas = tk.Canvas(window, width=self.vid.width, height=self.vid.height)
        self.canvas.pack()
          
        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 15
        self.update_widget()
    
    def update_widget(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()
        
        if ret:
            self.image = PIL.Image.fromarray(frame)
            self.photo = PIL.ImageTk.PhotoImage(image=self.image)
            self.canvas.create_image(0, 0, image = self.photo, anchor = tk.NW)
        
        self.window.after(self.delay, self.update_widget)

class MyVideoCapture:
    def __init__(self, video_source=0):
        # Open the video source
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)
    
        # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
    
        self.width = 800
        self.height = 600 
    
    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                frame = cv2.resize(frame, (800, 600))
                # Return a boolean success flag and the current frame converted to BGR
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)
    
    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

class DroneControlInterface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Interface de Contrôle du Drone")
        self.geometry("900x800")
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
        camera_frame = tkCamera(self)
        camera_frame.pack()
        # camera_frame = tk.LabelFrame(self, text="Caméra", bg="black", fg="white", font=("Arial", 14))
        # camera_frame.place(x=50, y=50, width=800, height=300)
        # camera_label = tk.Label(camera_frame, text="[Flux vidéo en direct]", font=("Arial", 16), bg="black", fg="white")
        # camera_label.pack(expand=True)

    def create_manual_controls(self):
        manual_frame = tk.Frame(self)
        manual_frame.place(x=50, y=600, width=800, height=150)

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
