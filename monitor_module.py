import tkinter as tk
import psutil
import socket
from tkinter import messagebox
from init_app import root

monitor_frame = tk.Frame(root, bg="#111827", bd=1, relief="ridge")
monitor_frame.place(x=1030, y=10, width=140, height=60)

charger_icon = tk.Label(monitor_frame, text="🔌", font=("Segoe UI", 16),
                        bg="#111827", fg="#22c55e")
network_icon = tk.Label(monitor_frame, text="🌐", font=("Segoe UI", 16),
                        bg="#111827", fg="#22c55e")
usb_icon = tk.Label(monitor_frame, text="💾", font=("Segoe UI", 16),
                    bg="#111827", fg="#22c55e")

def check_network():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=2)
        return True
    except:
        return False

def check_charger():
    battery = psutil.sensors_battery()
    return battery and battery.power_plugged

def check_usb():
    return any("removable" in p.opts.lower() for p in psutil.disk_partitions())

def show_usb(event):
    devices = [p.device for p in psutil.disk_partitions() if 'removable' in p.opts.lower()]
    messagebox.showinfo("USB Devices", "\n".join(devices) if devices else "No USB")

def show_network(event):
    status = "Connected" if check_network() else "Disconnected"
    messagebox.showinfo("Network", status)

def show_charger(event):
    status = "Charging" if check_charger() else "Not Charging"
    messagebox.showinfo("Charger", status)

usb_icon.bind("<Button-1>", show_usb)
network_icon.bind("<Button-1>", show_network)
charger_icon.bind("<Button-1>", show_charger)

def check_status():
    for w in monitor_frame.winfo_children():
        w.pack_forget()

    if check_charger():
        charger_icon.pack(side=tk.LEFT, padx=5)
    if check_network():
        network_icon.pack(side=tk.LEFT, padx=5)
    if check_usb():
        usb_icon.pack(side=tk.LEFT, padx=5)

    root.after(1000, check_status)

check_status()