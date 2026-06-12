import tkinter as tk
from tkinter import messagebox
import random
import string


def generate_password():
    try:
        length = int(length_entry.get())

        if length < 8:
            messagebox.showerror(
                "Error",
                "Password length must be at least 8."
            )
            return

        use_letters = letters_var.get()
        use_numbers = numbers_var.get()
        use_symbols = symbols_var.get()
        exclude_similar = exclude_var.get()

        if not (use_letters or use_numbers or use_symbols):
            messagebox.showerror(
                "Error",
                "Select at least one character type."
            )
            return

        letters = string.ascii_letters
        numbers = string.digits
        symbols = "!#$%&()*+"

        # Exclude confusing characters
        if exclude_similar:
            confusing = "O0Il1"

            letters = "".join(
                ch for ch in letters if ch not in confusing
            )

            numbers = "".join(
                ch for ch in numbers if ch not in confusing
            )

        password_chars = []

        # Security Rules
        if use_letters:
            password_chars.append(random.choice(string.ascii_lowercase))
            password_chars.append(random.choice(string.ascii_uppercase))

        if use_numbers:
            password_chars.append(random.choice(numbers))

        if use_symbols:
            password_chars.append(random.choice(symbols))

        pool = ""

        if use_letters:
            pool += letters

        if use_numbers:
            pool += numbers

        if use_symbols:
            pool += symbols

        remaining = length - len(password_chars)

        for _ in range(remaining):
            password_chars.append(random.choice(pool))

        random.shuffle(password_chars)

        password = "".join(password_chars)

        password_var.set(password)

        # Strength Indicator
        if length >= 14:
            strength_var.set("Strong")
        elif length >= 10:
            strength_var.set("Medium")
        else:
            strength_var.set("Weak")

    except ValueError:
        messagebox.showerror(
            "Error",
            "Enter a valid number."
        )


def copy_password():
    password = password_var.get()

    if password:
        root.clipboard_clear()
        root.clipboard_append(password)

        messagebox.showinfo(
            "Copied",
            "Password copied to clipboard."
        )


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("500x450")
root.resizable(False, False)

title = tk.Label(
    root,
    text="Advanced Password Generator",
    font=("Arial", 16, "bold")
)
title.pack(pady=10)

# Length
tk.Label(
    root,
    text="Password Length:"
).pack()

length_entry = tk.Entry(root)
length_entry.pack(pady=5)

# Checkboxes
letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)
exclude_var = tk.BooleanVar()

tk.Checkbutton(
    root,
    text="Include Letters",
    variable=letters_var
).pack(anchor="w", padx=120)

tk.Checkbutton(
    root,
    text="Include Numbers",
    variable=numbers_var
).pack(anchor="w", padx=120)

tk.Checkbutton(
    root,
    text="Include Symbols",
    variable=symbols_var
).pack(anchor="w", padx=120)

tk.Checkbutton(
    root,
    text="Exclude Similar Characters (O,0,I,l,1)",
    variable=exclude_var
).pack(anchor="w", padx=120)

# Generate Button
tk.Button(
    root,
    text="Generate Password",
    command=generate_password,
    width=20
).pack(pady=15)

# Password Display
password_var = tk.StringVar()

tk.Label(
    root,
    text="Generated Password:"
).pack()

password_entry = tk.Entry(
    root,
    textvariable=password_var,
    width=40,
    font=("Arial", 12)
)

password_entry.pack(pady=5)

# Strength
strength_var = tk.StringVar()

tk.Label(
    root,
    text="Password Strength:"
).pack()

strength_label = tk.Label(
    root,
    textvariable=strength_var,
    font=("Arial", 12, "bold")
)

strength_label.pack()

# Copy Button
tk.Button(
    root,
    text="Copy to Clipboard",
    command=copy_password,
    width=20
).pack(pady=15)

root.mainloop()