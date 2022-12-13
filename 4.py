from random import randint as r

count = int(input('Введите количество учеников на физкультуре: '))
classmate = [r(158, 182) for i in range(count)]
classmate = sorted(classmate)
classmate = list(reversed(classmate))
print(classmate)

student_hight = int(input('Введите рост Пети: '))

for j in range(len(classmate)):
    if student_hight >= classmate[j]:
        print(j + 1)
        break
