import random

# Stardew valley plantation calculator and estimator

def Average_of_list(liste):
    return sum(liste) / len(liste)


seed_amount = int(input("Seed amount: "))
seed_cost = int(input("Seed cost: "))
fertilizer_cost = 150
print("Using quality fertilizer")
regular_quality = 0
silver_quality = 0
gold_quality = 0

cost_of_operation = (fertilizer_cost + seed_cost) * seed_amount

regular_list = []
silver_list = []
gold_list = []

for i in range(50):
    for i in range(seed_amount):
        divider = random.randint(0, 100)
        if 10 >= divider >= 0:
            regular_quality = regular_quality + 1
        if 39 >= divider >= 11:
            silver_quality = silver_quality + 1
        if 100 >= divider >= 40:
            gold_quality = gold_quality + 1
    regular_list.append(regular_quality)
    silver_list.append(silver_quality)
    gold_list.append(gold_quality)
    regular_quality = 0
    silver_quality = 0
    gold_quality = 0

regular_average = round(Average_of_list(regular_list))
silver_average = round(Average_of_list(silver_list))
gold_average = round(Average_of_list(gold_list))

regular_profit = int(input("Regular sell price: "))
silver_profit = int(input("Silver sell price: "))
gold_profit = int(input("Gold sell price: "))

brutto_gain = int((regular_profit*regular_average)+(silver_profit*silver_average)+(gold_profit*gold_average))
netto_gain = brutto_gain - cost_of_operation

print("Brutto gain:", brutto_gain)
print("Netto gain:", netto_gain)
