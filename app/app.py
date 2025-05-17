from os.path import join
from tkinter import *
import json

root = Tk()
root.title("Library Construct")
root.geometry("600x600")


class StartMenu:
    def __init__(self, master: Tk):
        frame = Frame(master)
        frame.pack()

        welcome_label = Label(frame, text="Welcome to Library Construct!")
        welcome_label.pack()
        choose_label = Label(frame, text="Choose a language profile:")
        choose_label.pack()

        global profile_listbox
        profile_listbox = Listbox(frame)
        profile_listbox.pack()

        global data
        data = None
        with open(join("data", "profiles.json"), 'r') as file:
            data = json.load(file)
            file.close()

        for entry in data:
            profile_listbox.insert(END, entry["name"])

        choose_button = Button(frame, text="Choose", command=self.choose_profile)
        choose_button.pack()
        delete_button = Button(frame, text="Delete", command=self.delete_profile)
        delete_button.pack()
        create_entry = Entry(frame, borderwidth=5)
        create_entry.pack()
        create_button = Button(frame, text="Create", command=lambda: self.create_profile(create_entry.get()))
        create_button.pack()
        quit_button = Button(frame, text="Quit", command=quit)
        quit_button.pack()



    def choose_profile(self): 
        print(f"You have selected {profile_listbox.get(profile_listbox.curselection())}")


    def create_profile(self, name):
        global data
        new_json = {"name": name, "file": name+".json"}
        data.append(new_json)
        with open(join("data", "profiles.json"), 'w') as file:
            json.dump(data, file)


    def delete_profile(self):
        global data
        data = [x for x in data if x["name"] != profile_listbox.get(profile_listbox.curselection())]
        with open(join("data", "profiles.json"), 'w') as file:
            json.dump(data, file)


class CreateConlangDialog:
    def __init__(self, master: Toplevel):
        frame = Frame(master)

        entry = Entry(frame)
        entry.pack()

        button = Button(frame, text="Create", command=self.upload)
        button.pack()


    def upload():
        print("Upload!")


app = StartMenu(root)

root.mainloop()