import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import src.music as music
from src.music import Dir
from src.music import Interval
from src.music import Note

def open_file_dialog():
    '''
    Opens a window for the user to select the source file they wish to transpose
    '''
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    file_path = filedialog.askopenfilename(
        title="Select a File",
        filetypes=[("Word Documents", "*.doc*"), ("All files", "*.*")]
        # Optional: Uncomment next line to add default directory to open
        #initialdir="/default/directory/to/open/"
    )

    if file_path:
        return file_path

def get_transpose_params():
    '''
    Opens window for user to decide how they wish to transpose their chord chart.
    There are two options for transposition:\n
    One: Pick an interval and a direction to transpose (ex: Up a Major Second). Any
    transposition downwards will be redefined as an equivalent transposition upwards\n
    Two: Indicate the original key and the target key (ex: Transpose from C to D). Will
    be defined as an upwards transposition in all cases\n
    returns:
            semitones (int)- The number of semitones (upwards) to tranpose\n
            scale_degree (int)- The number of scale degrees (upwards) to tranpose
    '''
    semitones = -1
    scale_degree = -1

    def intervals_ret():
        nonlocal semitones, scale_degree # For purposes of scope

        #Grab interval and direction chosen from table
        interval_chosen = Interval[interval_var.get()]
        direction = Dir[direction_var.get()]
        
        # Case when transposition direction is up
        if direction.value == 0:  
            #return_val = interval_chosen.value
            semitones = interval_chosen.value[0]
            scale_degree = interval_chosen.value[1]
        # Case when transposition direction is down
        else:
             # Pitch is defined in mod12. Use this wrap around
             # So that a transposition downwards may be redefined with
             # a value upwards that is functionally equivalent
             interval = 12 - interval_chosen.value[0]
             semitones = music.intervals_array[interval].value[0]
             scale_degree = music.intervals_array[interval].value[1]
        # Exit GUI window
        root.quit()

    def key_to_key_ret():
        nonlocal semitones, scale_degree    # For purposes of scope
        
        # Grab original and target keys chosen from table
        new = Note[New_Key_var.get()]
        old = Note[Old_Key_var.get()]

        # Find difference between two keys in terms of semitones
        delta = new.value[1] - old.value[1]
        
        # Use mod12 wrap around to always define transposition as upwards
        if delta < 0:
             delta = 12 + delta
        semitones = music.intervals_array[delta].value[0]
        scale_degree = music.intervals_array[delta].value[1]
        # Exit GUI window
        root.quit()
    
    def window_closed():
        # Alert python that window has been closed
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

    root.protocol("WM_DELETE_WINDOW", window_closed)

    # Run the main loop
    root.mainloop()

    return semitones, scale_degree