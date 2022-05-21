import tkinter as tk
from tkinter import ttk

# detta är ba cookie clicker fast dålig

root = tk.Tk()

pas_unlocked = False
multiplier_value = tk.Label(text=1)
moners = tk.Label(text=0)
# ska fixa bättre namn för valutan senare, just nu bryr jag mig inte
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
    # låser ba upp passiv inkomst


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
        multi_sign.update()
        # fuck datorer och hur dem intereagerar med float värden, dedär ovanför tog mig typ en timme att fixa


def passive():
    if pas_unlocked:
        x = float(moners["text"])
        y = float(passive_gain["text"])
        moners["text"] = f"{float(x) + y}"
        moners["text"] = format(float(moners["text"]), '.1f')
    root.after(1000, passive)


def upgrade_passive():
    global pas_kostnad
    y = float(moners["text"])
    x = float(passive_gain["text"])
    pas_kostnad = 10 * (11 * float(x))
    if y >= pas_kostnad or x == pas_kostnad:
        moners["text"] = f"{float(y) - 10 * (11 * float(x))}"
        moners["text"] = format(float(moners["text"]), '.1f')
        passive_gain["text"] = f"{float(x) + 0.1}"
        passive_gain["text"] = format(float(passive_gain["text"]), '.1f')
        # jag vet inte hur jag ska visa hur mycket det kostar än, men de står där ovanför


root.after(1000, passive)
root.title("Pebis")
root.geometry("500x300")

button = ttk.Button(master=root, text="Moners", command=add_moner)
blank = tk.Label(text="")
upgrade_click_button = ttk.Button(master=root, text="upgrade Click", command=upgrade)
multi_sign = tk.Label(text="Click multiplier:")
passive_button = ttk.Button(master=root, text="Passive Income", command=get_passive)
upgrade_passive = ttk.Button(master=root, text="Passive Upgrade", command=upgrade_passive)

button.pack()
moners.pack()
blank.pack()
upgrade_click_button.pack()
multi_sign.pack()
multiplier_value.pack()
passive_button.pack()
"""
ska eventuellt byta från .pack() till .place() för att positionera bättre
.pack suger, eller så gör jag det, eller båda, anntagligen bara jag
"""
root.mainloop()
