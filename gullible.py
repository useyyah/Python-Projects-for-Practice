while True:
    response = input("Do you want to know how to keep a gullible person busy for hours Y/N").lower()
    if response.lower() == "no" or response.lower() == "n":
        break
    if response.lower() == "yes" or response.lower() == "y":
        continue
    print(f"{response} is not a valid yes/no response.")

print("Thanks for playing!!!")
