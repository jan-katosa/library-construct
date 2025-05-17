from os.path import join, exists
from os import remove
from tkinter import *
import json
import model.Conlang as cl
import model.Word as word


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
        new_json = {"name": name, "file": f"{name}.json"}
        data.append(new_json)
        
        with open(join("data", "profiles.json"), 'w') as file:
            json.dump(data, file)
            file.close()
        
        lang = cl.Conlang(name)

        #f = open(join("data", "langs", f"{name}.json"), 'w')
        with open(join("data", "langs", f"{name}.json"), 'w') as outfile:
            json.dump(lang, outfile)
            outfile.close()


    def delete_profile(self):
        name = profile_listbox.get(profile_listbox.curselection())
        global data
        data = [x for x in data if x["name"] != name]
        with open(join("data", "profiles.json"), 'w') as file:
            json.dump(data, file)
            file.close()
        if exists(join("data", "langs", f"{name}.json")):
            remove(join("data", "langs", f"{name}.json"))
        else:
            print("Profile does not exist!")

        


app = StartMenu(root)

root.mainloop()