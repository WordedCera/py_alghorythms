from os import listdir

# Структурирование относительно сложного кода
IN_FOLDER = "C:\\Users\\worde\\Desktop\\Учеба\\data\\demo1\\" 
OUT_FOLDER = "C:\\Users\\worde\\Desktop\\Учеба\\data\\demo1\\saved\\"

# функция обработки единичного файла
def processSinglefile(inFileName, o):
    f = open(f"{IN_FOLDER}/{inFileName}","r", encoding="UTF-8")
    text = f.read()
    f.close()
    lines = text.split("\n")
    for word in lines:
        word_name = word.split(" ")
        out = word_name[1] + ", " + word_name[0] + "\n"
        o.write(out)

o = open(f'{IN_FOLDER}/people2.txt', 'w', encoding="UTF-8")
    
files = listdir("data/demo1")
data2 = []

# Этот блок отвечает за цикл по файлам и за вызов функции обработки единичного файла
for i in files:
    if i.find("data") >= 0:
        processSinglefile(i, o)

o.close()
