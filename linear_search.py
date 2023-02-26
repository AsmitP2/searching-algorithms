#linear search
sampleList = [12, 56, 290, 48, 22, 100, 84]

element = int(input("Number: "))

x = 0
present = False

for i in sampleList:
    if element == i:
        print(x)
        present = True
    x+=1

if not present:
    print("Not Present")