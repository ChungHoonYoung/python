from tkinter import Tk, Frame, Label, Button, messagebox, StringVar
from tkinter.ttk import Combobox

import serial
import serial.tools.list_ports

class robotAarmControl():
    def __init__(self, master):
        self.master = master
        self.master.title("Robot Arm Controller")

        # Serial communication
        self.setup_serial_frame()

    def setup_serial_frame(self):
        serial_frame = Frame(self.master, width = 300)
        serial_frame.pack()

        serial_label = Label(serial_frame, text="Serial port 선택하세요.", bg="yellow", fg="black", padx=100)
        serial_label.pack()




if __name__ == "__name__" :
    root = Tk()
    app = robotAarmControl(root)
    root.mainloop()
