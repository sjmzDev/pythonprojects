import tkinter as tk
import threading
import time
import os
from pynput import keyboard
from pynput.mouse import Controller, Button

mouse = Controller()
running = False
CONFIG_FILE = "config.txt"

def limpiar_rastros(nombre_archivo="autoclicker.exe"):
    recientes = os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Recent')
    auto_dest = os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Recent', 'AutomaticDestinations')

    for f in os.listdir(recientes):
        try:
            with open(os.path.join(recientes, f), errors='ignore') as archivo:
                if nombre_archivo.lower() in archivo.read().lower():
                    os.remove(os.path.join(recientes, f))
        except: pass

    for f in os.listdir(auto_dest):
        try:
            with open(os.path.join(auto_dest, f), 'rb') as archivo:
                if nombre_archivo.encode().lower() in archivo.read().lower():
                    os.remove(os.path.join(auto_dest, f))
        except: pass

def click_loop(get_cps):
    global running
    while True:
        if running:
            try:
                cps = float(get_cps())
                if cps <= 0:
                    cps = 1
            except:
                cps = 10
            delay = 1.0 / cps
            mouse.press(Button.left)
            mouse.release(Button.left)
            time.sleep(delay)
        else:
            time.sleep(0.01)

def toggle_listener(get_key):
    def on_press(key):
        global running
        try:
            if key.char.lower() == get_key():
                running = not running
                print(f"[INFO] Autoclicker {'ACTIVADO' if running else 'DESACTIVADO'}")
        except AttributeError:
            if hasattr(key, 'name') and key.name == get_key():
                running = not running
                print(f"[INFO] Autoclicker {'ACTIVADO' if running else 'DESACTIVADO'}")

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

class AutoClickerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("BonesClicker 111")

        tk.Label(master, text="Clicks por segundo (CPS):").pack()
        self.cps_entry = tk.Entry(master)
        self.cps_entry.pack()

        tk.Label(master, text="Tecla para activar/desactivar:").pack()
        self.key_entry = tk.Entry(master)
        self.key_entry.pack()

        self.save_button = tk.Button(master, text="Guardar configuración", command=self.save_config)
        self.save_button.pack(pady=5)

        self.load_config()
        self.start_threads()

        self.master.protocol("WM_DELETE_WINDOW", self.on_close)

    def get_cps(self):
        try:
            return float(self.cps_entry.get())
        except:
            return 10

    def get_key(self):
        return self.key_entry.get().lower()

    def save_config(self):
        try:
            with open(CONFIG_FILE, "w") as f:
                f.write(f"cps={self.cps_entry.get()}\n")
                f.write(f"tecla={self.key_entry.get()}\n")
            print("[ ✅ ] Configuración guardada.")
        except Exception as e:
            print(f"[❗] Error al guardar configuración: {e}")

    def load_config(self):
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, "r") as f:
                    for line in f:
                        if line.startswith("cps="):
                            self.cps_entry.insert(0, line.strip().split("=")[1])
                        elif line.startswith("tecla="):
                            self.key_entry.insert(0, line.strip().split("=")[1])
                print("[ ✅ ] Configuración cargada.")
            except:
                print("[❗] No se pudo cargar configuración.")
        else:
            self.cps_entry.insert(0, "10")
            self.key_entry.insert(0, "f6")

    def start_threads(self):
        threading.Thread(target=click_loop, args=(self.get_cps,), daemon=True).start()
        toggle_listener(self.get_key)
        print("[ ✅ ] Comenzando..")

    def on_close(self):
        print("[ ✅ ] Cerrando autoclicker...")
        if os.path.exists(CONFIG_FILE):
            os.remove(CONFIG_FILE)
        limpiar_rastros("config.txt")
        limpiar_rastros("autoclicker.exe")
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.iconbitmap("test1.ico")
    app = AutoClickerApp(root)
    root.mainloop()
