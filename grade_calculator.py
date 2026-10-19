import tkinter as tk


def grade_from_average(average):
    if average >= 90:
        return "A"
    if average >= 80:
        return "B"
    if average >= 70:
        return "C"
    if average >= 60:
        return "D"
    return "F"


def on_get_grade():
    try:
        scores = [float(entry.get().strip()) for entry in score_entries]

        if any(score < 0 or score > 100 for score in scores):
            raise ValueError

        average = sum(scores) / len(scores)
        letter = grade_from_average(average)
        grade_label.config(text="Average: {:.1f} ({})".format(average, letter))
    except ValueError:
        grade_label.config(text="Enter scores between 0 and 100.")


root = tk.Tk()
root.title("Grade Calculator")
root.geometry("380x320")
root.resizable(False, False)
root.configure(padx=20, pady=20)

tk.Label(root, text="Grade Calculator", font=("Arial", 16, "bold")).pack(pady=(0, 15))

score_entries = []
assessment_names = ["Test 1:", "Test 2:", "Exam:"]

for name in assessment_names:
    row = tk.Frame(root)
    row.pack(fill="x", pady=5)
    tk.Label(row, text=name, width=14, anchor="w").pack(side="left")
    entry = tk.Entry(row)
    entry.pack(side="left", fill="x", expand=True)
    score_entries.append(entry)

tk.Button(root, text="Get Grade", command=on_get_grade, width=14).pack(pady=15)

grade_label = tk.Label(
    root,
    text="Enter three scores from 0 to 100.",
    wraplength=320,
    justify="center"
)
grade_label.pack()

if __name__ == "__main__":
    root.mainloop()
