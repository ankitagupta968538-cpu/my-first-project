import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator
import pyttsx3

engine = pyttsx3.init()

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def translate_text():
    try:
        text = input_text.get("1.0", tk.END).strip()
        src = src_lang.get()
        dest = dest_lang.get()

        if not text:
            messagebox.showwarning("Warning", "Text likho pehle")
            return

        translated = GoogleTranslator(source=src, target=dest).translate(text)

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated)

    except Exception as e:
        messagebox.showerror("Error", str(e))

def speak_translation():
    text = output_text.get("1.0", tk.END).strip()
    if text:
        speak_text(text)

# ---------- GUI ----------
root = tk.Tk()
root.title("Translator with Text To Speech")
root.geometry("600x450")

langs = ["auto","en","hi"]

frame = tk.Frame(root)
frame.pack(pady=10)

src_lang = ttk.Combobox(frame, values=langs, width=10)
src_lang.set("auto")
src_lang.grid(row=0, column=0, padx=10)

dest_lang = ttk.Combobox(frame, values=langs, width=10)
dest_lang.set("hi")
dest_lang.grid(row=0, column=1, padx=10)

input_text = tk.Text(root, height=6)
input_text.pack(fill="x", padx=20)

tk.Button(root, text="Translate", command=translate_text).pack(pady=10)

output_text = tk.Text(root, height=6)
output_text.pack(fill="x", padx=20)

tk.Button(root, text="🔊 Speak Translation", command=speak_translation).pack(pady=10)

root.mainloop()
