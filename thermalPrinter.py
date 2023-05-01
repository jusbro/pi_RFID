import tkinter as tk
import time
import serial
uart = serial.Serial("/dev/serial0", baudrate=19200, timeout=3000)
import adafruit_thermal_printer

ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.69)

printer = ThermalPrinter(uart)

class HomeScreen:
    def __init__(self, master):
        self.master = master
        master.title("HomeScreen")

        # Set background color to light purple
        master.configure(bg='#D3D3EA')

        # Set the window size to 1920x1080 and launch it full screen
        master.geometry("1920x1080")

        # Create label to display time
        self.time_label = tk.Label(master, text='', font=('Helvetica', 150), bg='#D3D3EA')
        self.time_label.pack(pady=50)

        # Update the time label every second
        self.update_time()

        # Create sign-in and sign-out buttons
        self.sign_out_button = tk.Button(master, text='Sign Out', font=('Helvetica', 75),width=12, height=3, command=self.sign_out, bg='#FFDAB9')
        self.sign_out_button.pack(side=tk.LEFT, padx=50, pady=20)

        self.sign_in_button = tk.Button(master, text='Sign In', font=('Helvetica', 75),width=12, height=3, command=self.sign_in, bg='#FFDAB9')
        #self.sign_in_button.pack(side=tk.RIGHT, padx=50, pady=20)

        # Create teacher login button
        self.teacher_login_button = tk.Button(master, text='Teacher Login', font=('Helvetica', 15),command=self.teacher_login, bg='white')
        #self.teacher_login_button.pack(side=tk.BOTTOM, pady=20)

    def update_time(self):
        """Updates the time label every second"""
        current_time = time.strftime('%I:%M:%S %p')
        self.time_label.configure(text=current_time)
        self.master.after(1000, self.update_time)
    def sign_out(self):
        # Create a new window for sign out
        sign_out_window = tk.Toplevel(self.master)
        sign_out_window.title('Sign Out')
        sign_out_window.geometry("1920x1080")
        sign_out_window.configure(bg='#D3D3EA')

        # Create label to display "Sign Out"
        sign_out_label = tk.Label(sign_out_window, text='Sign Out', font=('Helvetica', 100), bg='#D3D3EA')
        sign_out_label.pack()

        # Create label to display "Enter your Name"
        enter_name_label = tk.Label(sign_out_window, text='Enter your Name', font=('Helvetica', 75), bg='#D3D3EA')
        enter_name_label.pack(pady=5)

        # Create entry box for user to input their name
        name_entry = tk.Entry(sign_out_window, font=('Helvetica', 50), justify='center')
        name_entry.pack(pady=50)

        # Create label to display "Select your Destination"
        select_destination_label = tk.Label(sign_out_window, text='Select your Destination', font=('Helvetica', 50), bg='#D3D3EA')
        select_destination_label.pack(pady=50)

        # Create a list of destination names
        destinations = ['Office', 'Nurse', 'Locker', 'Bathroom', 'Guidance', 'Teacher']

        # Create a variable to hold the selected destination
        var = tk.StringVar()

        # Create a frame to hold the destination buttons
        button_frame = tk.Frame(sign_out_window, bg='#D3D3EA')
        button_frame.pack()

        # Create buttons for each destination
        for i in range(len(destinations)):
            destination_button = tk.Button(button_frame, text=destinations[i], font=('Helvetica', 30), width=15, height=2,
                                           bg='#FFDAB9', command=lambda dest=destinations[i]: var.set(dest))
            destination_button.grid(row=i//3, column=i%3, padx=10, pady=10)

        # Creat Confirmation Text to view the selected destination and name
        confirm_text = tk.Label(sign_out_window, textvariable="test", font=('Helvetica', 50), bg='#D3D3EA')
        confirm_text.pack()


        # Create "Confirm" and "Cancel" buttons
        confirm_button = tk.Button(sign_out_window, text='Confirm', font=('Helvetica', 50), bg='#FFDAB9',
                                    command=lambda: self.confirm_sign_out(name_entry.get(), var.get(), sign_out_window))
        confirm_button.pack(side=tk.LEFT, padx=50, pady=20)

        cancel_button = tk.Button(sign_out_window, text='Cancel', font=('Helvetica', 50), bg='#FFDAB9',
                                    command=sign_out_window.destroy)
        cancel_button.pack(side=tk.RIGHT, padx=50, pady=20)
    
    def print_pass(self, name, destination):
        current_time = time.strftime('%I:%M:%S %p')
        current_Date = time.strftime('%a %b %d %Y')
        print("Printing Pass")
        printer.bold = True
        printer.feed(1)
        printer.size = adafruit_thermal_printer.SIZE_LARGE
        printer.print("Hallway Pass")
        printer.feed(2)
        printer.bold = False
        printer.size = adafruit_thermal_printer.SIZE_SMALL
        printer.print("Student: "+name)
        printer.feed(1)
        printer.print("Origin: Mr. Brown")
        printer.feed(1)
        printer.print("Destination: "+destination)
        printer.feed(1)
        printer.print("Departure Time: " + str(current_time))
        printer.print("Departure Date: " + str(current_Date))
        printer.feed(1)
        printer.bold = True 
        printer.print("Returning Teacher Signature:")
        printer.feed(1)
        printer.underline = adafruit_thermal_printer.UNDERLINE_THICK
        printer.print("_________________________________")
        printer.feed(1)

        printer.print("Time: ___________________")
        printer.feed(1)

        printer.print("PASS AUTHORIZED BY MR. BROWN")
        printer.print("call 2133 with any questions.")
        printer.feed(3)

    def confirm_sign_out(self, name, destination, sign_out_window):
        # Print the name and destination to the console
        print(f"{name} is signing out for {destination}")

        # Close the sign out window
        self.print_pass(name, destination)
        sign_out_window.destroy()

    def sign_in(self):
        print("Sign In")

    def teacher_login(self):
        # Create a new window for teacher login
        teacher_login_window = tk.Toplevel(self.master)
        teacher_login_window.title('Teacher Login')
        teacher_login_window.geometry("1920x1080")
        teacher_login_window.configure(bg='#D3D3EA')
             

    def run(self):
        # Update the time label every second
        self.update_time()

        # Run the GUI
        self.master.mainloop()

root = tk.Tk()
my_gui = HomeScreen(root)
my_gui.run()
