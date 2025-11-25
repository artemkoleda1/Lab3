
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

def get_quarter(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4

quarter1 = get_quarter(x1, y1)
quarter2 = get_quarter(x2, y2)

if quarter1 == quarter2:
    quarters_roman = {1: "I", 2: "II", 3: "III", 4: "IV"}
    print(f"Yes, {quarters_roman[quarter1]}")
else:
    print("No")
