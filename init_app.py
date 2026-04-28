import tkinter as tk
from tkinter import ttk
from googletrans import Translator

# INIT
root = tk.Tk()
root.title("                                                    VOICE INPUT SIMULATOR FOR KEYBOARD   ")
root.geometry("1200x750")
root.configure(bg="#F8F6F6")

translator = Translator()

# TEXT AREA
text_area = tk.Text(root, height=10, width=100, font=("Arial", 12),
                    bg="#2b2b2b", fg="white", insertbackground="white")
text_area.pack(pady=10)

# LANGUAGE
languages = {
    "English": "en", "Urdu": "ur", "Hindi": "hi",
    "French": "fr", "Spanish": "es", "German": "de",
    "Chinese": "zh-cn", "Arabic": "ar", "Russian": "ru"
}

voice_language_map = {
    "en": "en-US", "ur": "ur-PK", "hi": "hi-IN",
    "fr": "fr-FR", "es": "es-ES", "de": "de-DE",
    "zh-cn": "zh-CN", "ar": "ar-SA", "ru": "ru-RU"
}

selected_lang = tk.StringVar(value="English")

lang_menu = ttk.Combobox(root, textvariable=selected_lang,
                         values=list(languages.keys()), width=20)
lang_menu.pack(pady=5)