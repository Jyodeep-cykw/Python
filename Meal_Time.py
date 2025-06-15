


def main():
    ans = input("What time is it? ")
    ans = convert(ans)
    if(7<= ans <= 8 ):
        print("Its breakfast time!")
    elif(12 <= ans <= 13):
        print("Its lunch time!")
    elif(18 <= ans <= 19):
        print("Its dinner time!")

def convert(time):
    hr, min = time.split(":")
    new_min = float(min) / 60
    return float(hr) + new_min

main()