import tkinter as tk


def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    if bmi < 25:
        return "Normal weight"
    if bmi < 30:
        return "Overweight"
    return "Obese"


def on_calculate():
    try:
        weight = float(weight_entry.get().strip())
        height = float(height_entry.get().strip())

        if weight <= 0 or height <= 0:
            result_label.config(text="Weight and height must be more than 0.")
            return

        bmi = weight / (height ** 2)
        category = classify_bmi(bmi)
        result_label.config(text="BMI: {:.1f} ({})".format(bmi, category))
    except ValueError:
        result_label.config(text="Please enter valid numbers.")


root = tk.Tk()
root.title("BMI Calculator")
root.geometry("380x280")
root.resizable(False, False)
root.configure(padx=20, pady=20)

tk.Label(root, text="BMI Calculator", font=("Arial", 16, "bold")).pack(pady=(0, 15))

weight_frame = tk.Frame(root)
weight_frame.pack(fill="x", pady=5)
tk.Label(weight_frame, text="Weight (kg):", width=14, anchor="w").pack(side="left")
weight_entry = tk.Entry(weight_frame)
weight_entry.pack(side="left", fill="x", expand=True)

height_frame = tk.Frame(root)
height_frame.pack(fill="x", pady=5)
tk.Label(height_frame, text="Height (m):", width=14, anchor="w").pack(side="left")
height_entry = tk.Entry(height_frame)
height_entry.pack(side="left", fill="x", expand=True)

tk.Button(root, text="Calculate", command=on_calculate, width=14).pack(pady=15)

result_label = tk.Label(
    root,
    text="Enter your weight and height.",
    wraplength=320,
    justify="center"
)
result_label.pack()

if __name__ == "__main__":
    root.mainloop()
