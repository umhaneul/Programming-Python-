f = open("file.txt","a") #a: append(이어서쓰기) , w:덮어쓰기

f.write("Hello")
f.write("\n")
f.write("World")

f.close()