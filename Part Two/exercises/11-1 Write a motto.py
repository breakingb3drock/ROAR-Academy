
with open("motto.txt","w") as file:
    file.write("Fiat Lux!\n")


with open("motto.txt","a") as file:
    file.write("Let there be light!\n")


with open("motto.txt","r") as file:
    updated_content = file.read()
    print("File content after appending:")
    print(updated_content)
