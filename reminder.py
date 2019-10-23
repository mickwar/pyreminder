#!/usr/bin/env python3

from sys import argv
from time import sleep, time
from tkinter import messagebox, Tk

# Parse arguments
if len(argv) < 2:
    print("")
    print("Usage: reminder.py length [total] [message]")
    print("")
    print("Opens a pop-up menu displaying `message` every `length` minutes until `total` minutes have elapsed")
    print("Leave `total` blank for one time use. Use `total` = inf for an indefinite period of time")
    print("`message` defaults to 'Take a break'")
    print("")
    quit()

length = float(argv[1])

if len(argv) == 3:
    total = float(argv[2])
else:
    total = length

if len(argv) == 4:
    message = argv[3]
else:
    message = "Take a break"


# Main function
if __name__ == "__main__":

    if length > total and total > 0:
        print("Note: `length` is greater than `total`, reminder will only pop-up once.")

    if total == float('inf'):
        print("Note: Reminders will pop-up indefinitely")

    START = time()

    # Loop until until time goes beyond given length
    while time() < START + total * 60:
        # Using sleep in conjunction with the messagebox means that the time
        # from closing the pop-up until the next one will be length * 60, NOT
        # that the message will pop-up at exactly the length * 60 intervals.
        # So if a message is left up for a while, the next pop-up will be offset.
        sleep(length * 60)
        window = Tk()
        window.wm_withdraw()
        messagebox.showinfo("Reminder", message)
        window.destroy()

    quit()

