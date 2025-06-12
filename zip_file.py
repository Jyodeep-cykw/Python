file_name = input("File Name: ")

if (file_name[-3:] == "png"):
    print("image/png")
elif (file_name[-3:] == "gif"):
    print("image/gif")
elif (file_name[-3:] == "jpg"):
    print("image/jpeg")
elif (file_name[-3:] == "jpeg"):
    print("image/jpeg")
elif (file_name[-3:] == "pdf"):
    print("image/pdf")
elif (file_name[-3:] == "txt"):
    print("image/txt")
elif (file_name[-3:] == "zip"):
    print("image/zip")
else:
    print("application/octet-stream")