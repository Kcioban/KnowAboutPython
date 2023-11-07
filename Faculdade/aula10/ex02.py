import tkinter as tk

def generate_odd_numbers():
    try:
        start_num = int(start_entry.get())
        end_num = int(end_entry.get())
        if start_num < 0 or end_num < 0:
            raise ValueError("Enter positive integers only")

        odd_numbers = [num for num in range(start_num, end_num + 1) if num % 2 != 0]
        output_label.configure(text="Odd numbers: {}".format(", ".join(map(str, odd_numbers))))
    except ValueError as e:
        output_label.configure(text=str(e))

window = tk.Tk()
window.title("Odd Numbers Generator")

# Create input labels and entries for start and end numbers
start_label = tk.Label(window, text="Start Number:")
start_label.grid(row=0, column=0)
start_entry = tk.Entry(window)
start_entry.grid(row=0, column=1)

end_label = tk.Label(window, text="End Number:")
end_label.grid(row=1, column=0)
end_entry = tk.Entry(window)
end_entry.grid(row=1, column=1)

# Create a button to generate odd numbers
generate_button = tk.Button(window, text="Generate Odd Numbers", command=generate_odd_numbers)
generate_button.grid(row=2, columnspan=2)

# Create a label to display the generated odd numbers
output_label = tk.Label(window, text="")
output_label.grid(row=3, columnspan=2)

window.mainloop()
