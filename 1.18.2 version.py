print("\ncurrently only supporting pressing, sawing, deploying and spouting/filling")
print("format should be 'modname:item_id/fluid_id(if in spout)'\nExample: 'create:copper_sheet' or 'minecraft:wheat'")
print("device names: saw, press, deployer, spout")
recipe_name = input("\nName of recipe(not important): ")
input_item = input("Input item: ").lower()
trans_item = input("Transition item: ").lower()
output_item = input("Output: ").lower()
how_many = int(input("How many?: "))
loops = input("Loops: ")
amount_of_devices = int(input("Amount of devices(maximum of 6): "))


def add_device(device):
    device = device.lower()
    dicte = {
        "press": ".addStep<mods.createtweaker.PressingRecipe>()",
        "saw": ".addStep<mods.createtweaker.CuttingRecipe>()"
    }
    if device == "spout":
        fluid = input("Spout fluid: ").lower()
        fluid_amount = input("how many milli buckets(max 1000): ")
        return f'.addStep<mods.createtweaker.FillingRecipe>((rb) => rb.require(<fluid:{fluid}>*{fluid_amount}))'
    elif device == "deployer":
        deployer_item = input("Deployer item: ").lower()
        return f'.addStep<mods.createtweaker.DeployerApplicationRecipe>((rb) => rb.require(<item:{deployer_item}>))'
    else:
        return dicte.get(device)


sequence_list = [
    f'<recipetype:create:sequenced_assembly>.addRecipe(<recipetype:create:sequenced_assembly>.builder("{recipe_name}")',
    f'.require(<item:{input_item}>)', f'.transitionTo(<item:{trans_item}>)', f'.loops({loops})',
    f'.addOutput(<item:{output_item}>*{how_many}, 1)']

rang = 0
for i in range(0, amount_of_devices):
    rang += 1
    sequence_list.append(add_device(input(f"device {rang}: ")))

sequence_list.append(');')

rango = 0
f = open(f"{recipe_name}.zs", "a")
for i in range(0, len(sequence_list)):
    f.write(sequence_list[rango])
    f.write("\n")
    rango += 1
