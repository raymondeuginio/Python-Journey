MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk" : 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def checkstock (namaminuman):
    """ Selain untuk cek stock apakah ada atau engga? 
    fungsi ini juga akan mengurangi resources (variabel global)"""
    global resources
    #cek air
    if resources['water'] < MENU[namaminuman]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
        return 777 # 777 kode artinya gabisa melakukan transaksi
    else:
        resources['water'] -= MENU[namaminuman]["ingredients"]["water"]
    #cek susu
    if resources['milk'] < MENU[namaminuman]["ingredients"]["milk"]:
        print("Sorry there is not enough milk.")
        return 777
    else:
        resources['milk'] -= MENU[namaminuman]["ingredients"]["milk"]

    #cek kopi
    if resources['coffee'] < MENU[namaminuman]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
        return 777
    else:
        resources['coffee'] -= MENU[namaminuman]["ingredients"]["coffee"]
    

def mesinpenghitung (userharusbayar, uq, ud, un, up):
    sum = 0
    sum += uq * 0.25
    sum += ud * 0.10
    sum += un * 0.05
    sum += up * 0.01
    if userharusbayar > sum:
        print("Sorry that's not enough money. Money Refunded")
        return 888 # 888 kode artinya duitnya kurang.
    else:
        return (sum - userharusbayar)


pendapatan = 0
user_input = "on"
while user_input != "off":
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "espresso":
        if checkstock("espresso") == 777:
            continue
        else:
            userharusbayar = MENU["espresso"]["cost"]

    elif user_input == "latte":
        if checkstock("latte") == 777:
            continue
        else:
            userharusbayar = MENU["latte"]["cost"]

    elif user_input == "cappuccino":
        if checkstock("cappuccino") == 777:
            continue
        else:
            userharusbayar = MENU["cappucino"]["cost"]

    elif user_input == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money : ${pendapatan}")
    elif user_input == "off":
        pass
    else:
        print("INVALID INPUT")
        continue

    print("Please insert coins.")
    uq = int(input("How many quarters?:"))
    ud = int(input("How many dimes?:"))
    un = int(input("How many nickles?:"))
    up = int(input("How many pennies?:"))
    if mesinpenghitung (userharusbayar, uq, ud, un, up) == 888:
        continue
    else:
        pendapatan += userharusbayar
        print(f"Here is ${mesinpenghitung (userharusbayar, uq, ud, un, up)} in change.")
        print(f"Here is your {user_input}. Enjoy!")