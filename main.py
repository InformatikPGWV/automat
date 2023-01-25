import time
from rich import print

from os import system, name

products = {
    1:{
        "name":"Kinder Bueno Double Pack",
        "price": 1.20,
        "quantity": 15
    },
    2:{
        "name":"M&Ms Chocolate",
        "price": 1.50,
        "quantity": 42
    },
    3:{
        "name":"M&Ms White Chocolate",
        "price": 1.70,
        "quantity": 1
    },
    4:{
        "name":"Haribo Gummibärchen",
        "price": 1.80,
        "quantity": 0
    },
    5:{
        "name":"Mettwurst",
        "price": 1.20,
        "quantity": 10
    }
}

moneyPieces = [0.01, 0.02, 0.05, 0.10, 0.20, 0.50, 1.00, 2.00]

guthaben = 0.00

def select_product():
    global guthaben
    guthaben = round(guthaben, 2)
    clearScreen()
    for key, value in products.items():
        if(value["quantity"] > 0):
            print(f"{key}: {value['name']} - {round(value['price'],2)}€ - [green]\[{value['quantity']} in stock][/green]")
        else:
            print(f"{key}: {value['name']} - {round(value['price'],2)}€ - [red] \[OUT OF STOCK] [/red]")

    print("Bitte wählen sie ein Produkt aus - Drücken Sie \"X\" zum abbrechen")
    print(f"Guthaben: {guthaben}€")


    selected_product = input(">>")

    if selected_product.upper() == "X":
        askMoney()

    try:
        selected_product = int(selected_product)
    except:
        clearScreen()
        print("[red]Es ist ein Fehler aufgetreten![/red]")
        time.sleep(1)
        select_product()

    if selected_product in products:
        if products[selected_product]["quantity"] > 0:
            if guthaben >= products[selected_product]["price"]:
                guthaben -= products[selected_product]["price"]
                products[selected_product]["quantity"] -= 1
                clearScreen()
                print(f"Sie haben {products[selected_product]['name']} gekauft")
                print(f"Sie haben noch {round(guthaben,2)}€ übrig")
                time.sleep(1)
                askMoney()
            else:
                clearScreen()
                print("[red]Sie haben nicht genug Geld![/red]")
                time.sleep(1)
                askMoney()
        else:
            clearScreen()
            print("[red]Das Produkt ist nicht mehr verfügbar![/red]")
            time.sleep(1)
            select_product()
    else:
        clearScreen()
        print("[red]Bitte geben Sie ein gültiges Produkt ein![/red]")
        time.sleep(1)
        select_product()

def askMoney():
    global guthaben
    while True:
        guthaben = round(guthaben, 2)
        clearScreen()
        print("Bitte Geld einwerfen - Produktwahl mit \"P\" öffnen - Geldausgabe mit \"X\"")
        print(f"Aktualles Guthaben: {guthaben}€")
        moneyIn = input(">>")
        if moneyIn.upper() == "P":
            break
        if moneyIn.upper() == "X":
            if guthaben > 0:
                print("here comes the Money")
                print(f"{guthaben}€ wird ausgezahlt.")
            else:
                print("Es kann nichts augezahlt werden.")
            time.sleep(1)
            guthaben = 0.0
            break
        try:
            float(moneyIn)
            if float(moneyIn) in moneyPieces:
                guthaben += float(moneyIn)
                print(f"Das Guthaben wurde um {moneyIn}€ erhöht")
            else:
                clearScreen()
                print("[red]Wir akzeptieren nur Euromünzen und Dogecoin![/red]")
                time.sleep(1)
        except:
            clearScreen()
            print("[red]Bitte geben Sie eine gültige Zahl ein![/red]")
            time.sleep(1)
            continue
    
    if guthaben == 0:
        intro()
    else:
        select_product()

def clearScreen():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def main():
    askMoney()
    
if __name__ == "__main__":
    main()