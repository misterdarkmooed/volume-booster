import tkinter as tk
from tkinter import ttk, messagebox

try:
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
    from comtypes import CLSCTX_ALL, cast, POINTER
except ImportError:
    AudioUtilities = None


class VolumeBooster:
    def __init__(self, root):
        self.root = root
        self.root.title("Volume Booster")
        self.root.geometry("420x230")
        self.root.resizable(False, False)
        self.root.configure(bg="#202124")
        self.volume = None

        tk.Label(root, text="🔊 Volume Booster", bg="#202124", fg="white",
                 font=("Segoe UI", 18, "bold")).pack(pady=(18, 5))
        tk.Label(root, text="Control del volumen de Windows", bg="#202124", fg="#c8c8c8",
                 font=("Segoe UI", 10)).pack()

        self.label = tk.Label(root, text="Volumen: --%", bg="#202124", fg="#7CFC00",
                              font=("Segoe UI", 14, "bold"))
        self.label.pack(pady=(18, 4))

        self.slider = ttk.Scale(root, from_=0, to=100, orient="horizontal",
                                length=330, command=self.change_volume)
        self.slider.set(50)
        self.slider.pack()

        tk.Label(root, text="0%                                      100%",
                 bg="#202124", fg="#aaaaaa").pack()

        tk.Button(root, text="Restaurar 50%", command=lambda: self.slider.set(50),
                  bg="#3c4043", fg="white", relief="flat", padx=12, pady=6).pack(pady=15)
        self.connect_audio()

    def connect_audio(self):
        if AudioUtilities is None:
            self.label.config(text="Falta instalar pycaw", fg="#ffb000")
            messagebox.showwarning(
                "Falta una dependencia",
                "Abre run.bat para instalar las dependencias y vuelve a intentarlo."
            )
            return
        try:
            device = AudioUtilities.GetSpeakers()
            interface = device.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            self.volume = cast(interface, POINTER(IAudioEndpointVolume))
            current = self.volume.GetMasterVolumeLevelScalar() * 100
            self.slider.set(current)
        except Exception as error:
            self.label.config(text="No se pudo acceder al audio", fg="#ff5555")
            print(error)

    def change_volume(self, value):
        percent = int(float(value))
        self.label.config(text=f"Volumen: {percent}%")
        if self.volume is not None:
            try:
                self.volume.SetMasterVolumeLevelScalar(percent / 100, None)
            except Exception as error:
                print(error)


if __name__ == "__main__":
    root = tk.Tk()
    VolumeBooster(root)
    root.mainloop()
