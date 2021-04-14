s = "Привет! Я строка в файле!"
a = 100
b = "*"
f = open("testfile_01.txt", "w", encoding="utf-8")
f.write(s + "\n")
f.write(str(a +1) + "\n")
f.write(b + "\n")
f.close()
