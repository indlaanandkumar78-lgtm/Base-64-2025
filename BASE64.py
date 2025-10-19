import base64
import tkinter as tk
from tkinter import messagebox

def encode_text():
    text = input_text.get("1.0", tk.END).strip()
    if text:
        encoded = base64.b64encode(text.encode("utf-8")).decode("utf-8")
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, encoded)
    else:
        messagebox.showwarning("Warning", "Please enter text to encode!")

def decode_text():
    text = input_text.get("1.0", tk.END).strip()
    if text:
        try:
            decoded = base64.b64decode(text.encode("utf-8")).decode("utf-8")
            output_text.delete("1.0", tk.END)
            output_text.insert(tk.END, decoded)
        except Exception:
            messagebox.showerror("Error", "Invalid Base64 text!")
    else:
        messagebox.showwarning("Warning", "Please enter text to decode!")

# --- Tkinter UI setup ---
root = tk.Tk()
root.title("Base64 Encoder / Decoder")
root.geometry("400x400")
root.resizable(False, False)

# Input label and text box
tk.Label(root, text="Enter text:", font=("Arial", 12, "bold")).pack(pady=5)
input_text = tk.Text(root, height=5, width=45)
input_text.pack()

# Buttons for encode/decode
tk.Button(root, text="Encode", command=encode_text, bg="lightgreen", width=15).pack(pady=5)
tk.Button(root, text="Decode", command=decode_text, bg="lightblue", width=15).pack(pady=5)

# Output label and text box
tk.Label(root, text="Output:", font=("Arial", 12, "bold")).pack(pady=5)
output_text = tk.Text(root, height=5, width=45)
output_text.pack()

root.mainloop()