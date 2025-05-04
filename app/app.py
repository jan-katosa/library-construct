from os.path import join
from tkinter import *
import json
import commands

root = Tk()
root.title("Library Construct")

main_frame = Frame(root)
main_frame.grid()


# Message on the top of the application window
Label(main_frame, text="Welcome to Library Construct!").grid(column=0, columnspan=2, row=0, padx=5)
Label(main_frame, text="Choose a language profile:").grid(column=0, columnspan=2, row=1, padx=5)

profile_listbox = Listbox(root)
profile_listbox.grid(column=0, columnspan=2, row=2, rowspan=2, pady=15, padx=10)

with open(join("data", "profiles.json"), 'r') as file:
    data = json.load(file)

for entry in data:
    profile_listbox.insert(END, entry)

choose_button = Button(root, text="Choose", command=commands.choose_profile)
choose_button.grid(column=0, row=4, pady=5)
delete_button = Button(root, text="Delete", command=commands.delete_profile)
delete_button.grid(column=1, row=4, pady=5)
quit_button = Button(root, text="Quit", command=quit)
quit_button.grid(column=0, row=5, pady=5)

root.mainloop()