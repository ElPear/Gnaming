import tkinter as tk
from tkinter import ttk

# detta är ba cookie clicker fast dålig

root = tk.Tk()

pas_unlocked = False
multiplier_value = tk.Label(text=1)
moners = tk.Label(text=0.0)
# ska fixa bättre namn för valutan senare, just nu bryr jag mig inte
passive_gain = tk.Label(text=0)
Moners_per_second = tk.Label(text="Moners/s: " + str(passive_gain["text"] + 0.1))


def get_passive():
    global pas_unlocked
    x = moners["text"]
    y = passive_gain["text"]
    if float(x) >= 10:
        moners["text"] = f"{float(x) - 10}"
        passive_gain["text"] = f"{float(y) + 0.1}"
        passive_button.forget()
        upgrade_passive.pack()
        Moners_per_second.pack()
    # låser ba upp passiv inkomst


def add_moner():
    x = float(moners["text"])
    multiplier = multiplier_value["text"]
    moners["text"] = f"{float(x) + 1 * float(multiplier)}"
    moners["text"] = format(float(moners["text"]), '.1f')


def upgrade():
    x = moners["text"]
    multiplier = multiplier_value["text"]
    kost = 10 * float(multiplier)
    if float(x) >= kost or float(x) == kost:
        moners["text"] = f"{float(x) - 10 * float(multiplier)}"
        # ska fixa så att de står hur mycket de kostar sen
        moners["text"] = format(float(moners["text"]), '.1f')
        multiplier_value["text"] = f"{float(multiplier) + 0.1}"
        multiplier_value["text"] = format(float(multiplier_value["text"]), '.1f')
        multi_sign["text"] = "Click multiplier: " + multiplier_value["text"]
        koest = 10 * (float(multiplier_value["text"]))
        koest = format(koest, '.1f')
        upgrade_click_button["text"] = "upgrade Click\nCost: "+koest
        # fuck datorer och hur dem intereagerar med float värden, dedär ovanför tog mig typ en timme att fixa


def passive():
    x = float(moners["text"])
    y = float(passive_gain["text"])
    moners["text"] = f"{float(x) + y}"
    moners["text"] = format(float(moners["text"]), '.1f')
    root.after(1000, passive)


def upgrade_passive():
    y = float(moners["text"])
    x = float(passive_gain["text"])
    pas_kostnad = 10 * (11 * float(x))
    if y >= pas_kostnad or x == pas_kostnad:
        moners["text"] = f"{float(y) - 10 * (11 * float(x))}"
        moners["text"] = format(float(moners["text"]), '.1f')
        passive_gain["text"] = f"{float(x) + 0.1}"
        passive_gain["text"] = format(float(passive_gain["text"]), '.1f')

        Moners_per_second["text"] = "Moners/s: " + str(format(float((x) + 0.1), '.1f'))
        upgrade_passive["text"] = "Passive Upgrade\nCost: "+str(int(10 * (11 * float(x+0.1))))


root.after(1000, passive)
root.title("Pebis")
root.geometry("500x300")

button = ttk.Button(master=root, text="Moners", command=add_moner)
upgrade_click_button = ttk.Button(master=root, text="upgrade Click\nCost: 10", command=upgrade)
multi_sign = tk.Label(text="Click multiplier: "+str(multiplier_value["text"]))
passive_button = ttk.Button(master=root, text="Passive Income\nCost: 10", command=get_passive)
upgrade_passive = ttk.Button(master=root, text="Passive Upgrade\nCost: 11", command=upgrade_passive)

button.pack()
moners.pack()
tk.Label(text="").pack()
upgrade_click_button.pack()
multi_sign.pack()
tk.Label(text="").pack()
passive_button.pack()
"""
ska eventuellt byta från .pack() till .place() för att positionera bättre
.pack suger, eller så gör jag det, eller båda, antagligen bara jag
"""
root.mainloop()

