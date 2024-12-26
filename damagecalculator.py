import math
import random

def calculate_damage(level, power, attack, modifiers, defense):
    base_damage = ((2*level/5+2)*power*(attack/defense))/50
    total_damage = base_damage * modifiers
    return math.floor(total_damage)

def calculate_modifiers(targets, critical, type, bonus, burn):

    random_multiplier = random.uniform(0.85, 1.00)
    modifiers = targets*critical*type*bonus*burn*random_multiplier
    return modifiers
while True:
    print("Input damage parameters:\n")
    level = int(input("Level: "))
    power = int(input("Power: "))
    attack = int(input("Attack: "))
    defense = int(input("Defense: "))
    print("\n")
    print("Input modifier parameters:\n")
    targets = float(input("Targets: "))
    critical = float(input("Critical: "))
    type = float(input("Type: "))
    bonus = float(input("Bonus: "))
    burn = float(input("Burn: "))

    modifiers = calculate_modifiers(targets, critical, type, bonus, burn)

    damage = calculate_damage(level, power, attack, modifiers, defense)
    print(f"\nCalculated Damage: {damage}\n")