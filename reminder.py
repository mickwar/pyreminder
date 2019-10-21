from sys import argv
from time import sleep
from tkinter import messagebox, Tk


# Parse arguments
if len(argv) > 1:
    timer = int(argv[1])
else:
    timer = 10

if len(argv) > 2:
    message = argv[2]
else:
    message = "Take a break"


# Main function
if __name__ == "__main__":
    # Loop until process exits
    while True:
        sleep(timer * 60)
        window = Tk()
        window.wm_withdraw()
        messagebox.showinfo("Reminder", message)
        window.destroy()

    quit()

