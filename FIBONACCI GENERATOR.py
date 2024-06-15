import tkinter as tk
from tkinter import messagebox

def generate_fibonacci():
    try:
        n = int(entry.get())
        if n <= 0:
            raise ValueError("The number must be positive.")
    except ValueError as e:
        messagebox.showerror("Invalid input", f"Please enter a valid positive integer.\n\nError: {e}")
        return
    
    fibonacci_series = [0, 1]
    for i in range(2, n):
        next_number = fibonacci_series[-1] + fibonacci_series[-2]
        fibonacci_series.append(next_number)
    
    result_label.config(text=f"Fibonacci series up to {n} terms:\n{', '.join(map(str, fibonacci_series))}")

#set up the main window
root = tk.Tk()
root.title("Fibonacci Series Generator")

#create label, entry, and button widgets
tk.Label(root, text="Enter the number of terms:").pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=10)

generate_button = tk.Button(root, text="Generate", command=generate_fibonacci)
generate_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

#start the fibbonaci generator
root.mainloop()
