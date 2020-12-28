a = input("Введите цифры: ").split()
for i in range(1, len(a), 2):
    a.insert(i - 1, a.pop(i))
print(a)