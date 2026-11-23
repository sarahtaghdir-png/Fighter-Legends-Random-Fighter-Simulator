import random
import time

fighters = ["F-35", "F-22", "F-15", "F-14", "SU-57", "J-20"]

countries = {
    "F-35": "آمریکا",
    "F-22": "آمریکا",
    "F-15": "آمریکا",
    "F-14": "آمریکا",
    "SU-57": "روسیه",
    "J-20": "چین"
}

print("====================================")
print("          FIGHTER LEGENDS")
print("====================================")

name = input("نام خلبان را وارد کنید: ")

while True:

    print("\nدر حال آماده سازی اطلاعات...")
    time.sleep(1)

    fighter = random.choice(fighters)

    power = random.randint(60, 100)
    speed = random.randint(60, 100)
    stealth = random.randint(60, 100)
    fuel = random.randint(30, 100)
    pilot = random.randint(50, 100)

    print("\n========== FLIGHT DATA ==========")

    print("Pilot:", name)
    print("Fighter:", fighter)
    print("Country:", countries[fighter])

    print("\n========== STATISTICS ==========")

    print("Power:", power, "/100")
    print("Speed:", speed, "/100")
    print("Stealth:", stealth, "/100")
    print("Fuel:", fuel, "/100")
    print("Pilot Skill:", pilot, "/100")

    score = (power + speed + stealth + pilot) // 4

    print("\n========== FINAL ANALYSIS ==========")

    print("Overall Score:", score, "/100")

    if fuel < 40:
        print("WARNING: LOW FUEL!")

    if score >= 90:
        print("Performance: EXCELLENT!")
    elif score >= 75:
        print("Performance: VERY GOOD!")
    elif score >= 60:
        print("Performance: GOOD!")
    else:
        print("Performance: NORMAL")

    result = random.randint(1, 100)

    print("\nChecking flight conditions...")
    time.sleep(1)

    if result <= score:
        print("FLIGHT STATUS: SUCCESSFUL!")
    else:
        print("FLIGHT STATUS: UNSUCCESSFUL!")

    print("\n====================================")

    again = input("Play again? (yes/no): ")

    if again != "yes":
        print("\nGoodbye Pilot", name)
        break

print("\n       END OF SIMULATION")
