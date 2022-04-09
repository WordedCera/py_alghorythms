x = 1234
y = 0

# try: 
#     z = x/y
#     print(z)
#     print("Program Proceeds")
# except:
#     print("Произошла ошибка")
#     # pass # Не проглатывайте ошибку - антипаттерн
# print("Program Proceeds")


f = open("data/nums.csv")
text = f.read()
f.close()
lines = text.split("\n")
for line in lines:
    try:
        splitted = line.split(";")
        x = int(splitted[0])
        y = int(splitted[1])
        z = x/y
        print(f"{x}:{y}={z}")
    except:
        # pass
        print(f"ERROR: {line}")

