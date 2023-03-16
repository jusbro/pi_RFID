import tkinter as tk
import time

homeroomColor = '#de97a7'
clubColor = '#bad98d'
period1Color = '#e6491e'
period2Color = '#961ee6'
period3Color = '#e6c11e'
period4Color = '#d2a3f0'
labColor = '#e61e1e'
period7Color = '#7be61e'
flexColor = '#1ee6d2'


class Period:
    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end

# Define the periods
periods = [
    Period("Homeroom", "07:30 AM", "07:38 AM"),
    Period("Period 1 Astronomy", "08:20 AM", "08:57 AM"),
    Period("Period 2 Computer Science", "09:00 AM", "09:37 AM"),
    Period("Period 3 Astronomy", "09:40 AM", "10:17 AM"),
    Period("Period 4 Physics", "10:20 AM", "10:57 AM"),
    Period("Period 6 Physics Lab", "12:14 PM", "12:59 PM"),
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
root.geometry("1280x1024")

# Create a new Toplevel window for cycle day selection
cycle_window = tk.Toplevel(root)
cycle_window.attributes('-topmost', True)
cycle_window.geometry("1280x1024")
cycle_window.configure(bg='#4eeddb')

cycle_label = tk.Label(cycle_window, text="What day of the cycle is it (1-6)?", font=("Helvetica", 55), bg='#4eeddb')
cycle_label.pack(pady=40)

for i in range(1, 7):
    button = tk.Button(cycle_window, text=str(i), font=("Helvetica", 40), bg = '#c1dbd8',command=lambda i=i: select_cycle_day(i))
    button.pack(pady=10)

# Define a function to handle the user input for cycle day
def select_cycle_day(day):
    global cycle_day
    cycle_day = day
    cycle_window.destroy()

# Wait for the user to select the cycle day before updating the labels
cycle_day = None
cycle_window.wait_window()

# Define the labels for the time and period
time_label = tk.Label(root, font=("Helvetica", 160))
time_label.pack(pady=20)

period_label = tk.Label(root, font=("Helvetica", 75))
period_label.pack()

# Define the function to update the time and period labels
def update_time():
    current_time = time.strftime("%I:%M:%S %p")
    current_period = get_current_period()
    period_info = ""
    
    if current_period:
        period_info += f"{current_period.name}\n"
        period_info += f"{current_period.start} to {current_period.end}\n"
        
        # Set the background color of the window and labels based on the current period
        if current_period.name == "Homeroom":
            root.configure(bg=homeroomColor)
            time_label.configure(bg=homeroomColor)
            period_label.configure(bg=homeroomColor)
        elif current_period.name == "Club":
            root.configure(bg=clubColor)
            time_label.configure(bg=clubColor)
            period_label.configure(bg=clubColor)
        elif current_period.name == "Period 1 Astronomy":
            root.configure(bg=period1Color)
            time_label.configure(bg=period1Color)
            period_label.configure(bg=period1Color)
        elif current_period.name == "Period 2 Computer Science":
            root.configure(bg=period2Color)
            time_label.configure(bg=period2Color)
            period_label.configure(bg=period2Color)
        elif current_period.name == "Period 3 Astronomy":
            root.configure(bg=period3Color)
            time_label.configure(bg=period3Color)
            period_label.configure(bg=period3Color)
        elif current_period.name == "Period 4 Physics":
            root.configure(bg=period4Color)
            time_label.configure(bg=period4Color)
            period_label.configure(bg=period4Color)
        elif current_period.name == "Period 7 Computer Science":
            root.configure(bg=period7Color)
            time_label.configure(bg=period7Color)
            period_label.configure(bg=period7Color)
        elif current_period.name == "FLEX Period":
            root.configure(bg=flexColor)
            time_label.configure(bg=flexColor)
            period_label.configure(bg=flexColor)
        elif current_period.name == "Period 6 Physics Lab":
            root.configure(bg=labColor)
            time_label.configure(bg=labColor)
            period_label.configure(bg=labColor)
    
    if cycle_day:
        period_info = f"Day {cycle_day}\n{period_info}"
    
    time_label.config(text=current_time)
    period_label.config(text=period_info)
    
    root.after(1000, update_time)

# Start updating the time and period labels
update_time()

# Start the Tkinter event loop
root.mainloop()
