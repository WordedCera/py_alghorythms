import os


IN_FOLDER = "C:\\Users\\worde\\Desktop\\Учеба\\data\\demo1\\" 
OUT_FOLDER = "C:\\Users\\worde\\Desktop\\Учеба\\data\\demo1\\saved\\"
# # command = "calc"
# # os.system(command)
# # os.system("dir")
files = os.listdir("data/demo1")
# # Провести манипуляции только с файлами, в которых есть data
# for i in files:
#     if i.find("data") >= 0:
#         print(i)
#         command = f"copy {IN_FOLDER}{i} {OUT_FOLDER}{i}"
#         os.system(command)

# Из файлов data1/data2 собрать данные в файл people3 в формате фамилия, Имя
data2 = []
o = open(f'{IN_FOLDER}/people2.txt', 'w', encoding="UTF-8")
for i in files:
    if i.find("data") >= 0:
        f = open(f"{IN_FOLDER}/{i}","r", encoding="UTF-8")
        text = f.read()
        f.close()
        lines = text.split("\n")
        for word in lines:
            word_name = word.split(" ")
            out = word_name[1] + ", " + word_name[0] + "\n"
            o.write(out)
o.close()