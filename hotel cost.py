city = input("Out of your given choices of Cabo, Tampa, Maui, or New York, where are you planning to go?")
nights = int(input("How many nights do you want to stay here?"))
days = int(input("How many days will you be approximately needing a rental car?"))
misc = float(input("How much do you want to keep aside for random spending?"))


def hotel(nights):
    if nights <= 7:
        return 50*nights
    else:
        return 100*nights

def plane(city):
    if city == "Cabo":
        return 600
    elif city == "Tampa":
        return 575
    elif city == "Maui":
        return 700
    elif city == "New York":
        return 800
    else:
        print("Try again with the given choices.")

def car(days):
    if days >= 1:
        return 200
    elif days >= 7:
        return 400
    else:
        return 350 + 20*days
    
def totaltrip(city, nights, days, misc):
    return plane(city) + hotel(nights) + car(days) + misc

print("plane cost:", plane(city))
print("hotel costs:", hotel(nights))
print("rental car cost:", car(days))
print("the total cost of this trip amounts to:", totaltrip(city, nights, days, misc))