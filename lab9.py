import tkinter as tk

entry = None

def click(event):
    global entry
    current = entry.get()
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(current, {"__builtins__": None}, {})
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

def main():
    global entry
    root = tk.Tk()
    root.title("Calculator")
    root.geometry("300x400")
    root.resizable(False, False)

    entry = tk.Entry(
        root,
        font=("Arial", 20),
        justify="right",
        bd=10,
        relief=tk.RIDGE
    )
    entry.pack(fill=tk.BOTH, ipadx=8, ipady=10, padx=10, pady=10)

    button_frame = tk.Frame(root)
    button_frame.pack(expand=True, fill="both")

    buttons = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["C", "0", "=", "+"]
    ]

    for row in buttons:
        row_frame = tk.Frame(button_frame)
        row_frame.pack(expand=True, fill="both")

        for btn_text in row:
            btn = tk.Button(
                row_frame,
                text=btn_text,
                font=("Arial", 18),
                relief=tk.GROOVE,
                bd=4
            )
            btn.pack(side="left", expand=True, fill="both")
            btn.bind("<Button-1>", click)

    root.mainloop()

if __name__ == "__main__":
    main()
