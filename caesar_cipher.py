import tkinter as tk
from tkinter import messagebox
from tkinter import font

def caesar_cipher(text, shift, mode='encrypt'):
    if mode not in ['encrypt', 'decrypt']:
        raise ValueError("Mode must be 'encrypt' or 'decrypt'")

    if mode == 'decrypt':
        shift = -shift

    result = []
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - start + shift) % 26 + start
            result.append(chr(shifted))
        else:
            result.append(char)

    return ''.join(result)

def process_text():
    mode = mode_var.get()
    text = text_entry.get("1.0", tk.END).strip()
    try:
        shift = int(shift_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer.")
        return

    if not text:
        messagebox.showerror("Invalid Input", "Text cannot be empty.")
        return

    try:
        result = caesar_cipher(text, shift, mode)
        result_display.config(state="normal")
        result_display.delete("1.0", tk.END)
        result_display.insert("1.0", result)
        result_display.config(state="disabled")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def clear_fields():
    text_entry.delete("1.0", tk.END)
    shift_entry.delete(0, tk.END)
    result_display.config(state="normal")
    result_display.delete("1.0", tk.END)
    result_display.config(state="disabled")

def exit_program():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Caesar Cipher")
root.geometry("550x500")
root.resizable(False, False)

default_font = font.Font(family="Helvetica", size=12)
header_font = font.Font(family="Helvetica", size=16, weight="bold")

# Header
header_label = tk.Label(root, text="Caesar Cipher Tool", font=header_font)
header_label.pack(pady=10)

# Mode selection
mode_label = tk.Label(root, text="Mode:", font=default_font)
mode_label.pack(pady=5)

mode_var = tk.StringVar(value="encrypt")
encrypt_radio = tk.Radiobutton(root, text="Encrypt", variable=mode_var, value="encrypt", font=default_font)
decrypt_radio = tk.Radiobutton(root, text="Decrypt", variable=mode_var, value="decrypt", font=default_font)
encrypt_radio.pack()
decrypt_radio.pack()

# Text input
text_label = tk.Label(root, text="Enter text:", font=default_font)
text_label.pack(pady=5)

text_entry = tk.Text(root, height=5, width=60, font=default_font, relief="sunken", bd=2)
text_entry.pack(pady=5)

# Shift input
shift_label = tk.Label(root, text="Enter shift value:", font=default_font)
shift_label.pack(pady=5)

shift_entry = tk.Entry(root, font=default_font, relief="sunken", bd=2)
shift_entry.pack(pady=5)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

process_button = tk.Button(button_frame, text="Process", command=process_text, font=default_font, bg="lightblue")
process_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(button_frame, text="Clear", command=clear_fields, font=default_font, bg="lightyellow")
clear_button.grid(row=0, column=1, padx=10)

exit_button = tk.Button(button_frame, text="Exit", command=exit_program, font=default_font, bg="lightcoral")
exit_button.grid(row=0, column=2, padx=10)

# Result label and display
result_label = tk.Label(root, text="Result:", font=default_font)
result_label.pack(pady=5)

result_display = tk.Text(root, height=5, width=60, font=default_font, state="disabled", bg="white", relief="sunken", bd=2, wrap="word")
result_display.pack(pady=10)

# Run the GUI
root.mainloop()
