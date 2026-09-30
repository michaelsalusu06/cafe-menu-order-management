menu = ["1.Beef Rendang", "2.Gyudon Bowl", "3.Ayam Goreng", "4.Mie Goreng", "5.Iced Tea"]
price = [25.00, 35.00, 20.00, 15.00, 5.00]
extra = ["6.Fried Egg", "7.Sambal", "8.Extra Rice", "9.Cheese"]

class Order():
    def __init__(self, items=None):
        self.items = items

orders = []

print("Main Menu:")
for i in range (len(menu)):
    print(menu[i])

print("Extras:")
for i in range (len(extra)):
    print(extra[i])

while(True):
    print("Input your order with numbers(1-5) for main courses, and (6-9) for extras type 0 to exit")
    foods = 0

    try:
        foods = int(input())
        if foods < 0 or foods > 9:
            raise ValueError
            print("Invalid input, only input numbers(1-5) for main courses and (6-9) for extras")
    except:
        print("Invalid input, only input numbers(1-5) for main courses and (6-9) for extras")
    
    if(foods == 0):
      break
    
    orders.append(foods)

total = 0
for i in range (len(orders)):
    if orders[i] <= 5:
        total += price[orders[i] - 1]

if total > 50:
    total *= 0.9

print("Your total is: ", total)
print("Pay here: ")
pay = int(input())

while pay < total:
    print("Payment insufficient")
    pay = int(input())

print("Payment success enjoy your meal")




