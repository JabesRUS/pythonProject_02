f = open("testfile_01.txt", "r", encoding="utf-8")
s = f.readline()
a = int(f.readline())
f.close()
s = s.replace("\n", "")
print(s)
print(a)

