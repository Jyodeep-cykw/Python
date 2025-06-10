def convert(smile):
    if ":)" in smile:
        smile = smile.replace(":)", "😊")
        return smile
    elif ":(" in smile:
        smile = smile.replace(":(", "😔")
        return smile
    else:
        return "No faces found. Try again!"


smile = input("")
print(convert(smile))
