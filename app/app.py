from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Library Construct")

main_frame = ttk.Frame(root, padding=5)
main_frame.grid()


# Message on the top of the application window
ttk.Label(main_frame, text="Welcome to Library Construct!").grid(column=0, row=0)
ttk.Label(main_frame, text="Choose a language profile:").grid(column=0, row=1)

# TODO: Profile table/list
ttk.Label(main_frame, text="Profile 1").grid(column=0, row=2)


root.mainloop()