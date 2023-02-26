sampleList = [2, 6, 9, 23, 45, 90, 91, 99, 127]
element = 127

low = 0
high = len(sampleList)-1
mid = (low+high) // 2
present = False

while low <= high:
    if element == sampleList[mid]:
        print(mid)
        present = True
        break
    elif element < sampleList[mid]:
        high = mid - 1
        mid = (low+high) // 2
    else:
        low = mid + 1
        mid = (low+high) // 2

if not present:
    print("Not Present")