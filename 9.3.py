import csv
print("Список покупок:")

f = open('2`1214214.csv')
c = list(csv.reader(f, delimiter = ","))

for i in c:
    print(i[0],"-",i[1], "шт. за ", i[2], "руб.")
s = sum([int(i[1])*int(i[2]) for i in c])
print("Итого: ", s, "руб.")