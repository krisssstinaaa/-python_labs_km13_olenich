def check(x):
    try:
        int(x)
    except ValueError:
        return False
    return True

r = int(input("Enter the value of R: "))
while check(r) == False or (0 > r or r > 255):
    r = int(input("Invalid input of R, try again: "))
g = int(input("Enter the value of G: "))
while check(g) == False or (0 > g or g > 255):
    g = int(input("Invalid input of G, try again: "))
b = int(input("Enter the value of B: "))
while check(b) == False or (0 > b or b > 255):
    b = int(input("Invalid input of B, try again: "))

system16 = {"1":"1", "2":"2", "3":"3", "4":"4", "5":"5", "6":"6", "7":"7", "8":"8", "9":"9", "0":"0",
            "10":"A", "11":"B", "12":"C", "13":"D", "14":"E", "15": "F"}

if r >= 16:
    first_value1 = str(r//16)
    first_value2 = str(int((r/16 - r//16)*16))
else:
    first_value1 = str(r)
if g >= 16:
    second_value1 = str(g//16)
    second_value2 = str(int((float(g/16) - g//16)*16))
else:
    second_value1 = str(g)
if b >= 16:
    third_value1 = str(b//16)
    third_value2 = str(int((float(b/16) - b//16)*16))
else: 
    third_value1 = str(b)

if r >= 16 and g >= 16 and b >= 16:
    rgb = (first_value1, first_value2, second_value1, second_value2, third_value1, third_value2)
if r <= 16 and g <= 16 and b <= 16:
    rgb = (first_value1, second_value1, third_value1)
if r >= 16 and g >= 16 and b <= 16:
    rgb = (first_value1, first_value2, second_value1, third_value1)
if r >= 16 and g <= 16 and b >= 16:
    rgb = (first_value1, first_value2, second_value1, third_value1, third_value2)
if r <= 16 and g >= 16 and b >= 16:
    rgb = (first_value1, second_value1, second_value2, third_value1, third_value2)
if r <= 16 and g <= 16 and b >= 16:
    rgb = (first_value1, second_value1, third_value1, third_value2)
if r <= 16 and g >= 16 and b <=16:
    rgb =(first_value1, second_value1, second_value2, third_value1)
if r >= 16 and g <= 16 and b <= 16:
    rgb = (first_value1, first_value2, second_value1, third_value1)
newstring = ""
for i in rgb:
    newstring += system16[i]
print("#" + newstring)
