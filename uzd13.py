
def uzd1(x):
    print("Pirkuma maksa bez PVN ir",x*PVN)
    
def uzd2():
    name = input("Mani sauc:")
    likes = input("Man patīk")
    birthyear = input("Esmu dzimis gadā:")
    dislikes = input("man nepatīk")
    dislikes2 = input("man nepatīk vēl")
    return [name,likes,birthyear,dislikes,dislikes2]
    
def uzd3(x):
    print("tev ir",x,"gadi")
    if x >= 18:
        print("Tu esi pieaudzis")
    else:
        print("esi bērns")
    
def uzd4(x,y):
    while True:
        print("abu skaitļu summa ir",x+y)
        answ=input("Vai vēlies atkārtot šo programmu? y/n")
        if answ =="n":
            break
        else:
            continue

def uzd5():
    for i in range(1,1000):
        print(i)

def uzd6():
    while True:
        x=str(input("vēlies atkārtot programmu? y/n vai 1/0"))
        if x=="y" or x=="1":
            continue
        else:
            break

def uzd7():
    while True:
        guess=float(input("uzmini skaitli no 1-10"))
        if guess < 7:
            print("skaitlis ir mazāks par pareizo skaitli")
        if guess == 7:
            print("tu uzminēji pareizo skaitli.")
            break
        if guess > 7:
            print("skaitlis ir lielāks par pareizo skaitli")
        
def uzd8():
    i = 1
    while True:
        if i % 2 == 0:
            print(i)
        i+=1

def uzd9():
    name=str(input("ievadi savu vārdu"))
    letter=str(input("ievadi savu burtu"))
    iter=0

    for i in name:
        if i == letter:
            iter+=1

    print("vārdā ir",iter,"burti, kas ir",letter)
    
def uzd10():
    count = 0
    howMany = 1000

    for i in range(0,howMany):
        if i%3==0 and i%5==0:
            count+=i
        elif i%3==0:
            count+=i
        elif i%5==0:
            count+=i
        
    print(count)

def uzd10other():
    def fib(x):
        if x==1 or x==2:
            return x
    
    return fib((x-2))+fib((x-1)) # Defineeta fibonachi sequence
    
    count=0

    valuesUnder = []
    i=1
    while True: # visi fibonaci skaitli, kas būs mazaaki par 4 000 000, likti sarakstā
        if fib(i)<4000000:
            valuesUnder.append(fib(i))
            i+=1
        else:
            break
    
    for i in valuesUnder: #saskaititi visi skaitļi, kas ir sarakstā
        if i%2==0:
            count+=i
        
    print(count) #izprintēts rezultāts
    
def uzd11():
    allLetters =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    count=0
    while count < len(allLetters):
        for iter in range(0,len(allLetters)):
            print(allLetters[count]+allLetters[iter])
        count+=1

def uzd12(x):
    print(2**x)
    
uzd9()
    

    
    
        
    