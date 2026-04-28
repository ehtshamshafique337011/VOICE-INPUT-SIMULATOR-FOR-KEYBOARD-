import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
import threading
from init_app import root, text_area, languages, voice_language_map, selected_lang, translator

# =========================
# VOICE CONTROL
# =========================
listening = False

def voice_loop():
    global listening
    recognizer = sr.Recognizer()

    # 🔥 FAST SETTINGS (NEW)
    recognizer.energy_threshold = 300
    recognizer.dynamic_energy_threshold = True

    while listening:
        try:
            lang_code = languages[selected_lang.get()]
            voice_lang = voice_language_map.get(lang_code, "en-US")

            with sr.Microphone() as source:
                # ⚡ Faster noise adjustment
                recognizer.adjust_for_ambient_noise(source, duration=0.3)

                # ⚡ QUICK LISTEN (MAIN FIX)
                audio = recognizer.listen(
                    source,
                    timeout=1,              # wait max 1 sec
                    phrase_time_limit=2     # short phrase → fast response
                )

                text = recognizer.recognize_google(audio, language=voice_lang)

                text_area.insert(tk.END, text + " ")
                text_area.see(tk.END)   # auto scroll

        except sr.WaitTimeoutError:
            continue
        except:
            pass

def start_voice():
    global listening
    if not listening:
        listening = True
        text_area.insert(tk.END, "\n[Voice Started]\n")
        threading.Thread(target=voice_loop, daemon=True).start()

def stop_voice():
    global listening
    listening = False
    text_area.insert(tk.END, "\n[Voice Stopped]\n")

# =========================
# TRANSLATE
# =========================
def translate_text():
    try:
        text = text_area.get(1.0, tk.END).strip()
        if not text:
            return

        lang_code = languages[selected_lang.get()]
        translated = translator.translate(text, dest=lang_code)

        text_area.insert(tk.END, f"\n[Translated]:\n{translated.text}\n")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# =========================
# BUTTONS
# =========================
frame = tk.Frame(root, bg="#1e1e1e")
frame.pack(pady=10)

tk.Button(frame, text="🎤 Start", command=start_voice, bg="#22c55e", fg="white").grid(row=0, column=0, padx=5)
tk.Button(frame, text="🔇 Stop", command=stop_voice, bg="#ef4444", fg="white").grid(row=0, column=1, padx=5)
tk.Button(frame, text="Translate", command=translate_text).grid(row=0, column=2, padx=5)