import tkinter as tk

def calculate_median():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        num3 = float(num3_entry.get())

        median = (num1 + num2 + num3) / 3
        output_label.configure(text="Median: {:.2f}".format(median))
    except ValueError as e:
        output_label.configure(text=str(e))

window = tk.Tk()
window.title("Median Calculator")

# Create input labels and entries for three numbers
num1_label = tk.Label(window, text="Number 1:")
num1_label.grid(row=0, column=0)
num1_entry = tk.Entry(window)
num1_entry.grid(row=0, column=1)

num2_label = tk.Label(window, text="Number 2:")
num2_label.grid(row=1, column=0)
num2_entry = tk.Entry(window)
num2_entry.grid(row=1, column=1)

num3_label = tk.Label(window, text="Number 3:")
num3_label.grid(row=2, column=0)
num3_entry = tk.Entry(window)
num3_entry.grid(row=2, column=1)

# Create a button to calculate the median
calculate_button = tk.Button(window, text="Calculate Median", command=calculate_median)
calculate_button.grid(row=3, columnspan=2)

# Create a label to display the calculated median
output_label = tk.Label(window, text="")
output_label.grid(row=4, columnspan=2)

window.mainloop()
