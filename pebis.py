import tkinter as tk
from tkinter import ttk

# detta är ba cookie clicker fast dålig

root = tk.Tk()

pas_unlocked = False
multiplier_value = tk.Label(text=1)
moners = tk.Label(text=0)
# ska fxa bättre namn för valutan senare, just nu bryr jag mig inte
passive_gain = tk.Label(text=0)


def get_passive():
    global pas_unlocked
    x = moners["text"]
    y = passive_gain["text"]
    if float(x) >= 10:
        moners["text"] = f"{float(x) - 10}"
        passive_gain["text"] = f"{float(y) + 0.1}"
        pas_unlocked = True
        passive_button.forget()
        upgrade_passive.pack()
        passive_gain.pack()


def add_moner():
    x = float(moners["text"])
    multiplier = multiplier_value["text"]
    moners["text"] = f"{float(x) + 1 * float(multiplier)}"
    moners["text"] = format(float(moners["text"]), '.1f')


def upgrade():
    x = moners["text"]
    multiplier = multiplier_value["text"]
    if float(x) >= 10 * float(multiplier) or float(x) == 10 * float(multiplier):
        moners["text"] = f"{float(x) - 10 * float(multiplier)}"
        # ska fixa så att de står hur mycket de kostar sen
        moners["text"] = format(float(moners["text"]), '.1f')
        multiplier_value["text"] = f"{float(multiplier) + 0.1}"
        multiplier_value["text"] = format(float(multiplier_value["text"]), '.1f')
        # fuck datorer och hur dem intereagerar med float värden, dedär ovanför tog mig typ en timme att fixa


def passive():
    if pas_unlocked:
        x = float(moners["text"])
        y = float(passive_gain["text"])
        moners["text"] = f"{float(x) + y}"
        moners["text"] = format(float(moners["text"]), '.1f')
    root.after(1000, passive)
    # låser ba upp passiv inkomst


def upgrade_passive():
    y = float(moners["text"])
    x = float(passive_gain["text"])
    if y >= 10 or x == 10:
        moners["text"] = f"{float(y) - 10 * (11 * float(x))}"
        moners["text"] = format(float(moners["text"]), '.1f')
        passive_gain["text"] = f"{float(x) + 0.1}"
        # jag vet inte hur jag ska visa hur mycket det kostar än, men de står där ovanför


root.after(1000, passive)
root.title("Pebis")
root.geometry("500x300")

button = ttk.Button(master=root, text="Moners", command=add_moner)
button.pack()

moners.pack()

blank = tk.Label(text="")
blank.pack()

code_button = ttk.Button(master=root, text="upgrade Click", command=upgrade)
code_button.pack()

multi_sign = tk.Label(text="Click multiplier:")

multi_sign.pack()

multiplier_value.pack()

passive_button = ttk.Button(master=root, text="Passive Income", command=get_passive)
passive_button.pack()

upgrade_passive = ttk.Button(master=root, text="Passive Upgrade", command=upgrade_passive)

# ska eventuellt byta från .pack() till .place() för att positionera bättre

root.mainloop()
