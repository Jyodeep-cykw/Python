punctuation = ["!", "#", "$", "%", "&", "(", ")", "*", "+", ",", "-", ".", "/", ":", 
               ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~"]

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if len(s) < 2 or len(s) > 6:
        return False

    for i in s:
        if i in punctuation:
            return False

    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False

    start = False  
    for i in range(len(s)):
        if s[i].isdigit():
            if start == False:
                start = True
                if s[i] == "0":  
                    return False
        elif start == True:
            return False

    return True

main()
