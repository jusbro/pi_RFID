import tkinter as tk
import time

class Period:
    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end

# Define the periods
periods = [
    Period("Homeroom", "07:30 AM", "07:38 AM"),
    Period("Period 1 Astronomy", "07:41 AM", "08:26 AM"),
    Period("Period 2 Computer Science", "08:29 AM", "09:14 AM"),
    Period("Period 3 Astronomy", "09:17 AM", "10:02 AM"),
    Period("Period 4 Physics", "10:05 AM", "10:50 AM"),
    Period("Period 7 Computer Science", "01:02 PM", "01:47 PM"),
    Period("FLEX Period", "01:50 PM", "02:30 PM"),
]

# Define a function to get the current period
def get_current_period():
    current_time = time.strftime("%I:%M %p")
    current_period = None
    
    for period in periods:
        if current_time >= period.start and current_time <= period.end:
            current_period = period
            break
    
    return current_period

# Define the Tkinter window
root = tk.Tk()
root.geometry("800x480")

# Define a function to handle the user input for cycle day
def select_cycle_day(day):
    global cycle_day
    cycle_day = day
    cycle_window.destroy()

# Create a new Toplevel window for cycle day selection
cycle_window = tk.Toplevel(root)

cycle_label = tk.Label(cycle_window, text="What day of the cycle is it (1-6)?", font=("Helvetica", 24))
cycle_label.pack(pady=20)

for i in range(1, 7):
    button = tk.Button(cycle_window, text=str(i), font=("Helvetica", 24), command=lambda i=i: select_cycle_day(i))
    button.pack(pady=10)

# Define the labels for the time and period
time_label = tk.Label(root, font=("Helvetica", 160))
time_label.pack(pady=20)

period_label = tk.Label(root, font=("Helvetica", 75))
period_label.pack()

# Wait for the user to select the cycle day before updating the labels
cycle_day = None
cycle_window.wait_window()

# Define the function to update the time and period labels
def update_time():
    current_time = time.strftime("%I:%M:%S %p")
    current_period = get_current_period()
    period_info = ""
    
    if current_period:
        period_info += f"{current_period.name}\n"
        period_info += f"{current_period.start} to {current_period.end}\n"
    
    if cycle_day:
        period_info = f"Day {cycle_day}\n{period_info}"
    
    time_label.config(text=current_time)
    period_label.config(text=period_info)
    
    root.after(1000, update_time)

# Start updating the time and period labels
update_time()

# Start the Tkinter event loop
root.mainloop()
