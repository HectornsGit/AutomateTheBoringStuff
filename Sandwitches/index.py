import pyinputplus as pyin
import time

prices = {
    "wheat": 30,
    "white": 40,
    "sourdough": 45,
    "turkey": 60,
    "ham": 50,
    "tofu": 70,
    "cheddar": 10,
    "Swiss": 20,
    "mozzarella": 15,
}
sandwich = []
price = 0

# Ask for bread type(inputMenu)
bread = pyin.inputMenu(
    choices=["wheat", "white", "sourdough"], prompt="What kind of bread you want? \n"
)
try:
    sandwich.append(bread)

except:
    print("Excuse me, sir?")

# Ask for protein(inputMenu)
protein = pyin.inputMenu(
    choices=["turkey", "ham", "tofu"], prompt="Which type of protein do you want? \n"
)
try:
    sandwich.append(protein)

except:
    print("Excuse me, sir?")

# Ask if they want cheese(YesNo)
withCheese = pyin.inputYesNo(prompt="Would you like it with cheese?")
try:
    if withCheese == "yes":
        cheese = pyin.inputMenu(
            choices=["cheddar", "Swiss", "mozzarella"],
            prompt="And what kind of cheese you'd like? \n",
        )

        # Ask for cheese type(inputMenu)
        try:
            sandwich.append(cheese)

        except:
            print("Excuse me, sir?")
    else:
        print("Ok, sir")
except:
    print("Excuse me, sir?")


# Ask for number of sandwitches(inputInt)
sandwichesCount = pyin.inputInt(prompt="How many sandwitches do you want? \n", min=1)

try:
    for ingredient in sandwich:
        price += prices[ingredient]
    price = price * sandwichesCount
    if price > 99:
        price = str(price)
        price = price[0] + "," + price[1:] + "€"
    else:
        price = "0." + str(price)
    print(f"ok, sir it will be {price}")
    time.sleep(3)
except:
    print("Excuse me, sir?")
