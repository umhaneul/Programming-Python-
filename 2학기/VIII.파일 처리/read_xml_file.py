#p244
import xml.etree.ElementTree as ET

f = open("order.xml",encoding="UTF-8")
string = f.read()
tree = ET.ElementTree(ET.fromstring(string)) #넣어줌으로써 xml로 바뀜
root = tree.getroot()
#print(root.tag)
#print(root.text)
for child in root :
    print("tag : ",child.tag,"text : ", child.text)
f.close()

