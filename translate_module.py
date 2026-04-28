from tkinter import messagebox
from init_app import text_area, translator, languages, selected_lang

def translate_text():
    try:
        text = text_area.get(1.0, "end").strip()
        if not text:
            return

        lang_code = languages[selected_lang.get()]
        translated = translator.translate(text, dest=lang_code)

        text_area.insert("end", f"\n[Translated]:\n{translated.text}\n")
    except Exception as e:
        messagebox.showerror("Error", str(e))