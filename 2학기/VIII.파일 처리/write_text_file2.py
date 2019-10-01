f = open("file.txt","w",encoding="utf-8") #encoding : 컴퓨터가 알아들을 수 있도록 0101로 바꾸어주는 것

f.write("반갑다")
f.write("\n")
f.write("세상아")

f.close()