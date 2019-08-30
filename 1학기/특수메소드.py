#p202
class DeletableClass:
    def __del__(self): #자바에서 toStirng()과 비슷
        print("delete")

d = DeletableClass()
del d

#p203
class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return "Person 설명, 이름은 " + self.name+ " 키는" + str(self.height)

    def __getitem__(self,key) :
        if key == "name":
            return self.name
        if key == "age" :
            return self.age
        return None

    def __len__(self):
        return len(self.name)

    def __del__(self) :
        print(self.name + "이 사라졌습니다.")

p = Person("양수빈",18,158)
print(p)
print("Person 설명, 이름은 "+p.name + "키는"+str(p.height))
print(len(p)) #3
print(len(Person("지코",29,182))) #2
print(p["name"])
print(p["age"])
print(p["weight"])

del p  #양수빈이 사라졌습니다.
#print(p)
p = Person("양수빈",19,170) #양수빈이 나타났습니다.