import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import music
from music import Dir
from music import Interval
from music import Note

def open_file_dialog():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    file_path = filedialog.askopenfilename(
        title="Select a File",
        filetypes=[("Word Documents", "*.doc*"), ("All files", "*.*")]
    )

    if file_path:
        return file_path

def get_transpose_params():
    result = {}

    def intervals_ret():
        interval_chosen = Interval[interval_var.get()]
        direction = Dir[direction_var.get()]
        if direction.value == 0:  
            return_val = interval_chosen.value
        else:
             interval = 12 - interval_chosen.value[0]
             return_val = music.intervals_array[interval].value
        result["Transpose"] = return_val
        root.quit()

    def key_to_key_ret():
        new = Note[New_Key_var.get()]
        old = Note[Old_Key_var.get()]
        delta = new.value[1] - old.value[1]
        if delta < 0:
             delta = 12 + delta
        result["Transpose"] = music.intervals_array[delta].value
        root.quit()

    # Create the main window
    root = tk.Tk()
    root.title("Chord Transposition")

    message_label = tk.Label(root, text="Transpose using interval and direction or from key to key")
    message_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    # Left side: Interval dropdown
    interval_label = ttk.Label(root, text="Interval:")
    interval_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
    interval_var = tk.StringVar(root)
    interval_dropdown = ttk.OptionMenu(root, interval_var, Interval.UNISON.name, *[(interval.name) for interval in Interval])
    interval_dropdown.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    # Left side: Direction dropdown
    direction_label = ttk.Label(root, text="Direction:")
    direction_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
    direction_var = tk.StringVar(root)
    direction_dropdown = ttk.OptionMenu(root, direction_var, Dir.UP.name, *[(dir.name) for dir in Dir])
    direction_dropdown.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    # Left side: Transpose button
    transpose_button_left = ttk.Button(root, text="Transpose", command=intervals_ret)
    transpose_button_left.grid(row=3, column=0, columnspan=2, pady=10)

    # Right side: Interval dropdown
    Old_Key_label = ttk.Label(root, text="Old Key:")
    Old_Key_label.grid(row=1, column=2, padx=10, pady=10, sticky="e")
    Old_Key_var = tk.StringVar(root)
    Old_Key_dropdown = ttk.OptionMenu(root, Old_Key_var, Note.C.name, *[(note.name) for note in Note])
    Old_Key_dropdown.grid(row=1, column=3, padx=10, pady=10, sticky="w")

    # Right side: Direction dropdown
    New_Key_label = ttk.Label(root, text="New Key:")
    New_Key_label.grid(row=2, column=2, padx=10, pady=10, sticky="e")
    New_Key_var = tk.StringVar(root)
    New_Key_dropdown = ttk.OptionMenu(root, New_Key_var, Note.C.name, *[(note.name) for note in Note])
    New_Key_dropdown.grid(row=2, column=3, padx=10, pady=10, sticky="w")

    # Right side: Transpose button
    transpose_button_right = ttk.Button(root, text="Transpose", command=key_to_key_ret)
    transpose_button_right.grid(row=3, column=2, columnspan=2, pady=10)

    # Run the main loop
    root.mainloop()

    return result