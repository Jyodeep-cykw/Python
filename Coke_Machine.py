original = 50

while original > 0:
    print("Amount Due:", original)
    
    user = int(input("Insert Coin: "))
    
    if user in [25, 10, 5]:
        original -= user
    else:
        print("Invalid coin.")

print("Change Owed:", abs(original))
