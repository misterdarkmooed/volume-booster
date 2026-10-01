import tkinter as tk
from tkinter import ttk

class VolumeBooster:
    def __init__(self, root):
        self.root = root
        self.root.title("Volume Booster")
        self.root.geometry("400x250")
        self.root.resizable(False, False)
        self.root.configure(bg="#1a1a1a")
        
        # Título
        title = tk.Label(root, text="🔊 Volume Booster", 
                        bg="#1a1a1a", fg="#00ff00", font=("Arial", 20, "bold"))
        title.pack(pady=20)
        
        # Volumen actual
        self.vol_label = tk.Label(root, text="Volumen: 50%", 
                                 bg="#1a1a1a", fg="#ffff00", font=("Arial", 16, "bold"))
        self.vol_label.pack(pady=10)
        
        # Slider
        self.slider = ttk.Scale(root, from_=0, to=100, orient="horizontal", 
                               command=self.update_label, length=300)
        self.slider.set(50)
        self.slider.pack(pady=15, padx=50)
        
        # Rango
        range_label = tk.Label(root, text="0%  ←  →  100%", 
                              bg="#1a1a1a", fg="#888888", font=("Arial", 10))
        range_label.pack()
        
        # Botón reset
        reset_btn = tk.Button(root, text="Restaurar 50%", command=lambda: self.slider.set(50),
                            bg="#333333", fg="#ffffff", relief="flat", padx=20, pady=8,
                            font=("Arial", 10), cursor="hand2")
        reset_btn.pack(pady=20)
        
        # Info
        info = tk.Label(root, text="⚠️ Cuidado con el volumen alto", 
                       bg="#1a1a1a", fg="#ff6666", font=("Arial", 9))
        info.pack(pady=5)

    def update_label(self, value):
        percent = int(float(value))
        self.vol_label.config(text=f"Volumen: {percent}%")

if __name__ == "__main__":
    root = tk.Tk()
    VolumeBooster(root)
    root.mainloop()
