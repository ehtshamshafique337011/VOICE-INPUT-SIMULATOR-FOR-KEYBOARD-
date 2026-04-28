import tkinter as tk
from init_app import root, text_area

caps_lock = False
shift_on = False

def insert_text(val):
    global caps_lock, shift_on

    if val == "Space":
        text_area.insert(tk.END, " ")
    elif val == "Enter":
        text_area.insert(tk.END, "\n")
    elif val == "Backspace":
        text_area.delete("end-2c")
    elif val == "Caps":
        caps_lock = not caps_lock
    elif val == "Shift":
        shift_on = not shift_on
    else:
        if caps_lock or shift_on:
            text_area.insert(tk.END, val.upper())
        else:
            text_area.insert(tk.END, val.lower())

class ModernKey(tk.Canvas):
    def __init__(self, parent, text, width=55, height=40):
        super().__init__(parent, width=width, height=height,
                         bg="#1e1e1e", highlightthickness=0)

        self.text = text

        self.rect = self.create_rectangle(5, 5, width-5, height-5,
                                          fill="#3c3f41", outline="#555", width=2)

        self.label = self.create_text(width//2, height//2,
                                      text=text, fill="white", font=("Arial", 9, "bold"))

        self.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        insert_text(self.text)
        self.flash()

    def flash(self):
        self.itemconfig(self.rect, fill="#2563eb")
        self.after(200, lambda: self.itemconfig(self.rect, fill="#3c3f41"))

keyboard_frame = tk.Frame(root, bg="#1e1e1e")
keyboard_frame.pack()

keyboard_keys = [
    ['F1','F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12'],
    ['1','2','3','4','5','6','7','8','9','0','-','=','Backspace'],
    ['Tab','q','w','e','r','t','y','u','i','o','p','[',']'],
    ['Caps','a','s','d','f','g','h','j','k','l',';','Enter'],
    ['Shift','Ctrl','z','x','c','v','b','n','m',',','.','/'],
    ['←','↑','↓','→'],
    ['Space']
]

def highlight_key(event):
    key = event.keysym.lower()

    mapping = {
        "space": "space",
        "return": "enter",
        "backspace": "backspace",
        "shift_l": "shift",
        "shift_r": "shift",
        "caps_lock": "caps",
        "control_l": "ctrl",
        "control_r": "ctrl",
        "left": "←",
        "right": "→",
        "up": "↑",
        "down": "↓"
    }

    key = mapping.get(key, key)

    for widget in keyboard_frame.winfo_children():
        for k in widget.winfo_children():
            if isinstance(k, ModernKey) and k.text.lower() == key:
                k.flash()

root.bind("<KeyPress>", highlight_key)

for row in keyboard_keys:
    frame = tk.Frame(keyboard_frame, bg="#1e1e1e")
    frame.pack()

    for key in row:
        k = ModernKey(frame, key)
        k.pack(side=tk.LEFT, padx=3, pady=3)