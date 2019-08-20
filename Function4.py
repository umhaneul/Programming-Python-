#p119
def hello(msg="안녕하세요."):
    print(msg + "!")

hello("오랜만이에요.")
hello("강은서")
hello()

def hello2(name="무명",msg="안녕하세요"):
    print(name+"님,"+msg+"!")

hello2("곽가연","오랫만이에요")
hello2()
hello("김민지")
hello2(msg="오랫만이에요")

def hello3(name,msg="안녕하세요"):
    print(name+"님,"+msg+"!")

hello3("김봄이", "오랫만이에요")
hello3("김소현")

def fn2(a, b=[]):
    b.append(a)
    print(b)

fn2(3)
fn2(5)
fn2(10)

#p123
def gugudan(dan):
    for i in range(1,9+1):
        print("{} x {} = {}".format(dan,i,dan*i))

gugudan(3)
#gugudan()

#p125
def sum(*numbers):
    sum_value = 0
    for number in numbers:
        sum_value += number

    return sum_value

reslut = sum(1,3)
print("1 + 3=", reslut)
print("1 + 3 + 5 + 7 = ",sum(1,3,5,7))

#p126
def min(*number):
    min_value = number[0]
    for number in number:
        if min_value > number:
            min_value = number
    
    return min_value

print("min(1,3) = ",min(1,3))
print("min(0,3,-11) = ",min(0,3,-11))

def max(*number2):
    mmax_value = number2[0]
    for number in number2:
        if max_value < number2:
            max_value = number2
    
    return mmax_value

print("max(5,3) = ",max(5,3))
print("max(0,3,-11) = ",max(0,3,-11))

#p127
def multi_num(mulit, start, end) :
    result = []
    for n in range(start, end) :
        if n % multi == 0:
            result.append(n)
    
    return result

print("multi_num(17,1,200) = ",multi_num(17,1,200))
print("multi_num(3,1,100 = ",multi_num(3,7,100))

#p128
def min_max(*args):
    min = args[0]
    max = args[0]
    for arg in args:
        if min > arg:
            min = arg
        if max < arg:
            max = arg
    
    return min,max

print("min_max(52,-3,23,89,-21")
min_value, max_value = min_max(52,-3,23,89,-21)
print("최솟값: ",min_value, "최댓값: ", max_value)