days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month = ["január", "február", "március", "április", "május", "június", "július", "augusztus", "szeptember", "október",
         "november", "december"]


months_and_days = []
for i in range(12):
    months_and_days.append(month[i])
    months_and_days.append(days_in_month[i])
print(months_and_days)


szamok = [34, 97, 12, -15, 35, 10]

max=szamok[0]
for i in range(len(szamok)):
    if(szamok[i]>max):
        max=szamok[i]
print(max)

min=szamok[0]
hely = 0
for i in range(len(szamok)):
    if(szamok[i]<min):
        min=szamok[i]
        hely = i
print(min)
print(hely)

for i in range(len(szamok)):
    if(szamok[i] == min):
        print(i)