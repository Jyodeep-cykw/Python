while True:
    
    try:
            
        user = input("Fraction: ")
        x, y = user.split("/")

        percent = int(x) / int (y)
        
        if percent <=1:
            break        
    except (ValueError , ZeroDivisionError):
        pass

f = int(percent * 100)

if f <=1:
    print("E")

if f >= 99:
    print("F")

else:
    print(f"{f}%")










