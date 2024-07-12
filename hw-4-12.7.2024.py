# הדפס את כל המספרים מ - 10 עד 20
for i in range(10, 21):
    print(i, end=" ");
print();

# הדפס את כל המספרים מ- 10 ועד 20 בדילוגים של ,2
for i in range(10, 21, 2):
    print(i, end=" ");
print();

# קליטת דילוג מהמשתמש והדפסת המספרים מ-10 עד 20 בהתאם
gap = int(input("please enter the gap? "));
for i in range(10, 21, gap):
    print(i, end=" ");
print();

# קליטת נקודת התחלה, נקודת סיום ודילוג מהמשתמש והדפסת המספרים בהתאם
start_point = int(input("please enter the start point? "));
end_point = int(input("please enter the end point? "));
gap = int(input("please enter the gap? "));

for i in range(start_point, end_point + 1, gap):
    print(i, end=" ");
print();






